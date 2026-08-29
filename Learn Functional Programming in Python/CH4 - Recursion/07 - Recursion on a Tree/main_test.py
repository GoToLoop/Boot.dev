#!/usr/bin/env -S python3 -m pytest

import pytest
from main import list_files

FileTree = dict[str, "FileTree | None"]

run_cases = [
    (
        {
            "Documents": {
                "Proposal.docx": None,
                "Report": {"AnnualReport.pdf": None, "Financials.xlsx": None},
            },
            "Downloads": {"picture1.jpg": None, "picture2.jpg": None},
        },
        [
            "/Documents/Proposal.docx",
            "/Documents/Report/AnnualReport.pdf",
            "/Documents/Report/Financials.xlsx",
            "/Downloads/picture1.jpg",
            "/Downloads/picture2.jpg",
        ],
    )
]

submit_cases = [
    pytest.param({}, [], marks=pytest.mark.submit),
    pytest.param(
        {
            "Work": {
                "ProjectA": {
                    "Documentation": {"README.md": None, "GUIDE.md": None},
                    "Source": {"main.py": None, "util.py": None},
                },
                "ProjectB": {"Presentation.pptx": None},
            }
        },
        [
            "/Work/ProjectA/Documentation/GUIDE.md",
            "/Work/ProjectA/Documentation/README.md",
            "/Work/ProjectA/Source/main.py",
            "/Work/ProjectA/Source/util.py",
            "/Work/ProjectB/Presentation.pptx",
        ],
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {
            "Music": {
                "Pop": {"song1.mp3": None},
                "Classical": {"Beethoven": {"symphony9.mp3": None}},
            }
        },
        ["/Music/Classical/Beethoven/symphony9.mp3", "/Music/Pop/song1.mp3"],
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(("input_tree", "expected"), run_cases + submit_cases)
def test_list_files(input_tree: FileTree, expected: list[str]) -> None:
    print("\n---------------------------------")
    print(f"Input: {input_tree}")
    print("Expected:")
    for output in expected:
        print(f"    {output}")
    result = sorted(list_files(input_tree))
    print("Actual:")
    for res in result:
        print(f"    {res}")
    assert result == expected
