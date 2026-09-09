from collections.abc import Callable, Collection

def doc_format_checker_and_converter(
    converter: Callable[[str], str], valid_formats: Collection[str]
) -> Callable[[str, str], str]:
    def formatter(filename: str, content: str) -> str:
        if filename.split('.')[-1] in valid_formats: return converter(content)
        raise ValueError("invalid file format")
    return formatter

# Don't edit below this line

def capitalize_content(content: str) -> str: return content.upper()
def reverse_content(content: str) -> str: return content[::-1]
