from dataclasses import field, dataclass
from enum import Enum, auto
import logging
from typing import List


logger = logging.getLogger(__name__)


class Gender(Enum):
    """Enumeration representing the gender of a person."""

    Female = auto()
    Male = auto()
    Unspecified = auto()


@dataclass
class Person:
    """
    Represents an individual with a first name, last name, and optional gender specification.

    :param firstname: The first name of the person.
    :param lastname: The last name of the person.
    :param gender: The gender of the person, defaulting to Gender.Unspecified.
    """

    firstname: str
    lastname: str
    gender: Gender = field(default=Gender.Unspecified)


class Greeter:
    """A tool to greet someone in several ways.

    :param person: the person to greet
    """

    _titles = {Gender.Female: "Mrs ", Gender.Male: "Mr ", Gender.Unspecified: "Mx "}

    def __init__(self, person: Person) -> None:
        self.person = person

    def greet_multiple_time(
        self, greet_count: int, *, is_formal: bool = True
    ) -> List[str]:
        """Greet a person.

        :param greet_count: the number of time to greet
        :param is_formal: whether to use a formal title, like "Mrs" when greeting, defaults to True
        :raises ValueError: if the greet count if not a positive integer
        :return: A List of greeting messages
        """

        if greet_count < 1:
            raise ValueError(
                f"Greeting count should be a positive integer, not {greet_count}"
            )

        # use title and lastname for a formal greeting, else only use the firstname
        name = self.person.lastname if is_formal else self.person.firstname
        title = self._titles[self.person.gender] if is_formal else ""

        logger.debug(
            "%i %s greeting%s incoming !",
            greet_count,
            "formal" if is_formal else "",
            "s" if greet_count > 1 else "",
        )

        message = f"Hello {title}{name} !"

        for _ in range(greet_count):
            print(message)

        return [message] * greet_count
