import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            table_data = list(reader)
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
