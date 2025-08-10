# camel.py - By Charan Katyal

def main():
    # Prompt the user for input in camel case
    camel_case = input("camelCase: ")

    # Convert camel case to snake case
    snake_case = convert_to_snake_case(camel_case)

    # Output the result
    print(f"snake_case: {snake_case}")

def convert_to_snake_case(camel_case):
    # Initialize an empty string for the result
    snake_case = ""

    # Iterate over each character in the camel case string
    for char in camel_case:
        # If the character is uppercase, convert it to lowercase and prepend an underscore
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char

    return snake_case

if __name__ == "__main__":
    main()
