from dataclasses import dataclass
from typing import Optional


@dataclass
class Node[T]:
    mark: T
    left: Optional['Node[T]'] = None
    right: Optional['Node[T]'] = None


type BTree[T] = Optional[Node[T]]


def tree_max[T: (str, int)](btree: BTree[T]) -> Optional[T]:
    match btree:
        case None:
            return None
        case Node(mark, None, None):
            return mark
        case Node(mark, None, right)