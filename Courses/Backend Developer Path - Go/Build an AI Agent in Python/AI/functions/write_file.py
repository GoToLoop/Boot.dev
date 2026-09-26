from os import makedirs
from os.path import abspath, commonpath, normpath, join, isdir, dirname

def write_file(working_directory: str, rel_file_path: str, content: str) -> str:
    if not isdir(wd := abspath(working_directory)):
        return 'Error: "' + working_directory + '" is not a directory'

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
