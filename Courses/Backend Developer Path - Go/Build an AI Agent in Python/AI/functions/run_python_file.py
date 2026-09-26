from os.path import abspath, commonpath, normpath, join, isdir, isfile
from subprocess import run, CompletedProcess, TimeoutExpired
from collections.abc import Sequence

PYTHON = "python3" # executable
TIMEOUT = 30 # seconds

def run_python_file(working_directory: str, file_path: str, *args: str) -> str:
    if not isdir(wd := abspath(working_directory)):
        return 'Error: "' + working_directory + '" is not a directory'

    if not isfile(target_file := normpath(join(wd, file_path))): return\
        'Error: "' + file_path + '" does not exist or is not a regular file'

    if not target_file.endswith(".py"):
        return 'Error: "' + file_path + '" is not a Python file'

    if not target_file.startswith(wd) or commonpath((wd, target_file)) != wd:
        return 'Error: Cannot execute "' + file_path\
            + '" as it is outside the permitted working directory'

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
