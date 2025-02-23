from math import isclose

from asteroids import (
    Vec2D, GameObject, Projectile, StaticObject,
    Item, Ammunition, Health, Ship, Asteroid
)


def test_abs():
    assert isclose(Vec2D(1.0, 0.0).abs(), 1.0)
    assert isclose(Vec2D(0.0, 0.0).abs(), 0.0)
    assert isclose(Vec2D(1.0, -1.0).abs(), 2 ** 0.5)
    assert isclose(Vec2D(-3.0, 4.0).abs(), 5.0)
    assert isclose(Vec2D(-12.0, -5.0).abs(), 13.0)


white = (255, 255, 255)


def test_objects():
    assert (GameObject(Vec2D(1, 2), 3, True, white) ==
            GameObject(position=Vec2D(1, 2), radius=3, alive=True, color=white))
    assert (Projectile(Vec2D(4, 5), 6, True, white, 7) ==
            Projectile(position=Vec2D(4, 5), radius=6, alive=True, color=white, speed=7))
    assert (StaticObject(Vec2D(8, 9), 10, True, white, 11) ==
            StaticObject(position=Vec2D(8, 9), radius=10, alive=True, color=white, rotation=11))
    assert (Item(Vec2D(12, 13), 14, True, white, 15, 16) ==
            Item(position=Vec2D(12, 13), radius=14, alive=True, color=white, rotation=15, amount=16))
    assert (Ammunition(Vec2D(17, 18), 19, True, white, 20, 21) ==
            Ammunition(position=Vec2D(17, 18), radius=19, alive=True, color=white, rotation=20, amount=21))
    assert (Health(Vec2D(22, 23), 24, True, white, 25, 26) ==
            Health(position=Vec2D(22, 23), radius=24, alive=True, color=white, rotation=25, amount=26))
    assert (Ship(Vec2D(27, 28), 29, True, white, 30, 31) ==
            Ship(position=Vec2D(27, 28), radius=29, alive=True, color=white, shots=30, hp=31))
    assert (Asteroid(Vec2D(32, 33), 34, True, white, 35, False) ==
            Asteroid(position=Vec2D(32, 33), radius=34, alive=True, color=white, rotation=35, special=False))


def test_update():
    o1 = GameObject(Vec2D(999, 999), 50, True, white)
    o1.update(1000, 1000, 1)
    assert o1.alive
    o1.position = Vec2D(1000, 1000)
    o1.update(1000, 1000, 1)
    assert not o1.alive
    o2 = Projectile(Vec2D(0, 0), 5, True, white, 150)
    o2.update(1000, 1000, 1)
    assert isclose(o2.position.y, -150)
    assert not o2.alive
    o3 = StaticObject(Vec2D(1000, 1000), 5, True, white, 0)
    o3.update(1000, 1000, 10)
    assert isclose(o3.position.y, 1010)
    assert not o3.alive
    o4 = Ship(Vec2D(5, 5), 10, True, white, 49, -5)
    o4.update(1000, 1000, 1)
    assert o4.hp == 0
    assert not o4.alive
    o5 = Ship(Vec2D(5, 5), 10, True, white, 49, 0)
    o5.update(1000, 1000, 1)
    assert o5.hp == 0
    assert not o5.alive
    o6 = Ship(Vec2D(5000, 50), 10, True, white, 49, 10)
    o6.update(1000, 1000, 1)
    assert not o6.alive


def test_is_colliding():
    o1 = Ship(Vec2D(50, 50), 50, True, white, 0, 100)
    o2 = Projectile(Vec2D(100, 30), 7, True, white, 10)
    assert o1.is_colliding(o2)
    assert o2.is_colliding(o1)
    o3 = Projectile(Vec2D(100, 20), 7, True, white, 10)
    assert not o1.is_colliding(o3)
    assert not o3.is_colliding(o1)
    assert o2.is_colliding(o3)
    assert o3.is_colliding(o2)


def test_on_collision():
    o1 = GameObject(Vec2D(1, 2), 3, True, white)
    o2 = GameObject(Vec2D(4, 5), 6, True, white)
    o1.on_collision(o2)
    o2.on_collision(o1)
    assert o1 == GameObject(Vec2D(1, 2), 3, True, white)
    assert o2 == GameObject(Vec2D(4, 5), 6, True, white)
    o3 = StaticObject(Vec2D(7, 8), 9, True, white, 0)
    o1.on_collision(o3)
    assert o3.alive
    o3.on_collision(o1)
    assert not o3.alive
    o4 = Projectile(Vec2D(10, 11), 12, True, white, 0)
    o5 = Ship(Vec2D(13, 14), 15, True, white, 16, 17)
    o4.on_collision(o5)
    assert o4.alive
    o4.on_collision(o3)
    assert not o4.alive
    o6 = Asteroid(Vec2D(18, 19), 20, True, white, 0, False)
    o6.on_collision(o6)
    assert o6.alive
    o6.on_collision(o5)
    assert not o6.alive
    o5.on_collision(o6)
    assert o5.hp == -3
    o7 = Ship(Vec2D(21, 22), 23, True, white, 24, 25)
    o8 = Health(Vec2D(26, 27), 28, True, white, 29, 30)
    o7.on_collision(o8)
    assert o7.hp == 55
    o9 = Ship(Vec2D(31, 32), 33, True, white, 34, 35)
    o10 = Ammunition(Vec2D(36, 37), 38, True, white, 39, 40)
    o9.on_collision(o10)
    assert o9.shots == 74


def test_shoot():
    s1 = Ship(Vec2D(50, 50), 30, True, white, 2, 10)
    p1 = s1.shoot()
    assert s1.shots == 1
    assert p1.position == s1.position
    assert p1.position is not s1.position
    assert p1.alive
    p2 = s1.shoot()
    assert s1.shots == 0
    assert p2.alive
    p3 = s1.shoot()
    assert s1.shots == 0
    assert not p3.alive


if __name__ == '__main__':
    test_abs()
    test_objects()
    test_update()
    test_is_colliding()
    test_on_collision()
    test_shoot()
