from item import Item


class Book(Item):

    def __init__(self, name: str, amount_list: int, weight: float):
        super().__init__(name, weight)
        self.__amount_list: int = amount_list

    @property
    def amount_list(self) -> int:
        return self.__amount_list

    def do_something(self):
        print(f"Книга '{self.name}' содержит {self.amount_list} страниц!")

    def __repr__(self):
        return f"Книга '{self.name}'"


class Box(Item):

    def __init__(self, width: int, height: int, weight: float):
        super().__init__("Коробка", weight)
        self.__width = width
        self.__height = height

    @property
    def height(self) -> int:
        return self.__height

    @property
    def width(self) -> int:
        return self.__width

    def square(self) -> int:
        return self.__height * self.__width

    def do_something(self):
        print(f"{self.name} имеет площадь {self.square} м^2!")

    def __repr__(self):
        return f"Коробка c площадью {self.square} м^2!"


class Bottle(Item):

    def __init__(self, name_liquid: str, amount_liquid: float, k_liquid: float):
        super().__init__(name_liquid, amount_liquid * k_liquid)
        self.__amount_liquid = amount_liquid
        self.__k_liquid = k_liquid

    def do_something(self):
        print(f"Жидкость '{self.name}' весит {self.weight} кг!")

    def __repr__(self):
        return f"Бутылка c жидкостью '{self.name}'"
