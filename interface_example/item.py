from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, name: str, weight: float):
        self.__name: str = name
        self.__weight: float = weight

    @property
    def name(self) -> str:
        return self.__name

    @property
    def weight(self) -> float:
        return self.__weight

    @abstractmethod
    def do_something(self):
        ...

