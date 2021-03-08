from typing import Tuple, Optional, List

from item import Item
from storage_system_interface import StorageSystemInterface
from my_exceptions import NoItemException, FullStorageException


class Garage(StorageSystemInterface):

    def __init__(self, address: str, max_storage_item: int):
        self.__address: str = address
        self.__max_storage_item: int = max_storage_item
        self.__items_list: List[Item] = []

    def push_item(self, item: Item) -> None:
        if len(self.__items_list) <= self.__max_storage_item:
            self.__items_list.append(item)
        else:
            raise FullStorageException("Это не черная дыра или дамская сумочка!!! Это гараж!!!")

    def pop_item(self) -> Item:
        if self.is_empty():
            raise NoItemException("Кирпичи выносить будешь?")
        return self.__items_list.pop()

    def pop_target_item(self, item_name: str) -> Optional[Item]:
        result = next((it for it in self.__items_list if it.name == item_name), None)
        if result is not None:
            self.__items_list.remove(result)
        return result

    def get_items(self) -> Tuple[Item, ...]:
        return tuple(self.__items_list)

    def is_empty(self) -> bool:
        return len(self.__items_list) <= 0

    def amount_storage_items(self) -> int:
        return len(self.__items_list)

    def is_contains(self, item_name: str) -> bool:
        result = next((it for it in self.__items_list if it.name == item_name), None)
        return result is not None

    @property
    def address(self) -> str:
        return self.__address

    def __repr__(self):
        return f"Гараж содержит {len(self.__items_list)} вещей"

    def open(self):
        ...

    def close(self):
        ...

    def clear(self):
        ...