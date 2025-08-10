# coke.py - By Charan Katyal

def main():
    # The price of a Coke bottle
    price = 50
    amount_inserted = 0

    # Loop until the user has inserted enough money
    while amount_inserted < price:
        # Print the amount due
        print(f"Amount Due: {price - amount_inserted}")

        # Prompt the user to insert a coin
        coin = int(input("Insert Coin: "))

        # Check if the coin is a valid denomination
        if coin in [25, 10, 5]:
            # Add the coin to the total inserted amount
            amount_inserted += coin
        else:
            # Ignore invalid coin and keep asking
            print("Invalid coin. Please insert a valid coin.")

    # Calculate the change to be returned
    change_owed = amount_inserted - price
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
