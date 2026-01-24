from seasons import calculate_minutes, convert_to_words
from datetime import date


def test_calculate_minutes():
    today = date(2023, 10, 27)
    birth_date = date(2022, 10, 27)
    assert calculate_minutes(today, birth_date) == 525600


def test_convert_to_words():
    assert convert_to_words(525600) == "five hundred twenty-five thousand, six hundred"
