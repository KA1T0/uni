def all(lst: list[bool]) -> bool:
    for i in lst:
        if not i:
            return False
    return True


if __name__ == "__main__":
    print(all([]))
    print(all([True, False, True, False]))
