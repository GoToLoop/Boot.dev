#!/usr/bin/env -S python3 -m pytest

import pytest
from main import TextFunc, replacer, tag_pre

run_cases = [
    (
        replacer("faith", "salmon")(lambda x: x),
        'replacer("faith", "salmon")(lambda x: x)',
        "I find your lack of faith disturbing, young Skywalker.",
        "I find your lack of salmon disturbing, young Skywalker.",
    ),
    (
        replacer("paragraph", "span")(replacer("p>", "span>")(lambda x: x)),
        'replacer("paragraph", "span")(replacer("p>", "span>")(lambda x: x))',
        "<p>Here is a paragraph</p>",
        "<span>Here is a span</span>",
    ),
    (
        tag_pre,
        "tag_pre",
        '<a href="https://www.boot.dev/blog/wiki/troubleshoot-code-editor-issues/">link</a>',
        "<pre>&lt;a href=&quot;https://www.boot.dev/blog/wiki/troubleshoot-code-editor-issues/&quot;&gt;link&lt;/a&gt;</pre>",
    ),
]

submit_cases = [
    pytest.param(
        tag_pre,
        "tag_pre",
        '<img src="https://imgur.com/a/VlMAK0B" alt="mystery">',
        "<pre>&lt;img src=&quot;https://imgur.com/a/VlMAK0B&quot; alt=&quot;mystery&quot;&gt;</pre>",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        tag_pre,
        "tag_pre",
        "<p>This paragraph has <em>italic text</em></p>",
        "<pre>&lt;p&gt;This paragraph has &lt;em&gt;italic text&lt;/em&gt;&lt;/p&gt;</pre>",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("func", "func_name", "input_text", "expected"), run_cases + submit_cases
)
def test_text_decorator(
    func: TextFunc, func_name: str, input_text: str, expected: str
) -> None:
    print("\n---------------------------------")
    print(f"Function: {func_name}")
    print(f"    Input: {input_text}")
    print(f"Expected: {expected}")
    result = func(input_text)
    print(f"Actual:   {result}")
    assert result == expected
