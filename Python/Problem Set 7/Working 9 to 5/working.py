import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s):
        start_hour, start_min, start_ampm, end_hour, end_min, end_ampm = match.groups()

        if start_min and not (0 <= int(start_min) < 60):
            raise ValueError("Invalid minute")
        if end_min and not (0 <= int(end_min) < 60):
            raise ValueError("Invalid minute")

        start_hour, end_hour = int(start_hour), int(end_hour)
        if not (1 <= start_hour <= 12 and 1 <= end_hour <= 12):
            raise ValueError("Invalid hour")

        # Convert to 24-hour format
        if start_ampm == "PM" and start_hour != 12:
            start_hour += 12
        if start_ampm == "AM" and start_hour == 12:
            start_hour = 0

        if end_ampm == "PM" and end_hour != 12:
            end_hour += 12
        if end_ampm == "AM" and end_hour == 12:
            end_hour = 0

        start_min = start_min or "00"
        end_min = end_min or "00"

        return f"{start_hour:02}:{start_min} to {end_hour:02}:{end_min}"

    raise ValueError("Invalid format")


if __name__ == "__main__":
    main()
