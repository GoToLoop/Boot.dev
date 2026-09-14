from collections.abc import Callable

def markdown_to_text_decorator(func: Callable[..., str]):
    def wrapper(*args: str, **kwargs: str) -> str:
        clean_args = map(convert_md_to_txt, args)
        clean_kwargs = { k: convert_md_to_txt(v) for k, v in kwargs.items() }
        return func(*clean_args, **clean_kwargs)
    return wrapper


# Don't touch below this line

def convert_md_to_txt(doc: str) -> str:
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
