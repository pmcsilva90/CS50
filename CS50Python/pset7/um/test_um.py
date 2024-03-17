from um import count

def main():
    test_inwords()
    test_spaces()
    test_case()

def test_inwords():
    assert count("album") == 0
    assert count("Do you play the drums?") == 0
    assert count("Hello, um friend") == 1
    assert count("123um") == 0
    assert count("??um??") == 1


def test_spaces():
    assert count("Hello, um... name?") == 1
    assert count("Do you require um, space?") == 1
    assert count("Just um a bit") == 1


def test_case():
    assert count("WHY ARE WE, UM, YELLING?") == 1
    assert count("Um, I don't know") == 1
    assert count("I'll yell, uM, JUST A BIT") == 1

if __name__ == "__main__":
    main()

