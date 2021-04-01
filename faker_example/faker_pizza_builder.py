from enum import Enum, auto
from collections import namedtuple

from faker import Faker
from faker.providers import BaseProvider

# объявим именованный кортеж для свойств основы пиццы
PizzaBase = namedtuple('PizzaBase', ['DoughDepth', 'DoughType'])


class PizzaDoughDepth(Enum):
    THIN = auto()
    THICK = auto()


class PizzaDoughType(Enum):
    WHEAT = auto()
    CORN = auto()
    RYE = auto()


class PizzaSauceType(Enum):
    PESTO = auto()
    WHITE_GARLIC = auto()
    BARBEQUE = auto()
    TOMATO = auto()


class PizzaTopLevelType(Enum):
    MOZZARELLA = auto()
    SALAMI = auto()
    BACON = auto()
    MUSHROOMS = auto()
    SHRIMPS = auto()


# Класс компонуемого продукта
class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time = None  # in minute

    def __str__(self):
        info: str = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough.DoughDepth.name} & " \
                    f"{self.dough.DoughType.name}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[it.name for it in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info


class PizzaProvider(BaseProvider):
    NAMES = ['Маргарита', '4 сыра', 'Салями', 'Мexico', 'Дьябло', 'Сицилийская', 'Капричоза', 'Кальцоне']
    DOUGH_DEPTH = [PizzaDoughDepth.THIN, PizzaDoughDepth.THICK]
    DOUGH_TYPE = [PizzaDoughType.RYE, PizzaDoughType.WHEAT, PizzaDoughType.CORN]

    SAUCE = [PizzaSauceType.TOMATO, PizzaSauceType.BARBEQUE,
             PizzaSauceType.PESTO, PizzaSauceType.WHITE_GARLIC]

    TOPPING = [PizzaTopLevelType.MOZZARELLA, PizzaTopLevelType.BACON,
               PizzaTopLevelType.SALAMI, PizzaTopLevelType.MUSHROOMS,
               PizzaTopLevelType.SHRIMPS]

    def create_fake_pizza(self):
        pizza = Pizza(self.random_element(self.NAMES))
        pizza.dough = PizzaBase(
            self.random_element(self.DOUGH_DEPTH),
            self.random_element(self.DOUGH_TYPE)
        )
        pizza.sauce = self.random_element(self.SAUCE)
        rand_amount_topping = self.random_int(2, len(self.TOPPING))
        for _ in range(rand_amount_topping):
            pizza.topping.append(self.random_element(self.TOPPING))

        pizza.cooking_time = self.random_int(10, 20)
        return pizza


if __name__ == '__main__':
    my_faker = Faker()
    my_faker.add_provider(PizzaProvider)
    for i in range(6):
        print('*'*10 + f' {i} ' + '*'*10)
        print(my_faker.create_fake_pizza())













