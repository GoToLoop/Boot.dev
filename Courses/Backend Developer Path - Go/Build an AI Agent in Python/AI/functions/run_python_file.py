from os.path import abspath, commonpath, normpath, join, isdir, isfile
from subprocess import run, CompletedProcess, TimeoutExpired

from collections.abc import Sequence
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING: from openai.types.chat import ChatCompletionFunctionToolParam

PYTHON = "python3" # executable
TIMEOUT = 30 # seconds

def run_python_file(
    working_directory: str, file_path: str, args: Optional[Sequence[str]] = None
) -> str:
    if not isdir(wd := abspath(working_directory)):
        return 'Error: "' + working_directory + '" is not a directory'

    if not isfile(target_file := normpath(join(wd, file_path))): return\
        'Error: "' + file_path + '" does not exist or is not a regular file'

    if not target_file.endswith(".py"):
        return 'Error: "' + file_path + '" is not a Python file'

    if not target_file.startswith(wd) or commonpath((wd, target_file)) != wd:
        return 'Error: Cannot execute "' + file_path\
            + '" as it is outside the permitted working directory'

    args = args or ()
    command = PYTHON, target_file, *args
    try: process = _call_python_script(command, wd)

    except TimeoutExpired:
        return f"Error: Python script {file_path} timed out after {TIMEOUT}s"

    except OSError as e:
        return f"Error: Executing Python process w/ args {command}...\n{e}"

    return _build_python_process_report(process)


def _call_python_script(
    py_args: Sequence[str], work_dir: str
) -> CompletedProcess[str]:
    return run(
        py_args,
        cwd=work_dir,
        capture_output=True,
        text=True,
        timeout=TIMEOUT
    )


def _build_python_process_report(process: CompletedProcess[str]) -> str:
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


schema_run_python_file: "ChatCompletionFunctionToolParam" = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": (
            "Executes a specified Python (.py) file within the working "
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
                        "The relative path to the Python file (.py) to execute,"
                        " starting from the `working_directory`."
                    )
                },
                "args": {
                    "type": "array",
                    "items": { "type": "string" },
                    "minItems": 0,
                    "description": (
                        "A sequence container representing the command-line's "
                        "variadic arguments to be passed to the Python script "
                        "`file_path`."
                    )
                }
            }
        }
    }
}
