import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_extensions = [".jpg", ".jpeg", ".png"]

    # Validate input file extension
    input_ext = os.path.splitext(input_path)[1].lower()
    if input_ext not in valid_extensions:
        sys.exit("Invalid input")

    # Validate output file extension
    output_ext = os.path.splitext(output_path)[1].lower()
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")

    # Check if input and output extensions match
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        # Open shirt image
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size

        # Open input image
        photo = Image.open(input_path)

        # Resize and crop the input photo to fit the shirt
        # ImageOps.fit crops and resizes to the exact dimensions
        # 'method', 'bleed', 'centering' default values are used
        photo = ImageOps.fit(photo, shirt_size)

        # Paste the shirt onto the resized photo
        # The second 'shirt' acts as a mask, using its alpha channel
        photo.paste(shirt, shirt)

        # Save the result
        photo.save(output_path)

    except FileNotFoundError:
        sys.exit("Input does not exist")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
