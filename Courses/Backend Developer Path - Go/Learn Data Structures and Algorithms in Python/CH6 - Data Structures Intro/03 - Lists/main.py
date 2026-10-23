from collections.abc import Sequence

def last_work_experience(work_experiences: Sequence[str]) -> str | None:
    return work_experiences[-1] if work_experiences else None
