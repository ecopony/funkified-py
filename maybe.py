from typing import TypeVar, Generic, Callable
from abc import abstractmethod
from __future__ import annotations # why do we need this? is mypy using 3.10?

T = TypeVar("T")
A = TypeVar("A")
B = TypeVar("B")

class Maybe(Generic[T]):
    @abstractmethod
    def map(self, fn: Callable[[T], B]) -> Maybe[B]:
        pass
    
    @abstractmethod
    def getOrElseValue(self, defaultValue: T) -> T:
        pass


class Just(Maybe[A]):
    value: A

    def __init__(self, value: A):
        self.value = value

    def map(self, fn: Callable[[A], B]) -> Maybe[B]:
        return Just(fn(self.value))

    def getOrElseValue(self, _: A) -> A:
        return self.value


class Nothing(Maybe[T]):
    def frmp(stuff):
        print(stuff)
