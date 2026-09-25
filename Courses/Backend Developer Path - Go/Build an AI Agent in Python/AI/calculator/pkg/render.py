from json import dumps

def format_json_output(exp: str, result: float, indent: int | str = 2) -> str:
    if isinstance(result, float) and result.is_integer(): result = int(result)
    return dumps({ "expression": exp, "result": result }, indent=indent)
