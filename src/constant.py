from enum import Enum

from faker import Faker

faker = Faker("ru_RU")


class BookingData(Enum):
    FIRSTNAME = faker.first_name()
    LASTNAME = faker.last_name()
    FIRSTNAME_UPDATE = faker.first_name() + "456"
    LASTNAME_UPDATE = faker.last_name() + "123"
