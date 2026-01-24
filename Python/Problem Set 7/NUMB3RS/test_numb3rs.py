from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_range():
    assert validate("275.3.6.28") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False

def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat") == False

def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.02.03.04") == False
