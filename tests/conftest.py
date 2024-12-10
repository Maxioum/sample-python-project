from pytest import fixture
from faker import Faker

from greeting.complex import Greeter, Person, Gender


@fixture
def person_male(faker: Faker) -> Person:
    return Person(faker.first_name_male(), faker.last_name_male(), Gender.Male)


@fixture
def person_gender_unspecified(faker: Faker) -> Person:
    return Person(faker.first_name_nonbinary(), faker.last_name_nonbinary(), Gender.Unspecified)


@fixture
def male_greeter(person_male: Person) -> Greeter:
    return Greeter(person_male)


@fixture
def gender_unspecified_greeter(person_gender_unspecified: Person) -> Greeter:
    return Greeter(person_gender_unspecified)
