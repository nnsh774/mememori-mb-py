__all__ = ('Flags',)

from enum import Enum
from typing import TypeVar, Generic

T = TypeVar('T', bound=Enum)

class Flags(Generic[T]):
    def __init__(self, values: T | list[T]) -> None:
        self.values = values if isinstance(values, list) else [values]

    def __int__(self) -> int:
        v: int = 0
        for value in self.values:
            v = (v | value.value)
        return v

    def __getitem__(self, which) -> T:
        return self.values[which]
