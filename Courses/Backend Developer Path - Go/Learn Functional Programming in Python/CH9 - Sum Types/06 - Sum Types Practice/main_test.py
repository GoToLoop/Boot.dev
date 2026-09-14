#!/usr/bin/env -S python3 -m pytest

# pyright: reportAny = hint
# pyright: reportExplicitAny = hint
# pyright: reportUnknownArgumentType = hint
# pyright: reportUnknownVariableType = hint

from typing import Any

import pytest
from main import CSVExportStatus, CSVStatusResult, get_csv_status

run_cases = [
    (
        CSVExportStatus.PENDING,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Pending...",
            [
                ["Customer ID", "Billed", "Paid"],
                ["1", "100", "100"],
                ["2", "400", "99"],
                ["3", "50", "25"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Customer ID", "Billed", "Paid"],
            ["1", "100", "100"],
            ["2", "400", "99"],
            ["3", "50", "25"],
        ],
        (
            "Processing...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        (
            "Success!",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Unknown error, retrying...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
]

submit_cases = [
    pytest.param(
        CSVExportStatus.PENDING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Pending...",
            [
                ["Card Name", "Condition", "Value"],
                ["Sparky Mouse", "Fair", "100"],
                ["Moist Turtle", "Good", "200"],
                ["Burning Lizard", "Very Good", "1000"],
                ["Mossy Frog", "Poor", "10"],
            ],
        ),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        CSVExportStatus.PROCESSING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", "100"],
            ["Moist Turtle", "Good", "200"],
            ["Burning Lizard", "Very Good", "1000"],
            ["Mossy Frog", "Poor", "10"],
        ],
        (
            "Processing...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        CSVExportStatus.SUCCESS,
        "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        (
            "Success!",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        CSVExportStatus.FAILURE,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Unknown error, retrying...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        1,
        None,
        ("Exception Raised:", "unknown export status"),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("status", "data", "expected"), run_cases + submit_cases)
def test_get_csv_status(status: Any, data: Any, expected: CSVStatusResult) -> None:
    print("\n---------------------------------")
    print(f"Checking: {status}")
    print("Expected:")
    print(expected[0])
    print(expected[1])
    try:
        result = get_csv_status(status, data)
    except Exception as error:
        result = expected[0], str(error)
    print("Actual:")
    print(result[0])
    print(result[1])
    assert result == expected
