from os import makedirs
from os.path import abspath, commonpath, normpath, join, isdir, dirname
from typing import TYPE_CHECKING

if TYPE_CHECKING: from openai.types.chat import ChatCompletionFunctionToolParam

def write_file(work_dir: str, /, rel_file_path: str, content: str) -> str:
    if not isdir(wd := abspath(work_dir)):
        return 'Error: "' + work_dir + '" is not a directory'

    if isdir(target_file := normpath(join(wd, rel_file_path))): return\
        'Error: Cannot write to "' + rel_file_path + '" as it is a directory'

    if not target_file.startswith(wd) or commonpath((wd, target_file)) != wd:
        return 'Error: Cannot write to "' + rel_file_path\
            + '" as it is outside the permitted working directory'

    try:
        makedirs(dirname(target_file), exist_ok=True)

        return 'Successfully wrote to "' + rel_file_path + '" (' + str(
            _write_file_content(target_file, content)) + ' characters written)'

    except OSError as e: return f'Error: Writing file "{rel_file_path}"...\n{e}'


def _write_file_content(absolute_file_path: str, content: str) -> int:
    with open(absolute_file_path, 'w') as f: return f.write(content)


schema_write_file: "ChatCompletionFunctionToolParam" = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": (
            "Creates if missing, then writes text content within the working "
            "directory (overwriting if the file exists). Automatically creates "
            "any missing parent directories too. Also returns a success string "
            "message describing filepath and number of characters written."
        ),
        "parameters": {
            "type": "object",
            "required": ["rel_file_path", "content"],
            "properties": {
                "rel_file_path": {
                    "type": "string",
                    "description": (
                        "The relative path to the file you want to write to, "
                        "starting from the working directory."
                    )
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write into the file."
                }
            }
        }
    }
}
