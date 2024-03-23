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


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    ...


def test_withdraw():
    ...
