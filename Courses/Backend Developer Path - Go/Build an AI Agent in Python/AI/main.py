#!/usr/bin/env python3

from prompts import SYSTEM_PROMPT
from ai_call_schema import FUNCTION_SCHEMA

from typing import Iterable, Optional

from os import environ
from argparse import ArgumentParser, Namespace
import json

from dotenv import load_dotenv

from openai import OpenAI, Omit, omit
from openai.types.shared import ChatModel

from openai.types.chat import (
    ChatCompletion, ChatCompletionMessageParam, ChatCompletionToolUnionParam
)

AI_API_KEY_NAME = "OPENROUTER_API_KEY"
AI_MODEL = "openrouter/free"
AI_URL = "https://OpenRouter.ai/api/v1"

class CLI_Prompt_Args(Namespace): user_prompt: str; verbose: bool

def parse_cli_args() -> CLI_Prompt_Args:
    parser = ArgumentParser(description="AI Code Assistant Agent")

    parser.add_argument("user_prompt", type=str, help="AI prompt")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    return parser.parse_args( namespace=CLI_Prompt_Args() )


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

    response = ask_ai(client, messages, FUNCTION_SCHEMA)
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


def log_ai_response(response: ChatCompletion, verbose=True):
    print("Model used:", response.model, '\n')

    if not (usage := response.usage): raise RuntimeError("Failed AI request!")

    if verbose:
        print("Prompt tokens:", usage.prompt_tokens)
        print("Response tokens:", usage.completion_tokens, '\n')

    message = response.choices[0].message

    if message.tool_calls:
        for call in message.tool_calls:
            if call.type == "function":
                func_name = call.function.name
                func_args = json.loads(call.function.arguments or "{}")
                print("Function to call:", f"{func_name}({func_args})")

    else: print("Response:", message.content, sep='\n')


if __name__ == "__main__": main()
