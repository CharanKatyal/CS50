def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if not (isinstance(x, int) and isinstance(y, int)):
                raise ValueError
            if x < 0 or y < 0:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()
