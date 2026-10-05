#!/usr/bin/env python3

from prompts import SYSTEM_PROMPT
from ai_call_schema import FUNC_SCHEMA, FUNC_MAP, WORK_DIR, is_partial_func

from typing import NamedTuple, Optional, TypeIs
from collections.abc import Iterable, Iterator, Sequence

import json
from os import environ
from time import sleep
from argparse import ArgumentParser, Namespace

from dotenv import load_dotenv

from openai import APIStatusError, RateLimitError, OpenAI, Omit, omit
from openai.types import CompletionUsage
from openai.types.shared import ChatModel

from openai.types.chat import (
    ChatCompletion,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionToolMessageParam,
    ChatCompletionToolUnionParam,
    ChatCompletionMessageToolCallUnion,
    ChatCompletionMessageFunctionToolCall,
    ChatCompletionAssistantMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam
)

from openai.types.chat.chat_completion_message_function_tool_call_param import (
    ChatCompletionMessageFunctionToolCallParam, Function as Requested_Func_Args
)

AI_API_KEY_NAME = "OPENROUTER_API_KEY"
AI_MODEL = "openrouter/free"
AI_URL = "https://OpenRouter.ai/api/v1"

AI_MAX_ITERS = 20; AI_MAX_ITERS_RANGE = range(AI_MAX_ITERS)
SLEEP_DELAY = 3 # sleep pause in seconds

NamedArgs = dict[str, list[str] | str]

class FuncNamedArgs(NamedTuple):
    call_id: str
    func_name: str
    named_args: NamedArgs
    json_error: str


class Cli_Prompt_Args(Namespace):
    user_prompt: str
    verbose: bool


def parse_cli_args() -> Cli_Prompt_Args:
    parser = ArgumentParser(description="AI Code Assistant Agent")

    parser.add_argument("user_prompt", type=str, help="AI prompt")

    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Verbose output"
    )

    return parser.parse_args( namespace=Cli_Prompt_Args() )


def main():
    if ( args := parse_cli_args() ).verbose:
        print("\nUser prompt:", args.user_prompt, '', sep='\n')

    if not (load_dotenv() and ( api_key := environ.get(AI_API_KEY_NAME) )):
        raise RuntimeError(AI_API_KEY_NAME + ' not found in file ".env"')

    client = OpenAI( base_url=AI_URL, api_key=api_key )

    token_count = CompletionUsage(
        prompt_tokens=0, completion_tokens=0, total_tokens=0
    )

    sys_behavior = ChatCompletionSystemMessageParam(
        role="system", content=SYSTEM_PROMPT
    )

    user_prompt = ChatCompletionUserMessageParam(
        role="user", content=args.user_prompt
    )

    messages: list[ChatCompletionMessageParam] = [ sys_behavior, user_prompt ]
    exit_code = 0 # 0: Success, 1: Failure

    for _ in AI_MAX_ITERS_RANGE:
        response = ask_ai(client, messages, FUNC_SCHEMA)
        if not response: continue

        chat_completion, token_usage = log_ai_responses(response, args.verbose)

        merge_token_usage(token_count, token_usage)

        if isinstance(chat_completion, Sequence): messages += chat_completion
        else: break # No more tool calls requested by the AI assistant

    else:
        print(AI_MAX_ITERS, "AI max iterations has been reached!")
        print("Cancelling this AI agent session to save tokens!")
        exit_code = 1 # Failure

    print("\n- Total spent tokens for this session:")
    log_ai_token_usage(token_count)

    exit(exit_code)


def ask_ai(
    client: OpenAI,
    messages: Iterable[ChatCompletionMessageParam],
    functions: Iterable[ChatCompletionToolUnionParam] | Omit = omit,
    model: ChatModel | str = AI_MODEL,
    randomness: Optional[float | Omit] = 0,
    sampling_size: Optional[float | Omit] = omit
) -> ChatCompletion | None:
    try: return client.chat.completions.create(
        messages=messages,
        model=model,
        tools=functions,
        temperature=randomness,
        top_p=sampling_size
    )

    except RateLimitError as e:
        print("\nAPI call rate limit exceeded with code status:", e.status_code)
        sleep(SLEEP_DELAY) # delaying next AI API request...

    except APIStatusError as e:
        print(f"API Status Error {e.status_code}:", e.message)
        sleep(SLEEP_DELAY) # delaying next AI API request...


def get_message_and_usage_from_ai_response(
    response: ChatCompletion
) -> tuple[ChatCompletionMessage, CompletionUsage]:
    if not response.usage: raise RuntimeError("Failed AI request!")
    return response.choices[0].message, response.usage


def merge_token_usage(
    target: CompletionUsage, source: CompletionUsage
) -> CompletionUsage:
    target.prompt_tokens += source.prompt_tokens
    target.completion_tokens += source.completion_tokens
    target.total_tokens += source.total_tokens

    return target


def log_ai_token_usage(token_stat: CompletionUsage) -> CompletionUsage:
    print("Prompt tokens:", token_stat.prompt_tokens)
    print("Response tokens:", token_stat.completion_tokens)
    print("Total tokens:", token_stat.total_tokens, '\n')

    return token_stat


def log_ai_responses(
    response: ChatCompletion, verbose: bool = True
) -> tuple[
        ChatCompletionMessage | list[ChatCompletionMessageParam],
        CompletionUsage
    ]:
    print("\nModel used:", response.model, '\n')

    message, usage = get_message_and_usage_from_ai_response(response)
 
    if verbose: log_ai_token_usage(usage)

    if not message.tool_calls:
        print("Response:", message.content, sep='\n')
        return message, usage # final AI's response for the user's prompt

    assistant_prompt: ChatCompletionAssistantMessageParam = {
        "role": "assistant",
        "content": message.content,
        "tool_calls": []
    }

    call_results: list[ChatCompletionMessageParam] = [ assistant_prompt ]

    for call in get_func_args_from_tool_calls(message.tool_calls):
        print(" - Calling function: " + call.func_name, end='')
        print(verbose and f"({call.named_args})" or "")

        append_new_call_params_to_assistant_role(call, assistant_prompt)

        call_results.append(result := call_function(call))
        if verbose: print(f"\n```\n{result['content']}\n```")

    return call_results, usage


def append_new_call_params_to_assistant_role(
    call: FuncNamedArgs, assistant: ChatCompletionAssistantMessageParam
) -> ChatCompletionMessageFunctionToolCallParam:
    args = json.dumps(call.named_args)
    func = Requested_Func_Args(name=call.func_name, arguments=args)

    tool_call_params = ChatCompletionMessageFunctionToolCallParam(
        id=call.call_id, type="function", function=func
    )

    if "tool_calls" in assistant and isinstance(assistant["tool_calls"], list):
        assistant["tool_calls"].append(tool_call_params)

    return tool_call_params


def call_function(
    call: FuncNamedArgs, work_dir: str = WORK_DIR
) -> ChatCompletionToolMessageParam:
    if (name := call.func_name) not in FUNC_MAP:
        res = f"Error: Unknown function: '{name}()'!"

    elif call.json_error: res = call.json_error

    else:
        func = FUNC_MAP[name]
        args = call.named_args

        try:
            res = func(**args) if is_partial_func(
                func) else func(work_dir, **args)

            if not res:
                raise RuntimeError(f"No content returned by func '{name}()'!")

        except TypeError as e:
            res = (
                f"Error: Invalid arguments for '{name}()': {e}! Please check "
                "the tool schema and try again without unsupported parameters."
            )

    return ChatCompletionToolMessageParam(
        role="tool", tool_call_id=call.call_id, content=res
    )


def get_func_args_from_tool_calls(
    tool_calls: Iterable[ChatCompletionMessageToolCallUnion]
) -> Iterator[FuncNamedArgs]:
    # return map( mapped_func_args, filter(is_func_tool, tool_calls) )

    return (
        mapped_func_args(tool_call)
        for tool_call in tool_calls if is_func_tool(tool_call)
    )


def is_func_tool(
    tool_call: ChatCompletionMessageToolCallUnion
) -> TypeIs[ChatCompletionMessageFunctionToolCall]:
    return tool_call.type == "function"


def mapped_func_args(
    func_call: ChatCompletionMessageFunctionToolCall
) -> FuncNamedArgs:
    raw_args = func_call.function.arguments or "{}"
    json_err = ""

    try: parsed_args: NamedArgs = json.loads(raw_args)

    except json.JSONDecodeError as e:
        parsed_args = {}

        json_err = (
            "Error: Failed to parse arguments '" + raw_args + "' as valid JSON!"
            "\nPlease make sure your named arguments conform to the requested "
            "`ChatCompletionToolUnionParam` schema and try again.\n"
            "`JSONDecodeError` message: " + e.msg + "\n... while deserializing "
            "JSON document '" + e.doc + "' via `json.loads()` at index "
            f"position [{e.pos}]."
        )

    return FuncNamedArgs(
        func_call.id,
        func_call.function.name,
        parsed_args,
        json_err
    )


if __name__ == "__main__": main()
