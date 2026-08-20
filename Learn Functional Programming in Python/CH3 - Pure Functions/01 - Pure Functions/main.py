def convert_file_format(filename: str, target_format: str) -> str | None:
    valid_extensions = "docx", "pdf", "txt", "pptx", "ppt", "md"

    valid_conversions: dict[str, tuple[str, ...]] = {
        "docx": ("pdf", "txt", "md"),
        "pdf": ("docx", "txt", "md"),
        "txt": ("docx", "pdf", "md"),
        "pptx": ("ppt", "pdf"),
        "ppt": ("pptx", "pdf"),
        "md": ("docx", "pdf", "txt"),
    }

    if (
        ( current_format := filename.split('.')[-1] ) in valid_extensions
        and target_format in valid_conversions[current_format]
    ): return filename.replace(current_format, target_format)
