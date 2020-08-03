# from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop


T = TypeVar('T')


def linear_contains(iterable, key):
    for item in iterable:
        if item == key:
            return True
    return False


C = TypeVar("c", bound="Comparable")


class Comparable(Protocol):
    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        return (not self < other) and self != other
    
    def __le__(self, other):
        return not self < other or self == other

    def __ge__(self, other):
        return not self < other


def binary_contains(sequence, key):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False


class Stack(Generic[T]):
    def __init__(self):
        self._container = []


    @property
    def empty(self):
        return not self._container

    def push(self, item):
        self._container.append(item)

    def pop(self):
        return self._container.pop()
    
    def __repr__(self):
        return repr(self._container)



if __name__ == '__main__':
    print(linear_contains([1, 5, 15, 15, 14, 15, 20], 5))
    print(binary_contains(["a", "b", "c", "d", "e"], "e"))
