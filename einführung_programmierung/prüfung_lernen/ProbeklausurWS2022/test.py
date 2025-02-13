#def s2_in_s1(s1: str, s2: str) -> bool:

def s2_in_s1(s1: str, s2: str):
    list = iter(s1)
    #list1 = iter(s2)
    for st in list:
        if all(st in s2 for st in list):
            return True
        else:
            return False


print(s2_in_s1("aaaa", "fn"))
