from functools import partial
from typing import Callable, TypeIs

from ..get_files_info import get_files_info, schema_get_files_info
from ..get_file_content import get_file_content, schema_get_file_content
from ..write_file import write_file, schema_write_file
from ..run_python_file import run_python_file, schema_run_python_file

WORK_DIR = "calculator"

get_files_info = partial(get_files_info, WORK_DIR)
get_file_content = partial(get_file_content, WORK_DIR)
write_file = partial(write_file, WORK_DIR)
run_python_file = partial(run_python_file, WORK_DIR)

def is_partial_func[R](func: Callable[..., R]) -> TypeIs[partial[R]]:
    return isinstance(func, partial)


__all__ = (
    "get_files_info", "schema_get_files_info",
    "get_file_content", "schema_get_file_content",
    "write_file", "schema_write_file",
    "run_python_file", "schema_run_python_file",
    'is_partial_func', 'WORK_DIR'
)
