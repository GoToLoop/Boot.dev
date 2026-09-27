from os.path import abspath, commonpath, normpath, join, isdir, isfile
from typing import TYPE_CHECKING

if TYPE_CHECKING: from openai.types.chat import ChatCompletionFunctionToolParam

MAX_CHARS = 10_000
TRUNCATED = f'[...File "%s" truncated at {MAX_CHARS} characters]'

def get_file_content(working_directory: str, rel_file_path: str) -> str:
    if not isdir(wd := abspath(working_directory)):
        return 'Error: "' + working_directory + '" is not a directory'

    if not isfile(target_file := normpath(join(wd, rel_file_path))): return\
        f'Error: File not found or is not a regular file: "{rel_file_path}"'

    if not target_file.startswith(wd) or commonpath((wd, target_file)) != wd:
        return 'Error: Cannot read "' + rel_file_path\
            + '" as it is outside the permitted working directory'

    try: return _read_file_content(target_file, rel_file_path)
    except OSError as e: return f'Error: Reading file "{rel_file_path}"...\n{e}'


def _read_file_content(absolute_file_path: str, relative_file_path='') -> str:
    with open(absolute_file_path) as f:
        if len(content := f.read(MAX_CHARS + 1)) > MAX_CHARS: 
            content = content[:MAX_CHARS] + TRUNCATED % (
                relative_file_path or absolute_file_path
            )
    return content


schema_get_file_content: "ChatCompletionFunctionToolParam" = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": (
            "Reads and returns the content of a specified file relative to the "
            "working directory. Automatically truncates files larger than "
            f"{MAX_CHARS:,} characters."
        ),
        "parameters": {
            "type": "object",
            "required": ["rel_file_path"],
            "properties": {
                "rel_file_path": {
                    "type": "string",
                    "description": (
                        "The relative path to the file you want to read, "
                        "starting from the working directory."
                    )
                }
            }
        }
    }
}
