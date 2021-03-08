from abc import ABC, abstractmethod
from typing import Optional, Tuple

from item import Item


class StorageSystemInterface(ABC):

    @abstractmethod
    def push_item(self, item: Item) -> None:
        pass

    @abstractmethod
    def pop_item(self) -> Item:
        pass

    @abstractmethod
    def pop_target_item(self, item_name: str) -> Optional[Item]:
        pass

    @abstractmethod
    def get_items(self) -> Tuple[Item, ...]:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def amount_storage_items(self) -> int:
        pass

    @abstractmethod
    def is_contains(self, item_name: str) -> bool:
        pass
