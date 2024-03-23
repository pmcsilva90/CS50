from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar._capacity == 12
    assert jar._size == 0

    jar1 = Jar(14, 2)
    assert jar1._capacity == 14
    assert jar1._size == 2

    with pytest.raises(ValueError):
        jar2 = Jar(10, 11)

    with pytest.raises(ValueError):
        jar3 = Jar(10, -1)

    with pytest.raises(ValueError):
        jar4 = Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar._size == 4
    jar.deposit(4)
    assert jar._size == 8

    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar(6, 4)

    jar.withdraw(1)
    assert jar._size == 3

    jar.withdraw(2)
    assert jar._size == 1

    with pytest.raises(ValueError):
        jar.withdraw(3)
