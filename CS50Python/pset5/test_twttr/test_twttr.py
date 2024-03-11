from twttr import shorten


def test_shorten():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("My name is...") == "My nm s..."
    assert shorten("12345") == "12345"
    assert shorten("ALL IN CAPSLOCK") == "LL N CPSLCK"
    assert shorten("L33t 5p34k") == "L33t 5p34k"
    assert shorten("This is CS50") == "Ths s CS50"


if __name__ == "__main__":
    main()
