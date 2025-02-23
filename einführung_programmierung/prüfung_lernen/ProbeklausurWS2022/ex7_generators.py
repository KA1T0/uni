# Aufgabe 7 (Generatoren) ####################################################

from typing import Callable, Iterator, Iterable


def drop(xs: Iterable, n: int) -> Iterator:
    count = 0
    for x in xs:
        if count >= n:
            yield x
        count += 1


def split(xs: Iterable, sep) -> Iterator[list]:
    chunk = []
    for x in xs:
        if x == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(x)
    yield chunk


# Tests  ######################################################################
if __name__ == "__main__":

    print(list(drop([2, 4, 6, 8, 10, 12], 3)))

    assert list(split([1, 5, 3, 4, 9, 3, 5], 3)) == [[1, 5], [4, 9], [5]]
    assert list(split("mississippi", "i")) == [
        ["m"], ["s", "s"], ["s", "s"], ["p", "p"], []
    ]
