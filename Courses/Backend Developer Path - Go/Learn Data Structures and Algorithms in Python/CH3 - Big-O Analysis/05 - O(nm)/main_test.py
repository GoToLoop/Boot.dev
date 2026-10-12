#!/usr/bin/env -S python3 -m pytest

import random

import pytest
from main import get_avg_brand_followers

run_cases = [
    pytest.param(10, 1000, "luxa", 383.9),
    pytest.param(20, 2000, "luxa", 593.25),
    pytest.param(30, 3000, "luxa", 932.23),
]

submit_cases = [
    pytest.param(40, 4000, "luxa", 1495.4, marks=pytest.mark.submit),
    pytest.param(80, 8000, "luxa", 2608.95, marks=pytest.mark.submit),
    pytest.param(160, 16000, "luxa", 5920.98, marks=pytest.mark.submit),
]


@pytest.fixture(scope="module", autouse=True)
def seed_random():
    random.seed(1)


@pytest.mark.parametrize(
    ("num_handles", "avg_aud_size", "brand_name", "expected_output"),
    run_cases + submit_cases,
)
def test_get_avg_brand_followers(
    num_handles, avg_aud_size, brand_name, expected_output
):
    print("\n---------------------------------")
    print(
        f"Checking {num_handles} influencers with average audience sizes of",
        f"{avg_aud_size}..."
    )
    print(f" * brand_name: {brand_name}")
    print(f"Expected: {expected_output}")
    all_handles = get_all_handles(num_handles, avg_aud_size)
    avg = round(get_avg_brand_followers(all_handles, brand_name), 2)
    print(f"Actual:   {avg}")
    assert avg == expected_output


def get_all_handles(num, audience_size):
    all_handles = []
    for _ in range(num):
        m = random.randrange(
            int(audience_size - audience_size * 1.2),
            int(audience_size + audience_size * 1.2),
        )
        handles = get_user_handles(m)
        all_handles.append(handles)
    return all_handles


def get_user_handles(num):
    handles = []
    for i in range(num):
        m = random.randrange(0, 6)
        if m == 0:
            handles.append(f"luxaraygirl{i}")
        elif m == 1:
            handles.append(f"theprimerog{i}")
        elif m == 2:
            handles.append(f"luxafanboi{i}")
        elif m == 3:
            handles.append(f"dashlord{i}")
        elif m == 4:
            handles.append(f"saintrex{i}")
        elif m == 5:
            handles.append(f"writergurl{i}")
    return handles
