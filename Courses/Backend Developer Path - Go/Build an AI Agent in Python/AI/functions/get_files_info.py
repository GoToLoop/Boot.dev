from os import PathLike, path, scandir

DESCRIPTION = "- %s: file_size=%d bytes, is_dir=%s"

def get_files_info(working_directory: str, relative_dir: str = '.') -> str:
    if not path.isdir(wd := path.abspath(working_directory)):
        return 'Error: "' + working_directory + '" is not a directory'

    if not path.isdir(target_dir := path.normpath(path.join(wd, relative_dir))):
        return 'Error: "' + relative_dir + '" is not a directory'

    if not target_dir.startswith(wd) or path.commonpath((wd, target_dir)) != wd:
        return 'Error: Cannot list "' + relative_dir\
            + '" as it is outside the permitted working directory'

    try: return _get_dir_files_description(target_dir)
    except OSError as e: return f"Error: Scanning files...\n{e}"


def _get_dir_files_description(folder: PathLike[str] | str) -> str:
    with scandir(folder) as entries: return '\n'.join(
        DESCRIPTION % (entry.name, entry.stat().st_size, entry.is_dir())
        for entry in entries
    )
