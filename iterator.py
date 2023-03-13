from __future__ import annotations
from typing import Any, List


class Iterator:
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration()


class IterableCollection:
    def __init__(self) -> None:
        self._collection = []

    def __iter__(self) -> Iterator:
        return Iterator(self._collection)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)
