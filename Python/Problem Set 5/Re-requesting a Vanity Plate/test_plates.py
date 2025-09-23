# test_plates.py - By Charan Katyal

import plates
from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS123") == True
    assert is_valid("AB1234") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("1CS50") == False
    assert is_valid("C1S50") == False
    assert is_valid("1A234") == False
    assert is_valid("9ABC") == False
    assert is_valid("A1") == False

def test_invalid_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS5A") == False
    assert is_valid("CS5 0") == False
    assert is_valid("CS!50") == False

def test_only_letters():
    assert is_valid("CSIDE") == True
