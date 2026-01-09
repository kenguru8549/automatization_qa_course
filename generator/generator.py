from data.data import Person
from faker import Faker #  библ содержит большое кол-во полей и данных для работы


faker_ru = Faker('ru_RU')  #  чтобы были данные на русском
Faker.seed()
def generated_person():
    yield Person(         #   вызываем класс персон с его полями
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )
