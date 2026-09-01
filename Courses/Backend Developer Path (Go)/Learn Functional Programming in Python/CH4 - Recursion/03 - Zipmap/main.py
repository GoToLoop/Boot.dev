from collections.abc import Sequence

def zipmap(titles: Sequence[str], scores: Sequence[float]) -> dict[str, float]:
    if not (titles and scores): return {}
    ( title_scores := zipmap(titles[1:], scores[1:]) )[ titles[0] ] = scores[0]
    return title_scores
