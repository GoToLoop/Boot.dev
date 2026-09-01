def choose_parser(file_ext: str) -> str:
    return "markdown" if file_ext.lower() in ("markdown", "md") else "plaintext"
