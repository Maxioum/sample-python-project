import pytest

from greeting.simple import greet


@pytest.mark.parametrize(
    ("name", "expected_result"),
    [
        ("John", "Hello John !"),
    ],
)
def test_module(name: str, expected_result: str) -> None:
    assert greet(name) == expected_result
