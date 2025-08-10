# faces.py - By Charan Katyal

def convert(text: str) -> str:
    # Replace emoticons with corresponding emoji
    text = text.replace(":)", "🙂")  # Happy face
    text = text.replace(":(", "🙁")  # Sad face
    return text

def main():
    # Prompt the user for input
    userInput = input("Please enter a sentence: ")
    # Call convert to replace emoticons with emoji
    result = convert(userInput)
    # Print the result
    print(result)

main()
