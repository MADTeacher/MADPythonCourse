from dataclasses import dataclass

from faker import Faker


@dataclass
class Student:
    name: str
    age: int
    course: int
    group_name: str
    address: str
    vk_url: str

    def __str__(self):
        info: str = f"Name: {self.name} \n" \
                    f"Age: {self.age} " \
                    f"Course: {self.course} \n" \
                    f"Group name: {self.group_name} \n" \
                    f"Address: {self.address} \n" \
                    f"Vk url: {self.vk_url} "
        return info


def create_fake_student(faker: Faker) -> Student:
    course = faker.random.randint(1, 4)
    return Student(
        name=faker.name(),
        age=faker.random.randint(16, 25),
        course=course,
        group_name=faker.bothify(text=f'{course}-???-##', letters='МДАТИ'),
        address=faker.address(),
        vk_url='https://vk.com/' + faker.user_name()
    )


if __name__ == '__main__':
    my_faker = Faker('ru_RU')
    for i in range(6):
        print('*' * 10 + f' {i} ' + '*' * 10)
        print(create_fake_student(my_faker))
