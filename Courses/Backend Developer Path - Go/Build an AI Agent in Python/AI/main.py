#!/usr/bin/env python3

from prompts import SYSTEM_PROMPT
from ai_call_schema import FUNC_SCHEMA, FUNC_MAP, WORK_SUBDIR, is_partial_func

from typing import NamedTuple, Iterable, Sequence, Optional, TypeIs

from os import environ
from argparse import ArgumentParser, Namespace
import json

from dotenv import load_dotenv

from openai import OpenAI, Omit, omit
from openai.types import CompletionUsage
from openai.types.shared import ChatModel

from openai.types.chat import (
    ChatCompletion, ChatCompletionMessage, ChatCompletionToolMessageParam,
    ChatCompletionMessageParam, ChatCompletionToolUnionParam,
    ChatCompletionMessageToolCallUnion, ChatCompletionMessageFunctionToolCall
)

AI_API_KEY_NAME = "OPENROUTER_API_KEY"
AI_MODEL = "openrouter/free"
AI_URL = "https://OpenRouter.ai/api/v1"

NamedArgs = dict[str, Sequence[str] | str]

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
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    return parser.parse_args( namespace=Cli_Prompt_Args() )


def main():
    if ( args := parse_cli_args() ).verbose:
        print("\nUser prompt:", args.user_prompt, '', sep='\n')

    if not (load_dotenv() and ( api_key := environ.get(AI_API_KEY_NAME) )):
        raise RuntimeError(AI_API_KEY_NAME + ' not found in file ".env"')

    client = OpenAI( base_url=AI_URL, api_key=api_key )

    messages: tuple[ChatCompletionMessageParam, ...] = (
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": args.user_prompt }
    )

    response = ask_ai(client, messages, FUNC_SCHEMA)
    log_ai_response(response, args.verbose)


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


def log_ai_response(
    response: ChatCompletion,
    verbose=True
) -> Optional[list[ChatCompletionToolMessageParam]]:
    print("Model used:", response.model, '\n')

    message, usage = get_message_and_usage_from_ai_response(response)
 
    if verbose:
        print("Prompt tokens:", usage.prompt_tokens)
        print("Response tokens:", usage.completion_tokens, '\n')

    if not message.tool_calls:
        return print("Response:", message.content, sep='\n')

    replies: list[ChatCompletionToolMessageParam] = []

    for call in get_func_args_from_tool_calls(message.tool_calls):
        print(" - Calling function: " + call.func_name, end='')
        print(verbose and f"({call.named_args})" or "")

        replies.append(reply := call_function(call))
        if verbose: print(f"\n-> {reply['content']}")

    return replies


def get_message_and_usage_from_ai_response(
    response: ChatCompletion
) -> tuple[ChatCompletionMessage, CompletionUsage]:
    if not response.usage: raise RuntimeError("Failed AI request!")
    return response.choices[0].message, response.usage


def get_func_args_from_tool_calls(
    tool_calls: Iterable[ChatCompletionMessageToolCallUnion]
) -> tuple[FuncNamedArgs, ...]:
    # return tuple(map(mapped_func_args, filter(is_func_predicate, tool_calls)))

    return tuple(
        mapped_func_args(tool_call)
        for tool_call in tool_calls
        if is_func_tool(tool_call)
    )


def is_func_tool(
    tool_call: ChatCompletionMessageToolCallUnion
) -> TypeIs[ChatCompletionMessageFunctionToolCall]:
    return tool_call.type == "function"


def mapped_func_args(
    func_call: ChatCompletionMessageFunctionToolCall
) -> FuncNamedArgs:
    func = func_call.function
    return FuncNamedArgs(
        func_call.id,
        func.name,
        json.loads(func.arguments or "{}")
    )


def call_function(
    call: FuncNamedArgs, verbose=True
) -> ChatCompletionToolMessageParam:

    if (name := call.func_name) not in FUNC_MAP:
        result = "Error: Unknown function: " + name

    else:
        func = FUNC_MAP[name]
        args = call.named_args

        result = func(**args) if is_partial_func(
            func) else func(WORK_SUBDIR, **args)

        if not result: raise Exception("No content returned by function" + name)

    return { "role": "tool", "tool_call_id": call.call_id, "content": result }


if __name__ == "__main__": main()
