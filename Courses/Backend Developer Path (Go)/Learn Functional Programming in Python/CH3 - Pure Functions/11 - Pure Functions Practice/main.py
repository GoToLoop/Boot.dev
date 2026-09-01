from collections.abc import Iterable

def sort_dates(dates: Iterable[str]) -> list[str]:
    return sorted(dates, key=format_date)


def format_date(date: str) -> str: # "MM-DD-YYYY" -> "YYYYMMDD"
    m, d, y = date.split('-')
    return y + m + d
