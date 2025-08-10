# twttr.py

def main():
    # Prompt the user for input
    text = input("Input: ")

    # Remove vowels from the text
    result = remove_vowels(text)

    # Output the modified text
    print(f"Output: {result}")

def remove_vowels(text):
    # Define vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"

    # Initialize an empty string for the result
    no_vowels = ""

    # Iterate through each character in the text
    for char in text:
        # If the character is not a vowel, add it to the result
        if char not in vowels:
            no_vowels += char

    return no_vowels

if __name__ == "__main__":
    main()
