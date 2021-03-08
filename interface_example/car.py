from enum import Enum
from typing import Tuple, Optional, List, Dict

from item import Item
from storage_system_interface import StorageSystemInterface
from my_exceptions import NoItemException, FullStorageException


class StorageTypeEnum(Enum):
    NONE = 1
    CABIN = 2
    CARCASE = 3


class Car(StorageSystemInterface):

    def __init__(self, number: str, max_storage_item: int = 30):
        self.number: str = number
        self.__max_storage_item: int = max_storage_item
        self.__max_cabin_item: int = max_storage_item // 3
        self.__max_carcase_item: int = max_storage_item - self.__max_cabin_item
        self.__items_storage: Dict[StorageTypeEnum, List[Item]] = {
            StorageTypeEnum.CABIN: [],
            StorageTypeEnum.CARCASE: []
        }
        self.__last_used_storage: StorageTypeEnum = StorageTypeEnum.NONE

    def push_item(self, item: Item) -> None:
        last_used_storage: StorageTypeEnum = StorageTypeEnum.NONE
        if len(self.__items_storage[StorageTypeEnum.CARCASE]) <= self.__max_carcase_item:
            self.__items_storage[StorageTypeEnum.CARCASE].append(item)
            last_used_storage = StorageTypeEnum.CARCASE
        elif len(self.__items_storage[StorageTypeEnum.CABIN]) <= self.__max_cabin_item:
            self.__items_storage[StorageTypeEnum.CABIN].append(item)
            last_used_storage = StorageTypeEnum.CABIN

        if last_used_storage is StorageTypeEnum.NONE:
            raise FullStorageException("Ну ты даешь!!! Такой посадке все на кавказе обзавидуются!!!")
        else:
            self.__last_used_storage = last_used_storage

    def pop_item(self) -> Item:
        if (self.__last_used_storage is StorageTypeEnum.NONE) or self.is_empty():
            raise NoItemException("Достаем двигатель или запаску из машины?")
        if not self.__items_storage[self.__last_used_storage]:
            if self.__last_used_storage is StorageTypeEnum.CARCASE:
                self.__last_used_storage = StorageTypeEnum.CABIN
            else:
                self.__last_used_storage = StorageTypeEnum.CARCASE
        return self.__items_storage[self.__last_used_storage].pop()

    def pop_target_item(self, item_name: str) -> Optional[Item]:
        result: Optional[Item] = None
        result = next((it for it in self.__items_storage[StorageTypeEnum.CABIN] if it.name == item_name), None)
        if result is not None:
            self.__items_storage[StorageTypeEnum.CABIN].remove(result)
            return result

        result = next((it for it in self.__items_storage[StorageTypeEnum.CARCASE] if it.name == item_name), None)
        if result is not None:
            self.__items_storage[StorageTypeEnum.CARCASE].remove(result)
            return result

        print("Лови дырку от бублика!")
        return result

    def get_items(self) -> Tuple[Item, ...]:
        result: List[Item] = self.__items_storage[StorageTypeEnum.CARCASE][:]
        result.extend(self.__items_storage[StorageTypeEnum.CABIN][:])
        return tuple(result)

    def is_empty(self) -> bool:
        return ((len(self.__items_storage[StorageTypeEnum.CABIN]) <= 0) and
                (len(self.__items_storage[StorageTypeEnum.CARCASE]) <= 0))

    def amount_storage_items(self) -> int:
        return (len(self.__items_storage[StorageTypeEnum.CABIN]) +
                len(self.__items_storage[StorageTypeEnum.CARCASE]))

    def is_contains(self, item_name: str) -> bool:
        result_cabin = next((it for it in self.__items_storage[StorageTypeEnum.CABIN] if it.name == item_name), None)
        result_carcase = next((it for it in self.__items_storage[StorageTypeEnum.CARCASE] if it.name == item_name), None)
        return not ((result_cabin is None) and (result_carcase is None))

    def __repr__(self):
        return f"В машине содержится {self.amount_storage_items()} вещей"

    def start(self):
        ...

    def stop(self):
        ...

    def open(self):
        ...
