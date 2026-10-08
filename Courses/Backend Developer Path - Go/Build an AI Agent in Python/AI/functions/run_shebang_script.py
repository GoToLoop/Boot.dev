from os.path import abspath, commonpath, normpath, join, isdir, isfile
from subprocess import run, CompletedProcess, TimeoutExpired

from collections.abc import Sequence
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING: from openai.types.chat import ChatCompletionFunctionToolParam

from functions.get_file_content import read_file_content

TIMEOUT = 30 # seconds

def run_shebang_script(
    work_dir: str, /, file_path: str, args: Optional[Sequence[str]] = None
) -> str:
    if not isdir(wd := abspath(work_dir)):
        return 'Error: "' + work_dir + '" is not a directory'

    if not isfile(target_file := normpath(join(wd, file_path))): return\
        'Error: "' + file_path + '" does not exist or is not a regular file'

    if not target_file.startswith(wd) or commonpath((wd, target_file)) != wd:
        return 'Error: Cannot execute "' + file_path\
            + '" as it is outside the permitted working directory'

    try: shebang_mark = read_file_content(target_file, file_path, 2)
    except OSError as e: return f'Error: Reading file "{file_path}"...\n{e}'

    if not shebang_mark.startswith("#!"):
        return 'Error: "' + file_path + '" is not a shebang script file'

    args = args or ()
    command = target_file, *args
    try: process = _call_shebang_script(command, wd)

    except TimeoutExpired:
        return f"Error: shebang script {file_path} timed out after {TIMEOUT}s"

    except OSError as e:
        return f"Error: Executing shebang process w/ args {command}...\n{e}"

    return _build_shebang_process_report(process)


def _call_shebang_script(
    py_args: Sequence[str], work_dir: str, timeout: float = TIMEOUT
) -> CompletedProcess[str]:
    return run(
        py_args,
        cwd=work_dir,
        capture_output=True,
        text=True,
        timeout=timeout
    )


def _build_shebang_process_report(process: CompletedProcess[str]) -> str:
    reports: list[str] = []

    if code := process.returncode:
        reports.append(f"Process exited with code {code}")

    stdout = process.stdout.strip()
    stderr = process.stderr.strip()

    if not (stdout or stderr): reports.append("No output produced")
    else:
        if stdout: reports.append("STDOUT:\n" + stdout)
        if stderr: reports.append("STDERR:\n" + stderr)

    return '\n'.join(reports)


schema_run_shebang_script: "ChatCompletionFunctionToolParam" = {
    "type": "function",
    "function": {
        "name": "run_shebang_script",
        "description": (
            "Executes a specified shebang script within the working "
            "directory with optional command-line arguments and returns its "
            "both outputs as 1 joined string. It also enforces a "
            f"{TIMEOUT}-second execution timeout."
        ),
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": (
                        "The relative path to the shebang script to execute, "
                        "starting from the working directory."
                    )
                },
                "args": {
                    "type": "array",
                    "items": { "type": "string" },
                    "minItems": 0,
                    "description": (
                        "A sequence container representing any optional "
                        "command-line's variadic arguments to be passed to the "
                        "shebang script `file_path`."
                    )
                }
            }
        }
    }
}
