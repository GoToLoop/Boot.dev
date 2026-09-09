#!/usr/bin/env -S python3 -m pytest

import copy

import pytest
from main import Styles, css_styles

StyleUpdate = tuple[str, str, str]

run_cases = [
    (
        {
            "h1": {
                "color": "yellow",
            },
            "body": {
                "background-color": "black",
                "color": "white",
            },
        },
        [
            ("h1", "color", "#CC00FF"),
            ("body", "background-color", "#696969"),
        ],
        {
            "h1": {
                "color": "#CC00FF",
            },
            "body": {
                "background-color": "#696969",
                "color": "white",
            },
        },
    )
]

submit_cases = [
    pytest.param(
        {},
        [
            ("p", "font-size", "16px"),
        ],
        {
            "p": {
                "font-size": "16px",
            },
        },
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {
            ".container": {
                "max-width": "1200px",
                "margin": "0 auto",
                "padding": "0 20px",
            },
        },
        [
            (".container", "max-width", "1450px"),
            (".container", "color", "#660099"),
        ],
        {
            ".container": {
                "max-width": "1450px",
                "margin": "0 auto",
                "padding": "0 20px",
                "color": "#660099",
            },
        },
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("initial_styles", "new_styles", "expected"), run_cases + submit_cases
)
def test_css_styles(
    initial_styles: Styles, new_styles: list[StyleUpdate], expected: Styles
) -> None:
    print("\n---------------------------------")
    print(f"Initial styles: {initial_styles}")
    initial_styles_copy = copy.deepcopy(initial_styles)
    add_style = css_styles(initial_styles)
    result = initial_styles.copy()
    for style in new_styles:
        print(f"Style to add: {style}")
        result = add_style(*style)
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")
    assert initial_styles_copy == initial_styles, (
        "You should not modify the initial styles"
    )
    assert result == expected, "Unexpected result"
