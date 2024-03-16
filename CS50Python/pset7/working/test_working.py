from working import convert

def test_alpha():
    assert convert("cat") == False
    assert convert("dog") == False
    assert convert("a.b.c.d") == False
    assert convert("aa.bb.cc.dd") == False
    assert convert("Hello...") == False


def test_inrange():
    assert convert("1.1.1.1") == True
    assert convert("11.11.11.11") == True
    assert convert("111.111.111.111") == True
    assert convert("333.333.333.333") == False
    assert convert("123.123.123.123") == True
    assert convert("566.754.346.72") == False



def test_format():
    assert convert("1.2") == False
    assert convert("198.0.0") == False
    assert convert("1,1,2.0") == False
    assert convert("123.234.111.222") == True
    assert convert("198:0:0;1") == False

if __name__ == "__main__":
    main()
