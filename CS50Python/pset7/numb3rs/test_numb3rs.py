from numb3rs import validate

def test_alpha():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("a.b.c.d") == False
    assert validate("aa.bb.cc.dd") == False
    assert validate("Hello...") == False


def test_inrange():
    assert validate("1.1.1.1") == True
    assert validate("11.11.11.11") == True
    assert validate("111.111.111.111") == True
    assert validate("333.333.333.333") == False
    assert validate("123.123.123.123") == True
    assert validate("566.754.346.72") == False
    assert validate("-11.11.-11.11") == False
    assert validate("-11.11.11.11") == False
    assert validate("0.123.123.123") == True
    assert validate("255.123.123.123") == True
    assert validate("256.123.123.123") == False
    assert validate("-1.123.123.123") == False
    assert validate("123.333.333.333") == False



def test_format():
    assert validate("1.2") == False
    assert validate("198.0.0") == False
    assert validate("1,1,2.0") == False
    assert validate("123.234.111.222") == True
    assert validate("198:0:0;1") == False

if __name__ == "__main__":
    main()
