from enum import Enum

class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4

# Don't touch above this line

def convert_format(
    content: str, from_format: DocFormat, to_format: DocFormat | None
) -> str:
    match from_format, to_format:
        case DocFormat.MD, DocFormat.HTML: return "<h1>" + content[2:] + "</h1>"
        case DocFormat.TXT, DocFormat.PDF: return "[PDF] " + content + " [PDF]"
        case DocFormat.HTML, DocFormat.MD: return "# " + content[4:-5]
        case _: raise Exception("invalid type")
