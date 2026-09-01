from collections.abc import Callable

def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str: return "```\n" + to_string(file) + "\n```"
