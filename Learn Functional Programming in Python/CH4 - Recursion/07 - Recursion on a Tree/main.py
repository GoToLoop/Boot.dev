type FileTree = dict[str, FileTree | None]
"""A recursive mapping representing a file-system tree.

Each key is either a subfolder name or a filename. If the corresponding value
is another ``FileTree``, the key denotes a subfolder containing further entries.
If the value is ``None``, the key denotes a filename (leaf node).
"""

def list_files(filename_paths: FileTree, current_path: str = "") -> list[str]:
    filepaths: list[str] = [] # list of filename paths

    for folder_or_file, file_tree in filename_paths.items():
        new_path = current_path + '/' + folder_or_file # new current path so far
        if file_tree is None: filepaths.append(new_path) # file path complete
        else: filepaths += list_files(file_tree, new_path) # recursion

    return filepaths
