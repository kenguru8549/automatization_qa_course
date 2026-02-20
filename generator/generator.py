import random

from data.data import Person, Color
from faker import Faker #  библ содержит большое кол-во полей и данных для работы


faker_ru = Faker('ru_RU')  #  чтобы были данные на русском
Faker.seed()
def generated_person():
    yield Person(         #   вызываем класс персон с его полями
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        email=faker_ru.email(),
        salary=random.randint(32000, 178000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()
    )

def generated_file():
    path = rf'C:\Users\guskov-av\PycharmProjects\automatization_qa_course\filetest{random.randint(0, 999)}.txt'  #  прописываем путь к файлу и рандомно его создаем (rf -регулярное выражение)
    file = open(path, 'w+')  #  открываем файл по пути выше (w+ - метод обновления файла в функции open
    file.write(f'hello{random.randint(0, 999)}')  #  заполняем файл
    file.close()  #  закрываем файл
    return file.name, path  #  возвращаем имя файла (метод) и путь

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Black", "White"]
    )

