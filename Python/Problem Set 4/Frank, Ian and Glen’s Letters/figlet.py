# figlet.py - By Charan Katyal

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    # Check if the user has provided arguments
    if len(sys.argv) == 1:
        # No arguments: Use random font
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        # Two arguments: The first must be -f or --font, second is the font name
        if sys.argv[1] not in ['-f', '--font']:
            sys.exit("Error: The first argument must be '-f' or '--font'.")
        
        font = sys.argv[2]
        # Check if the provided font is valid
        if font not in figlet.getFonts():
            sys.exit(f"Error: '{font}' is not a valid font.")
    else:
        # Incorrect number of arguments
        sys.exit("Usage: python figlet.py [-f or --font FONT_NAME]")

    # Ask the user for input text
    text = input("Enter text to render in ASCII art: ")

    # Set the font and render the text
    figlet.setFont(font=font)
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
