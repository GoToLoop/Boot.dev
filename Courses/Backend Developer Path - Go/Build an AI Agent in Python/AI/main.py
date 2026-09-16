#!/usr/bin/env python3

from os import environ
from dotenv import load_dotenv
from openai import OpenAI

PROMPT = "Why is Boot.dev such a great place to learn " +\
         "backend development? Use one paragraph maximum."

def main():
    if not (load_dotenv() and (api_key := environ.get("OPENROUTER_API_KEY"))):
        raise RuntimeError('OPENROUTER_API_KEY not found in file ".env"')

    client = OpenAI(
        base_url="https://OpenRouter.ai/api/v1",
        api_key=api_key,
    )

    print("User prompt:")
    print(PROMPT, '\n')

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": PROMPT,
            }
        ],
    )

    if not (usage := response.usage): raise RuntimeError("Failed AI request!")

    print("Model used:", response.model, '\n')
    print("Prompt tokens:", usage.prompt_tokens)
    print("Response tokens:", usage.completion_tokens, '\n')

    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__": main()
