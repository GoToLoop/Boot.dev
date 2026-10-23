#!/usr/bin/env -S python3 -m pytest

import pytest
from main import matchmake
from user_queue import Queue
from typing import cast

ERR = "No match found"
mark = pytest.mark.submit

run_cases = (
    [ ("Ted", "join"), (["Ted"], ERR) ],
    [ ("Barney", "join"), (["Barney", "Ted"], ERR) ],
    [ ("Marshall", "join"), (["Marshall", "Barney", "Ted"], ERR) ],
    [ ("Lily", "join"), (["Lily", "Marshall"], "Ted matched Barney!") ],
    [ ("Robin", "join"), (["Robin", "Lily", "Marshall"], ERR) ],
    [ ("Carl", "join"), (["Carl", "Robin"], "Marshall matched Lily!") ],
    [ ("Carl", "leave"), (["Robin"], ERR) ],
    [ ("Robin", "leave"), (cast(list[str], []), ERR) ],
)

submit_cases = (
    pytest.param( ("Ranjit", "join"), (["Ranjit"], ERR), marks=mark ),
    pytest.param( ("Ranjit", "leave"), (cast(list[str], []), ERR), marks=mark ),
    pytest.param( ("Victoria", "join"), (["Victoria"], ERR), marks=mark ),
    pytest.param( ("Quinn", "join"), (["Quinn", "Victoria"], ERR), marks=mark ),

    pytest.param(
        ("Zoey", "join"),
        (["Zoey", "Quinn", "Victoria"], ERR),
        marks=mark
    ),

    pytest.param(
        ("Stella", "join"),
        (["Stella", "Zoey"], "Victoria matched Quinn!"),
        marks=mark
    ),
)

queue = Queue()

@pytest.mark.parametrize(("user", "expected_state"), run_cases + submit_cases)
def test_matchmake(
    user: tuple[str, str], expected_state: tuple[list[str], str]
):
    print("\n---------------------------------")
    print(f"Queue: {queue}")

    name, action = user

    if action == "leave": print(f"{name} left the queue.")
    if action == "join": print(f"{name} joined the queue.")

    print(f"Expecting Queue: {expected_state[0]}")
    print(f"Expecting Return: {expected_state[1]}")

    try: result = matchmake(queue, user)
    except Exception as error: result = f"Error: {error}"

    print(f"Actual Queue: {queue}")
    print(f"Actual Return: {result}")

    assert result == expected_state[1]
    assert queue.items == expected_state[0]
