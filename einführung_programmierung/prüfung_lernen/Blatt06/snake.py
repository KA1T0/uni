from dataclasses import dataclass
from random import randint


# a)
@dataclass
class Vec2D:
    x: int
    y: int


v = Vec2D(52, 20)
print(v.x)
print(v.y)


# b)
def add_vecs(v1: Vec2D, v2: Vec2D) -> Vec2D:
    x = v1.x + v2.x
    y = v1.y + v2.y
    return Vec2D(x, y)


v1 = Vec2D(43, 10)
v2 = Vec2D(-4, 20)
print(add_vecs(v1, v2))


# c)
@dataclass
class Item:
    position: Vec2D
    energy: int


item = Item(Vec2D(4, 2), 3)
print(item.position)
print(item.energy)


# d)
@dataclass
class Snake:
    positions: list[Vec2D]
    direction: Vec2D
    alive: bool
    grow: int


s = Snake([Vec2D(0, 0), Vec2D(1, 0)], Vec2D(-1, 0), True, 6)
print(s.positions)
print(s.direction)
print(s.alive)
print(s.grow)


# d)
@dataclass
class Game:
    snake: Snake
    width: int
    height: int
    frame: int
    items: list[Item]


g = Game(Snake([Vec2D(3, 0), Vec2D(2, 0)], Vec2D(1, 0), True, 2), 16, 14, 0, [Item(Vec2D(7, 2), 3)])
print(g.width)
print(g.height)
print(g.frame)
print(g.items)
print(g.snake)


# f)
def turn_direction(direction: Vec2D, turn: int) -> Vec2D:
    if turn == 1:
        return Vec2D(-direction.y, direction.x)
    if turn == -1:
        return Vec2D(direction.y, -direction.x)
    else:
        return direction


position = Vec2D(1, 0)
print(turn_direction(position, 1))
print(turn_direction(position, -1))
print(turn_direction(position, 7))


def turn_snake(snake: Snake, turn: int) -> Snake:
    if snake.alive is False:
        print("schlange tod")
        return snake
    else:
        print("schlange lebt")
        return Snake(snake.positions, turn_direction(snake.direction, turn), snake.alive, snake.grow)


# g)
def grow_positions(positions: list[Vec2D], direction: Vec2D) -> list[Vec2D]:
    head = positions[0]
    return [add_vecs(head, direction)] + positions


def move_snake(snake: Snake) -> Snake:
    if snake.alive is False:
        return snake
    #new_position = grow_positions(snake.positions, snake.direction)
    if snake.grow == 0:
        return Snake(grow_positions(snake.positions, snake.direction)[:-1], snake.direction, snake.alive, snake.grow)
    else:
        return Snake(grow_positions(snake.positions, snake.direction), snake.direction, snake.alive, snake.grow - 1)


s = Snake([Vec2D(0, 0)], Vec2D(1, 0), True, 1)
s = move_snake(s)
print(s.positions)
print(s.grow)

s = move_snake(s)
print(s.positions)
print(s.grow)


# h)
def collision(snake: Snake, width: int, height: int) -> bool:
    head = snake.positions[0]
    if head in snake.positions[1:]:
        return True
    if (head.x < 0 or head.x >= width or head.y < 0 or head.y >= height):
        return True
    return False


s = Snake([Vec2D(9, 9)], Vec2D(1, 0), True, 0)
print(collision(s, 10, 10))
print(collision(s, 10, 9))


# i)
def generate_item(game: Game) -> Item:
    return Item(Vec2D(randint(0, game.width - 1), randint(0, game.height - 1)), randint(1, 5))


# j)
def pick_item(items: list[Item], position: Vec2D) -> tuple[list[Item], int]:
    new_items = []
    energy = 0
    for item in items:
        if position != item.position:
            new_items = new_items + [item]
        else:
            energy += item.energy
    return new_items, energy
