from collections.abc import Callable, Iterable

def file_type_getter(
    file_extension_tuples: Iterable[tuple[str, Iterable[str]]],
) -> Callable[[str], str]:
    return lambda file_extension: {
        file_ext: file_type
        for file_type, exts in file_extension_tuples
        for file_ext in exts
    }.get(file_extension, "Unknown")
