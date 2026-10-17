
from typing import Generic, TypeVar

T = TypeVar("T")

class Cache(Generic[T]):
    def __init__(self, items: list[T]) -> None:
        self.items = items

    def get_items(self) -> list[T]:
        return self.items


def combine[T](first: Cache[T], second: Cache[T]) -> Cache[T]:
    return Cache(first.get_items() + second.get_items())


def example() -> None:
    integers = Cache([1, 2, 3])
    floats = Cache([4.5, 5.5])

    result = combine(integers, floats)
    reveal_type(result)
