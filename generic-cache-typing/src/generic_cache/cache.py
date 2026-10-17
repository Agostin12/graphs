from dataclasses import dataclass


@dataclass
class Cache[T]:
    """A small mutable container for values of type T."""

    items: list[T]

    def get_items(self) -> list[T]:
        """Return the stored items."""
        return self.items


def combine[T, U](first: Cache[T], second: Cache[U]) -> Cache[T | U]:
    """Combine two caches while preserving both element types in the result."""
    return Cache(first.get_items() + second.get_items())
