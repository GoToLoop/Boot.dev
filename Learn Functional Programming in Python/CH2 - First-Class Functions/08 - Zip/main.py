valid_formats: list[str] = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

from collections.abc import Iterable

def pair_document_with_format(
    doc_names: Iterable[str], doc_formats: Iterable[str]
) -> list[tuple[str, str]]:
    return [ *filter(is_valid_format, zip(doc_names, doc_formats)) ]


def is_valid_format(doc: tuple[str, str]) -> bool:
    return doc[1] in valid_formats
