import sys

def main():
    """
    Main function to handle command-line arguments and count lines of code.
    """
    check_arguments()

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    code_lines = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            code_lines += 1

    print(code_lines)


def check_arguments():
    """
    Checks for the correct number of command-line arguments and file type.
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
