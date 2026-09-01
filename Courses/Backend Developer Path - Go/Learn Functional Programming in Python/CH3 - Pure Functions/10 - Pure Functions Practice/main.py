from collections.abc import Callable

default_commands: dict[str, Callable[..., object]] = {}
default_formats: list[str] = ["txt", "md", "html"]
saved_documents: dict[str, str] = {}

# Don't edit above this line

def add_custom_command(
    commands: dict[str, Callable[..., object]],
    new_command: str,
    function: Callable[..., object],
) -> dict[str, Callable[..., object]]:
    (commands := commands.copy())[new_command] = function
    return commands


from collections.abc import Iterable

def add_format(formats: Iterable[str], format: str) -> list[str]:
    return [*formats, format]


def save_document(docs: dict[str, str], file: str, doc: str) -> dict[str, str]:
    (docs := docs.copy())[file] = doc
    return docs


def add_line_break(line: str) -> str: return line + "\n\n"
