from dataclasses import dataclass
from enum import Enum


# a)
class Tag(Enum):
    P = 'p'
    STRONG = 'strong'
    II = 'ii'
    DIV = 'div'
    H1 = 'h1'


# b)
@dataclass
class Node:
    tag: Tag
    children: list['Node'] | str
    

def validate(tree: Node) -> bool:
    match tree:
        case Node(Tag.II, str()):
            return True
        case Node(Tag.DIV, str()):
            return False
        case Node(Tag.DIV, list(children)):
            return True
        case _:
            return False
        

print(validate(Node(Tag.II, "Hallo Welt")))
print(validate(Node(Tag.DIV, "Hallo Welt")))
print(validate(Node(Tag.DIV, [Node(Tag.H1, "Ganz Oben"),Node(Tag.STRONG, ""), Node(Tag.DIV, [])])))