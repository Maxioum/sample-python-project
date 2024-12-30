import pytest
from pytest import FixtureRequest

from greeting.complex import Greeter


@pytest.mark.parametrize(
    ("greeter_fixture", "title", "greet_count"),
    [("male_greeter", "Mr", 1), ("gender_unspecified_greeter", "Mx", 2)],
)
def test_greet_multiple_time_formal(
    greeter_fixture: str, title: str, greet_count: int, request: FixtureRequest
) -> None:
    greeter: Greeter = request.getfixturevalue(greeter_fixture)
    assert (
        greeter.greet_multiple_time(greet_count)
        == [f"Hello {title} {greeter.person.lastname} !"] * greet_count
    )


@pytest.mark.parametrize(
    ("greeter_fixture", "greet_count"),
    [("male_greeter", 1), ("gender_unspecified_greeter", 2)],
)
def test_greet_multiple_time_not_formal(
    greeter_fixture: str, greet_count: int, request: FixtureRequest
) -> None:
    greeter: Greeter = request.getfixturevalue(greeter_fixture)
    assert (
        greeter.greet_multiple_time(greet_count, is_formal=False)
        == [f"Hello {greeter.person.firstname} !"] * greet_count
    )


@pytest.mark.parametrize("greet_count", range(1, 10))
def test_multiple_greetings(male_greeter: Greeter, greet_count: int) -> None:
    assert (
        male_greeter.greet_multiple_time(greet_count, is_formal=False)
        == [f"Hello {male_greeter.person.firstname} !"] * greet_count
    )


@pytest.mark.parametrize("greet_count", [-2, -1, 0])
def test_non_positive_greet_count(
    gender_unspecified_greeter: Greeter, greet_count: int
) -> None:
    with pytest.raises(ValueError):
        gender_unspecified_greeter.greet_multiple_time(greet_count, is_formal=False)
