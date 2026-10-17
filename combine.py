class Cache[T]:
    def __init__(self, items: list[T]) -> None:
        self.items = items


def combine[T, U](
    first: Cache[T],
    second: Cache[U],
) -> Cache[T | U]:
    return Cache(first.items + second.items)


def example() -> None:
    integers = Cache([1, 2, 3])
    strings = Cache(["a", "b", "c"])

    result = combine(integers, strings)
    reveal_type(result)
