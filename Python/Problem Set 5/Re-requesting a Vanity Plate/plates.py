# plates.py - By Charan Katyal

import sys

def is_valid(s: str) -> bool:
    if len(s) < 2 or len(s) > 6:
        return False
    
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    number_start_index = None
    for i, char in enumerate(s):
        if char.isdigit():
            number_start_index = i
            break
    
    if number_start_index is not None:
        if s[number_start_index] == '0':
            return False
        for c in s[number_start_index:]:
            if not c.isdigit():
                return False
    
    if not s.isalnum():
        return False
    
    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        sys.exit(1)


if __name__ == "__main__":
    main()
