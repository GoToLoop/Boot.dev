def add_format(default_formats: dict[str, bool], new_format: str
) -> dict[str, bool]: 
    ( formats := default_formats.copy() )[new_format] = True; return formats


def remove_format(default_formats: dict[str, bool], old_format: str
) -> dict[str, bool]:
    ( formats := default_formats.copy() )[old_format] = False; return formats
