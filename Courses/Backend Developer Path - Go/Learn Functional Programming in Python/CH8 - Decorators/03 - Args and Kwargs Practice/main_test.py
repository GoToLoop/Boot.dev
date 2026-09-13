#!/usr/bin/env -S python3 -m pytest

from collections.abc import Callable

import pytest
from decorators import PluginConfig
from plugins import configure_backups, configure_login

PluginArg = tuple[str, str]
PluginFunc = Callable[..., PluginConfig]

run_cases = [
    (
        "configure_backups",
        configure_backups,
        [
            ("path", "~/documents"),
            ("extension", ".md"),
        ],
        {
            "path": "~/documents",
            "prefix": "copy_",
            "extension": ".md",
        },
    ),
    (
        "configure_login",
        configure_login,
        [
            ("user", "goku_fanatic"),
            ("password", "kakarot1989"),
        ],
        {
            "user": "goku_fanatic",
            "password": "kakarot1989",
            "token": None,
        },
    ),
]

submit_cases = [
    pytest.param(
        "configure_backups",
        configure_backups,
        [
            ("path", "~/workspace/backups"),
            ("prefix", "backup_"),
        ],
        {
            "path": "~/workspace/backups",
            "prefix": "backup_",
            "extension": ".txt",
        },
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "configure_login",
        configure_login,
        [
            ("user", "john_q_sample"),
            ("password", "p@$$w0rd"),
            ("token", "a09adc-0914sf-012la9-fa3sa0-2342ra"),
        ],
        {
            "user": "john_q_sample",
            "password": "p@$$w0rd",
            "token": "a09adc-0914sf-012la9-fa3sa0-2342ra",
        },
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("func_name", "func", "args", "expected"), run_cases + submit_cases
)
def test_configure_plugin(
    func_name: str,
    func: PluginFunc,
    args: list[PluginArg],
    expected: PluginConfig,
) -> None:
    print("\n---------------------------------")
    print(f"Function: {func_name}")
    print("Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print("Expected:")
    print(expected)
    result = func(*args)
    print("Actual:")
    print(result)
    assert result == expected
