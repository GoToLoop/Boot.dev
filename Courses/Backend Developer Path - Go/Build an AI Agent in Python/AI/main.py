#!/usr/bin/env python3

from prompts import SYSTEM_PROMPT
from ai_call_schema import FUNC_SCHEMA, FUNC_MAP, WORK_DIR, is_partial_func

from typing import NamedTuple, Iterable, Sequence, Optional, TypeIs

from os import environ
from argparse import ArgumentParser, Namespace
import json

from dotenv import load_dotenv

from openai import OpenAI, Omit, omit
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
    ChatCompletionMessageFunctionToolCallParam
)

from openai.types.chat.chat_completion_message_function_tool_call_param import (
    Function
)

AI_API_KEY_NAME = "OPENROUTER_API_KEY"
AI_MODEL = "openrouter/free"
AI_URL = "https://OpenRouter.ai/api/v1"

AI_MAX_ITERS = 20; AI_MAX_ITERS_RANGE = range(AI_MAX_ITERS)

NamedArgs = dict[str, list[str] | str]

class FuncNamedArgs(NamedTuple):
    call_id: str
    func_name: str
    named_args: NamedArgs


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

    messages: list[ChatCompletionMessageParam] = [
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": args.user_prompt }
    ]

    for _ in AI_MAX_ITERS_RANGE:
        response = ask_ai(client, messages, FUNC_SCHEMA)
        chat_completion = log_ai_responses(response, args.verbose)

        if isinstance(chat_completion, Sequence): messages += chat_completion
        else: break # No more tool calls requested by the AI assistant

    else:
        print(AI_MAX_ITERS, "AI max iterations has been reached!")
        print("Cancelling this AI agent session to save tokens!")
        exit(1)


def ask_ai(
    client: OpenAI,
    messages: Iterable[ChatCompletionMessageParam],
    functions: Iterable[ChatCompletionToolUnionParam] | Omit = omit,
    model: ChatModel | str = AI_MODEL,
    randomness: Optional[float | Omit] = 0,
    sampling_size: Optional[float | Omit] = omit
) -> ChatCompletion:
    return client.chat.completions.create(
        messages=messages,
        model=model,
        tools=functions,
        temperature=randomness,
        top_p=sampling_size
    )


def log_ai_responses(
    response: ChatCompletion,
    verbose=True
) -> ChatCompletionMessage | list[ChatCompletionMessageParam]:
    print("\nModel used:", response.model, '\n')

    message, usage = get_message_and_usage_from_ai_response(response)
 
    if verbose:
        print("Prompt tokens:", usage.prompt_tokens)
        print("Response tokens:", usage.completion_tokens, '\n')

    if not message.tool_calls:
        print("Response:", message.content, sep='\n')
        return message # final AI's response for the user's prompt

    assistant: ChatCompletionAssistantMessageParam = {
        "role": "assistant",
        "content": message.content,
        "tool_calls": []
    }

    call_results: list[ChatCompletionMessageParam] = [ assistant ]

    for call in get_func_args_from_tool_calls(message.tool_calls):
        print(" - Calling function: " + call.func_name, end='')
        print(verbose and f"({call.named_args})" or "")

        append_new_call_params_to_assistant_role(call, assistant)

        call_results.append(result := call_function(call))
        if verbose: print(f"\n-> {result['content']}")

    return call_results


def append_new_call_params_to_assistant_role(
    call: FuncNamedArgs,
    assistant: ChatCompletionAssistantMessageParam
) -> ChatCompletionMessageFunctionToolCallParam:
    id = call.call_id
    name = call.func_name
    args = json.dumps(call.named_args)
    func = Function(name=name, arguments=args)

    tool_call_params = ChatCompletionMessageFunctionToolCallParam(
        id=id, type="function", function=func
    )

    if "tool_calls" in assistant and isinstance(assistant["tool_calls"], list):
        assistant["tool_calls"].append(tool_call_params)

    return tool_call_params


def get_message_and_usage_from_ai_response(
    response: ChatCompletion
) -> tuple[ChatCompletionMessage, CompletionUsage]:
    if not response.usage: raise RuntimeError("Failed AI request!")
    return response.choices[0].message, response.usage


def get_func_args_from_tool_calls(
    tool_calls: Iterable[ChatCompletionMessageToolCallUnion]
) -> Iterable[FuncNamedArgs]:
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

    return FuncNamedArgs(
        func_call.id,
        func_call.function.name,
        json.loads(func_call.function.arguments or "{}")
    )


def call_function(call: FuncNamedArgs) -> ChatCompletionToolMessageParam:
    if (name := call.func_name) not in FUNC_MAP:
        result = "Error: Unknown function: " + name

    else:
        func = FUNC_MAP[name]
        args = call.named_args

        result = func(**args) if is_partial_func(
            func) else func(WORK_DIR, **args)

        if not result:
            raise RuntimeError("No content returned by function " + name)

    return ChatCompletionToolMessageParam(
        role="tool", tool_call_id=call.call_id, content=result
    )


if __name__ == "__main__": main()
