def remove_invalid_lines(document: str) -> str:
    return '\n'.join( filter(not_hyphen_predicate, document.split('\n')) )

def not_hyphen_predicate(line: str) -> bool: return not line.startswith('-')
