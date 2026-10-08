from functions.partial import *
from collections.abc import Callable

FUNC_SCHEMA = (
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
    schema_run_shebang_script
)

FUNC_MAP: dict[str, Callable[..., str]] = {
    (name := func["function"]["name"]): globals()[name]
    for func in FUNC_SCHEMA
}

FUNC_NAMES = (
    "get_files_info",
    "get_file_content",
    "write_file",
    "run_python_file",
    "run_shebang_script"
)

FUNCTIONS = (
    get_files_info,
    get_file_content,
    write_file,
    run_python_file,
    run_shebang_script
)
