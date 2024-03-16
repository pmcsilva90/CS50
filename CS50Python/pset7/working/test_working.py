from working import convert

def test_alpha():
    assert convert("cat") == False
    assert convert("dog") == False
    assert convert("a.b.c.d") == False
    assert convert("aa.bb.cc.dd") == False
    assert convert("Hello...") == False


def test_inrange():
    assert convert("08:30 PM to 12:43 AM") == True
    assert convert("07:31 PM to 11:26 AM") == True
    assert convert("10 AM to 4 PM") == True

    assert convert("11:82 AM to 07:47 AM") == False
    assert convert("13:08 PM to 04:29 PM") == 
    assert convert("") == False



def test_format():
    assert convert("1.2") == False
    assert convert("198.0.0") == False
    assert convert("1,1,2.0") == False
    assert convert("123.234.111.222") == True
    assert convert("198:0:0;1") == False

if __name__ == "__main__":
    main()
