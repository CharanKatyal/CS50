import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    if names:
        print("")
        print(f"Adieu, adieu, to {p.join(names)}")
    if not names:
        print("")
        print(f"Adieu, adieu, to yieu, yieu, and yieu")

if __name__ == "__main__":
    main()