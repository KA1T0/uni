from snake import (
    Vec2D, add_vecs, Item, Snake, Game, turn_direction, turn_snake,
    grow_positions, move_snake, collision, generate_item, pick_item
)


def test_Vec2D():
    v = Vec2D(52, 20)
    assert v.x == 52
    assert v.y == 20


def test_add_vecs():
    v1 = Vec2D(43, 10)
    v2 = Vec2D(-4, 20)
    res = add_vecs(v1, v2)
    assert res == Vec2D(39, 30)


def test_Item():
    it = Item(Vec2D(4, 2), 3)
    assert it.position == Vec2D(4, 2)
    assert it.energy == 3


def test_Snake():
    s = Snake([Vec2D(0, 0), Vec2D(1, 0)], Vec2D(-1, 0), True, 6)
    assert s.positions == [Vec2D(0, 0), Vec2D(1, 0)]
    assert s.direction == Vec2D(-1, 0)
    assert s.alive is True
    assert s.grow == 6


def test_Game():
    g = Game(Snake([Vec2D(3, 0), Vec2D(2, 0)], Vec2D(1, 0), True, 2),
             16, 14, 0, [Item(Vec2D(7, 2), 3)])
    assert g.snake == Snake([Vec2D(3, 0), Vec2D(2, 0)], Vec2D(1, 0), True, 2)
    assert g.width == 16
    assert g.height == 14
    assert g.frame == 0
    assert g.items == [Item(Vec2D(7, 2), 3)]


def test_turn_direction():
    d = Vec2D(1, 0)
    d2 = turn_direction(d, 0)
    assert d == d2 == Vec2D(1, 0)
    d3 = turn_direction(d, 1)
    assert d3 != d
    dirs = []
    for _ in range(4):
        d = turn_direction(d, 1)
        dirs = dirs + [d]
    assert dirs == [Vec2D(0, 1), Vec2D(-1, 0), Vec2D(0, -1), Vec2D(1, 0)]
    dirs = []
    for _ in range(4):
        d = turn_direction(d, -1)
        dirs = dirs + [d]
    assert dirs == [Vec2D(0, -1), Vec2D(-1, 0), Vec2D(0, 1), Vec2D(1, 0)]


def test_turn_snake():
    s1 = Snake([Vec2D(2, 4)], Vec2D(0, 1), True, 4)
    s2 = turn_snake(s1, 0)
    assert s1 == s2
    s3 = Snake([Vec2D(2, 4)], Vec2D(0, 1), False, 4)
    s4 = turn_snake(s3, 1)
    assert s3 == s4
    s5 = Snake([Vec2D(2, 4)], Vec2D(0, 1), True, 5)
    s6 = turn_snake(s5, 1)
    assert s6 == Snake([Vec2D(2, 4)], Vec2D(-1, 0), True, 5)
    assert s5 is not s6


def test_grow_positions():
    ps = [Vec2D(0, 0), Vec2D(1, 0), Vec2D(1, 1)]
    ps2 = grow_positions(ps, Vec2D(0, 1))
    assert ps2 == [Vec2D(0, 1), Vec2D(0, 0), Vec2D(1, 0), Vec2D(1, 1)]
    assert ps2 is not ps
    ps3 = grow_positions(ps2, Vec2D(0, 1))
    assert ps3 == [Vec2D(0, 2), Vec2D(0, 1), Vec2D(0, 0), Vec2D(1, 0), Vec2D(1, 1)]
    assert ps3 is not ps2


def test_move_snake():
    s1 = Snake([Vec2D(0, 0)], Vec2D(1, 0), False, 2)
    s2 = move_snake(s1)
    assert s1 == s2
    s3 = Snake([Vec2D(0, 0), Vec2D(0, 1), Vec2D(0, 2)], Vec2D(1, 0), True, 0)
    s4 = move_snake(s3)
    assert s4 == Snake([Vec2D(1, 0), Vec2D(0, 0), Vec2D(0, 1)], Vec2D(1, 0), True, 0)
    assert s3 is not s4
    s5 = Snake([Vec2D(0, 0)], Vec2D(1, 0), True, 2)
    s6 = move_snake(s5)
    assert s6 == Snake([Vec2D(1, 0), Vec2D(0, 0)], Vec2D(1, 0), True, 1)
    assert s5 is not s6
    s7 = move_snake(s6)
    assert s7 == Snake([Vec2D(2, 0), Vec2D(1, 0), Vec2D(0, 0)], Vec2D(1, 0), True, 0)
    assert s7 is not s6


def test_collide():
    s1 = Snake([Vec2D(9, 9)], Vec2D(1, 0), True, 0)
    assert not collision(s1, 10, 10)
    assert collision(s1, 10, 9)
    s2 = Snake([Vec2D(4, 4), Vec2D(4, 3), Vec2D(3, 3), Vec2D(3, 4), Vec2D(4, 4)],
               Vec2D(0, 1), True, 0)
    assert collision(s2, 10, 10)
    s3 = Snake([Vec2D(-1, 3)], Vec2D(1, 0), True, 3)
    assert collision(s3, 10, 10)


def test_generate_item():
    g = Game(Snake([Vec2D(3, 0)], Vec2D(1, 0), True, 0), 1, 1, 0, [])
    it = generate_item(g)
    assert it.position == Vec2D(0, 0)
    assert 1 <= it.energy <= 5


def test_pick_item():
    its = [Item(Vec2D(0, 0), 1), Item(Vec2D(3, 4), 3), Item(Vec2D(0, 0), 4)]
    its2, s1 = pick_item(its, Vec2D(0, 0))
    assert s1 == 5
    assert its2 == [Item(Vec2D(3, 4), 3)]
    its3, s2 = pick_item(its2, Vec2D(1, 2))
    assert s2 == 0
    assert its2 == its3
    assert its2 is not its3


if __name__ == '__main__':
    test_Vec2D()
    test_add_vecs()
    test_Item()
    test_Snake()
    test_Game()
    test_turn_direction()
    test_turn_snake()
    test_grow_positions()
    test_move_snake()
    test_collide()
    test_generate_item()
    test_pick_item()
