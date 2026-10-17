from generic_cache import Cache, combine


def test_cache_stores_items() -> None:
    cache = Cache([1, 2, 3])
    assert cache.get_items() == [1, 2, 3]


def test_combine_same_element_types() -> None:
    first = Cache([1, 2])
    second = Cache([3, 4])
    result = combine(first, second)

    assert result.items == [1, 2, 3, 4]


def test_combine_different_element_types() -> None:
    numbers = Cache([1, 2])
    words = Cache(["three", "four"])
    result = combine(numbers, words)

    assert result.items == [1, 2, "three", "four"]


def test_combine_empty_caches() -> None:
    first: Cache[int] = Cache([])
    second: Cache[str] = Cache([])
    result = combine(first, second)

    assert result.items == []
