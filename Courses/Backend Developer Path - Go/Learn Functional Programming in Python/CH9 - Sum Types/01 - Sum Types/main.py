class MaybeParsed:
    pass


# Don't touch above this line

class Parsed(MaybeParsed):
    def __init__(self, doc_name: str, text: str) -> None:
        self.doc_name: str = doc_name; self.text: str = text


class ParseError(MaybeParsed):
    def __init__(self, doc_name: str, err: str) -> None:
        self.doc_name: str = doc_name; self.err: str = err
