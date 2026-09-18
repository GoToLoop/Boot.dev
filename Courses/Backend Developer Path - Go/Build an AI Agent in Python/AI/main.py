#!/usr/bin/env python3

from typing import Protocol

from os import environ
from argparse import ArgumentParser

from dotenv import load_dotenv
from openai import OpenAI

class ChatNamespace(Protocol): user_prompt: str

def main():
    if not (load_dotenv() and (api_key := environ.get("OPENROUTER_API_KEY"))):
        raise RuntimeError('OPENROUTER_API_KEY not found in file ".env"')

    client = OpenAI(
        base_url="https://OpenRouter.ai/api/v1",
        api_key=api_key,
    )

    parser = ArgumentParser(description="AI Code Assistant Agent")
    parser.add_argument("user_prompt", type=str, help="AI prompt")
    args = parser.parse_args(namespace=ChatNamespace)

    print("\nUser prompt:")
    print(args.user_prompt, '\n')

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=({ "role": "user", "content": args.user_prompt },)
    )

    if not (usage := response.usage): raise RuntimeError("Failed AI request!")

    print("Model used:", response.model, '\n')
    print("Prompt tokens:", usage.prompt_tokens)
    print("Response tokens:", usage.completion_tokens, '\n')

    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__": main()
