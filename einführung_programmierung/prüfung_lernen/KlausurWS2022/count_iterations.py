def count_iterations(n: int, a: int) -> int:
    value = n
    add = 0
    rounds = 0
    while add < a:
        if value % 2 == 0:
            value = value / 2
            add += value
            rounds += 1
        else:
            value = 3 * value + 1
            add += value
            rounds += 1
    return rounds


print(count_iterations(7, 42))
