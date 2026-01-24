import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        return False

    parts = ip.split(".")
    if len(parts) != 4:
        return False

    for part in parts:
        if len(part) > 1 and part.startswith("0"):
             return False
        if not 0 <= int(part) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
