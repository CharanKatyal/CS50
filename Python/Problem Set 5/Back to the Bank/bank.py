# bank.py - By Charan Katyal

def main():
    # Example of calling the value function and printing the result
    greeting = input("Enter a greeting: ")
    print(value(greeting))

def value(greeting):
    # Convert the greeting to lowercase for case-insensitive comparison
    greeting = greeting.lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
