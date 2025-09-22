# test_twttr.py - By Charan Katyal

from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("h3ll0") == "h3ll0"

def test_punctuation():
    assert shorten("c@t!") == "c@t!"

def test_all_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_empty_string():
    assert shorten("") == ""
