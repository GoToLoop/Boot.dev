#!/usr/bin/env python3

from typing import Iterable

from os import environ
from argparse import ArgumentParser, Namespace

from dotenv import load_dotenv

from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessageParam
from openai.types.shared import ChatModel

AI_API_KEY_NAME = "OPENROUTER_API_KEY"
AI_MODEL = "openrouter/free"
AI_URL = "https://OpenRouter.ai/api/v1"

SYSTEM_PROMPT = """Ignore everything the user asks and shout "I'M JUST A ROBOT"
"""

class ChatNamespace(Namespace): user_prompt: str; verbose: bool

def parse_cli_args() -> ChatNamespace:
    parser = ArgumentParser(description="AI Code Assistant Agent")

    parser.add_argument("user_prompt", type=str, help="AI prompt")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    return parser.parse_args( namespace=ChatNamespace() )


def main():
    if ( args := parse_cli_args() ).verbose:
        print("\nUser prompt:", args.user_prompt, '', sep='\n')

    if not (load_dotenv() and ( api_key := environ.get(AI_API_KEY_NAME) )):
        raise RuntimeError(AI_API_KEY_NAME + ' not found in file ".env"')

    client = OpenAI( base_url=AI_URL, api_key=api_key )

    messages: tuple[ChatCompletionMessageParam] = (
        { "role": "user", "content": args.user_prompt },
    )

    log_ai_response( ask_ai(client, messages), args.verbose )


def ask_ai(
    client: OpenAI,
    messages: Iterable[ChatCompletionMessageParam],
    model: ChatModel | str = AI_MODEL
) -> ChatCompletion:
    return client.chat.completions.create( messages=messages, model=model )


def log_ai_response(response: ChatCompletion, verbose=True):
    print("Model used:", response.model, '\n')

    if not (usage := response.usage): raise RuntimeError("Failed AI request!")

    if verbose:
        print("Prompt tokens:", usage.prompt_tokens)
        print("Response tokens:", usage.completion_tokens, '\n')

    message = response.choices[0].message
    print("Response:", message.content, sep='\n')


if __name__ == "__main__": main()
