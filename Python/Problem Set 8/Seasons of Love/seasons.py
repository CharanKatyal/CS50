import inflect
import sys
from datetime import date

def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    today = date.today()
    minutes = calculate_minutes(today, birth_date)
    words = convert_to_words(minutes)
    print(f"{words.capitalize()} minutes")

def calculate_minutes(today, birth_date):
    delta = today - birth_date
    return delta.days * 24 * 60

def convert_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number, andword="")

if __name__ == "__main__":
    main()
