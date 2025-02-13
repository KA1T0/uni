# Aufgabe 3 (Strings) #########################################################

def s2_in_s1(s1: str, s2: str) -> bool:
    for i in s2:
        if i in s1:
            print("true")
            return True
        else:
            print("false")
            return False
    else:
        return False


#def split_text(text):



# Tests  ######################################################################
if __name__ == "__main__":
    assert s2_in_s1("function", "fn") is True
    assert s2_in_s1("function", "ufnction") is False
    assert s2_in_s1("function", "fnn") is True
    assert s2_in_s1("function", "fcc") is False

    #assert split_text("You're a lizard, Harry!") == [
    #    'You', "'", 're', ' ', 'a', ' ', 'lizard', ', ', 'Harry', '!'
    #]
   # assert split_text("Luke! I'm your father!!") == [
    #    'Luke', '! ', 'I', "'", 'm', ' ', 'your', ' ', 'father', '!!'
   # ]
    #assert split_text("*Stay away from her, you $!#@!*") == [
    #    '*', 'Stay', ' ', 'away', ' ', 'from', ' ', 'her', ', ', 'you', ' $!#@!*'
   # ]
    #assert split_text("hello world") == ["hello", " ", "world"]