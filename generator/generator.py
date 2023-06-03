import random

from data.data import Person

from faker import Faker
faker_ru= Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() +  " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_ru.job(),  # тут должна быть ваша база данных =)
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_file():
    path = rf'G:\Projects\filetest{random.randint(0, 999)}.txt'
    file = open(path,
                'w+')  # 'w' open for writing, truncating the file first     '+' open a disk file for updating (reading and writing)
    file.write(f'HELLO FROM VKT =) {random.randint(0, 999)}')  # немного креатива
    file.close()
    return file.name, path