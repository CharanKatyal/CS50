import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            data = []
            for row in reader:
                name_parts = row["name"].split(", ")
                if len(name_parts) == 2:
                    last_name, first_name = name_parts[0], name_parts[1]
                else:
                    last_name = name_parts[0] # Fallback, might not be accurate
                    first_name = ""
                    if len(name_parts) > 1:
                        first_name = name_parts[1]

                data.append({
                    "first": first_name,
                    "last": last_name,
                    "house": row["house"]
                })

        with open(output_file, 'w', newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")
    except KeyError:
        sys.exit("Input file is missing expected columns (name, house)")


if __name__ == "__main__":
    main()
