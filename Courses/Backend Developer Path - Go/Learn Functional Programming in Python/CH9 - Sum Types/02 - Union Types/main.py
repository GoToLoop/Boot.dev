class Parsed:
    def __init__(self, doc_name: str, text: str) -> None:
        self.doc_name: str = doc_name
        self.text: str = text


class ParseError:
    def __init__(self, doc_name: str, err: str) -> None:
        self.doc_name: str = doc_name
        self.err: str = err


# Don't touch above this line

def parse_document(doc_name: str, content: str) -> Parsed | ParseError:
    return content and Parsed(doc_name, content)\
                   or  ParseError(doc_name, "no content")


def display_parse_result(result: Parsed | ParseError) -> str:
    doc_name = result.doc_name

    return f"Parsed {doc_name}: {len(result.text)} characters" if isinstance(
        result, Parsed) else f"Failed {doc_name}: {result.err}"
