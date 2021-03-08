from typing import Optional, List

from item import Item
from storage_system_interface import StorageSystemInterface
from item_child import Box, Book, Bottle
from car import Car
from garage import Garage
from cupboard import Cupboard


class Person:

    def __init__(self, name: str, storage_interface: StorageSystemInterface):
        self.__storage_interface = storage_interface
        self.__name = name

    def change_interface(self, storage_interface: StorageSystemInterface):
        self.__storage_interface = storage_interface

    def save_item(self, item: Item) -> None:
        self.__storage_interface.push_item(item)

    def pop_item(self) -> Item:
        return self.__storage_interface.pop_item()

    def pop_item_by_name(self, item_name: str) -> Optional[Item]:
        return self.__storage_interface.pop_target_item(item_name)

    def amount_storage_items(self) -> int:
        return self.__storage_interface.amount_storage_items()

    def print_storage_item_list(self):
        items: List[str] = [it.name for it in self.__storage_interface.get_items()]
        print(items)

    def __repr__(self):
        return f"{self.__name} запрятал {self.amount_storage_items()} вещей!"


if __name__ == '__main__':
    car: Car = Car("h134if123", 20)
    cupboard: Cupboard = Cupboard(40)
    garage: Garage = Garage("очень далеко д.21", 10)

    car.push_item(Book("dsfsdf", 200, 0.5))
    car.push_item(Box(1, 2, 3))

    person: Person = Person("Петр", car)
    person.save_item(Bottle("Жижа", 29, 0.7))
    person.save_item(Bottle("Жижа 2.1", 29, 1.7))
    print(person.pop_item())

    person.change_interface(garage)
    print(person.amount_storage_items())
    person.save_item(Bottle("Жижа", 29, 0.7))
    person.save_item(Bottle("Жижа 2.1", 29, 1.7))




