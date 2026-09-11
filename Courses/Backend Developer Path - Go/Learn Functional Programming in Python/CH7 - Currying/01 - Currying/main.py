from collections.abc import Callable

def converted_font_size(font_size: int) -> Callable[[str], int]:
    def by_doc_type(doc_type: str) -> int:
        match doc_type:
            case "txt": return font_size
            case "md": return font_size << 1
            case "docx": return font_size * 3
            case _: raise ValueError("invalid doc type")
    return by_doc_type
