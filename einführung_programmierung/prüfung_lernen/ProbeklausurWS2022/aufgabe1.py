def count_iterations(n: int, a: int) -> int:
    runs = 0
    while n < a:
        if n % 2 == 0:
            n = n // 2
            runs += 1
        else:
            n = 9 * n + 3
            runs += 1
    else:
        return runs


print(count_iterations(3, 100))
