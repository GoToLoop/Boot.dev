from collections.abc import Iterable

def count_marketers(job_titles: Iterable[str]) -> int:
    # return sum( 1 for job in map(str.lower, job_titles) if job == "marketer" )
    # return sum( job == "marketer" for job in map(str.lower, job_titles) )
    return list( map(str.lower, job_titles) ).count("marketer")
