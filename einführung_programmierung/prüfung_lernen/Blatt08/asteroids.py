from dataclasses import dataclass
from math import sqrt


# a)
@dataclass
class Vec2D:
    x: float
    y: float

# b)
    def abs(self) -> float:
        return sqrt(self.x**2 + self.y**2)


# c)
@dataclass
class GameObject:
    position: Vec2D
    radius: int
    alive: bool
    color: tuple[int, int, int]

    def update(self, width: int, height: int, delta: float):
        if not (0 <= self.position.x < width and 0 <= self.position.y < height):
            self.alive = False

    def is_colliding(self, other: 'GameObject') -> bool:
        d = Vec2D(self.position.x - other.position.x, self.position.y - other.position.y)
        return d.abs() <= self.radius + other.radius

    def on_clossing(self, other: 'GameObject'):
        pass


@dataclass
class Projectile(GameObject):
    speed: float

    def update(self, width: int, height: int, delta: float):
        self.position.y -= (delta * self.speed)
        super().update(width, height, delta)

    def on_clossing(self, other: 'GameObject'):
        if not isinstance(other, Ship):
            self.alive = False

@dataclass
class StaticObject(GameObject):
    rotation: float

    def update(self, width: int, height: int, delta: float):
        self.position.y += delta
        self.rotation += delta / self.radius
        super().update(width, height, delta)

    def on_clossing(self, other: 'GameObject'):
        self.alive = False


@dataclass
class Item(StaticObject):
    amount: int


@dataclass
class Ammunition(Item):
    pass


@dataclass
class Health(Item):
    pass


@dataclass
class Ship(GameObject):
    shot: int
    hp: int


@dataclass
class Asteroid(StaticObject):
    special: bool
