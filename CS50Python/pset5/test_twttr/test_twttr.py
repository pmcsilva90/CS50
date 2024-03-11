from twttr import shorten

def test_shorten():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("My name is...") == "My nm s..."









if __name__ == "__main__":
    main()
