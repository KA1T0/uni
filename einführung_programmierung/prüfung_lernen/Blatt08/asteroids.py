from dataclasses import dataclass
from math import sqrt
import pygame


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

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, (self.position.x, self.position.y), self.radius)

    def update(self, width: int, height: int, delta: float):
        if not (0 <= self.position.x < width and 0 <= self.position.y < height):
            self.alive = False

    def is_colliding(self, other: "GameObject") -> bool:
        dist = Vec2D(self.position.x - other.position.x, self.position.y - other.position.y)
        return dist.abs() <= self.radius + other.radius

    def on_collision(self, other: "GameObject"):
        pass


@dataclass
class Projectile(GameObject):
    speed: float

    def update(self, width: int, height: int, delta: float):
        self.position.y -= delta * self.speed
        super().update(width, height, delta)

    def on_collision(self, other: 'GameObject'):
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
    shots: int
    hp: int

    def update(self, width: int, height: int, delta: float):
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        super().update(width, height, delta)

    def on_collision(self, other: 'GameObject'):
        match other:
            case Asteroid():
                self.hp -= other.radius
            case Health():
                self.hp += other.amount
            case Ammunition():
                self.shots += other.amount

    def shoot(self) -> Projectile:
        alive = False
        if self.shots:
            self.shots -= 1
            alive = True
        pos = Vec2D(self.position.x, self.position.y)
        return Projectile(pos, 5, alive, (255, 0, 0), 3)


@dataclass
class Asteroid(StaticObject):
    special: bool

    def on_collision(self, other: 'GameObject'):
        if not isinstance(other, Asteroid):
            self.alive = False
