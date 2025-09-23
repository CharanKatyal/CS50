# test_bank.py - By Charan Katyal

import bank
from bank import value

def test_value_hello():
    # Test if greeting starts with "hello"
    assert value("hello") == 0
    assert value("HELLO") == 0  # Case-insensitive test
    assert value("Hello there") == 0

def test_value_h():
    # Test if greeting starts with "h" but not "hello"
    assert value("hi") == 20
    assert value("Happiness") == 20
    assert value("howdy") == 20
    assert value("H") == 20

def test_value_other():
    # Test if greeting doesn't start with "h" or "hello"
    assert value("Good morning") == 100
    assert value("Greetings") == 100
    assert value("Bye") == 100
    assert value("Zebra") == 100
