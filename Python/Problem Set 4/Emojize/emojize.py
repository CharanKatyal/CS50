# emojize.py - By Charan Katyal

import emoji

def main():
    # Get input from the user
    user_input = input("Input: ")

    # Convert emoji codes and aliases to emoji characters and print the output
    print("Output:", emoji.emojize(user_input, language='alias'))

if __name__ == "__main__":
    main()

