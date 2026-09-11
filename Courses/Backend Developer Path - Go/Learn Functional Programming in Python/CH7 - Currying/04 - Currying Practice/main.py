from collections.abc import Callable

MD_URL_Curry = Callable[[str], Callable[[str | None], str]]

def create_markdown_image(alt_text: str) -> MD_URL_Curry:
    alt_text = '![' + alt_text + ']'

    def with_url(url: str) -> Callable[[str | None], str]:
        url = alt_text + '(' + url.replace('(', '%28').replace(')', '%29')

        def with_title(title: str | None = None) -> str:
            return url + ')' if title is None else url + ' "' + title + '")'

        return with_title

    return with_url
