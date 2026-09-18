#!/usr/bin/env python3

from typing import Iterable

from os import environ
from argparse import ArgumentParser, Namespace

from dotenv import load_dotenv

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam
from openai.types.shared import ChatModel

class ChatNamespace(Namespace):
    user_prompt: str
    verbose: bool


def ask_ai(
    client: OpenAI,
    messages: Iterable[ChatCompletionMessageParam],
    model: ChatModel | str = "openrouter/free"
) -> ChatCompletion:
    return client.chat.completions.create(messages=messages, model=model)


def log_ai_response(response: ChatCompletion, verbose=True):
    if not (usage := response.usage): raise RuntimeError("Failed AI request!")

    print("Model used:", response.model, '\n')

    if verbose:
        print("Prompt tokens:", usage.prompt_tokens)
        print("Response tokens:", usage.completion_tokens, '\n')

    print("Response:")
    print(response.choices[0].message.content)


def main():
    if not (load_dotenv() and (api_key := environ.get("OPENROUTER_API_KEY"))):
        raise RuntimeError('OPENROUTER_API_KEY not found in file ".env"')

    client = OpenAI(
        base_url="https://OpenRouter.ai/api/v1",
        api_key=api_key
    )

    parser = ArgumentParser(description="AI Code Assistant Agent")
    parser.add_argument("user_prompt", type=str, help="AI prompt")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args(namespace=ChatNamespace)

    if args.verbose:
        print("\nUser prompt:")
        print(args.user_prompt, '\n')

    messages: list[ChatCompletionMessageParam] = [
        { "role": "user", "content": args.user_prompt }
    ]

    log_ai_response( ask_ai(client, messages), args.verbose )


if __name__ == "__main__": main()
