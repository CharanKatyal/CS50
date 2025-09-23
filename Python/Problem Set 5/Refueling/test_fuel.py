# test_fuel.py - By Charan Katyal

import fuel
import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("0/1") == 0
    assert convert("100/100") == 100

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/2.5")
    with pytest.raises(ValueError):
        convert("2/1")  # x > y
    with pytest.raises(ValueError):
        convert("3/")
    with pytest.raises(ValueError):
        convert("/4")
    with pytest.raises(ValueError):
        convert("-1/2")  # Negative numerator
    with pytest.raises(ValueError):
        convert("1/-2")  # Negative denominator

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_edges():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"

