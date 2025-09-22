# twttr.py - By Charan Katyal

def shorten(word):
    vowels = "aeiouAEIOU"
    return "".join(char for char in word if char not in vowels)

def main():
    word = input("Input: ")
    print("Output:", shorten(word))

if __name__ == "__main__":
    main()

