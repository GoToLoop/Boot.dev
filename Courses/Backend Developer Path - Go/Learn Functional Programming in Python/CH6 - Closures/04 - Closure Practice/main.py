import copy
from collections.abc import Callable

Styles = dict[str, dict[str, str]]

# Don't touch above this line

def css_styles(initial_styles: Styles) -> Callable[[str, str, str], Styles]:
    styles = copy.deepcopy(initial_styles)

    def add_style(selector: str, property: str, value: str) -> Styles:
        try: styles[selector][property] = value
        except KeyError: styles[selector] = { property: value }
        return styles

    return add_style
