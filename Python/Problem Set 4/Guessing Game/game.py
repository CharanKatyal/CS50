# game.py - By Charan Katyal

import random

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

def main():
    # Step 1: Prompt the user for the level
    level = get_level()
    
    # Step 2: Generate a random number between 1 and level
    secret_number = random.randint(1, level)
    
    # Step 3: Keep prompting for guesses until the correct one is entered
    while True:
        guess = get_guess()
        
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
