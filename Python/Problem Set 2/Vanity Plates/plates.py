# plates.py - By Charan Katyal

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    
    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    found_number = False
    for char in s:
        if char.isdigit():
            if not found_number and char == '0':
                return False
            found_number = True
        elif found_number:
            return False

    return True

if __name__ == "__main__":
    main()