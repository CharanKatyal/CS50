# deep.py - By Charan Katyal

# Prompt user for input
userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Check and print
if userInput.strip().lower() in ['42', 'forty-two', 'forty two']:
	print("Yes")
else:
	print("No")
