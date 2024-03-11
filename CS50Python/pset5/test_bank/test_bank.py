from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLlO") == 0
    assert value("hElLo") == 0
    assert value("Hello, friend!") == 0
    assert value("Hello!!1!1") == 0


def test_h():
    assert value("hey") == 20
    assert value("HEY") == 20
    assert value("Hi") == 20
    assert value("hI") == 20
    assert value("Hi, friend!") == 20
    assert value("Heeeyyy!!1!11|") == 20
    assert value("Hola") == 20
    assert value("HOLA, qUe Tal¿¿¿???") == 20
    assert value("How are you today?") == 20
    assert value("henlo frend") == 20


def test_else():
    assert value("Good morning!") == 100
    assert value("Good afternoon") == 100
    assert value("COMO ESTÁS") == 100
    assert value("TuDo BEmm?") == 100
    assert value("BueNas!!1'!|") == 100

if __name__ == "__main__":
    main()
