# bank.py - By Charan Katyal

# Prompt the user for a greeting
greeting = input("Enter a greeting: ").strip().lower()

# Check the conditions and output the appropriate amount
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
