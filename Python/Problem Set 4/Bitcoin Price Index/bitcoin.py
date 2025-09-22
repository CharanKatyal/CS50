# bitcoin.py - By Charan Katyal

import sys
import requests

def main():
    # Check if a command-line argument was provided
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        # Try to convert the argument to a float
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        headers = {"Authorization": "Bearer 5b76f623d09ffe9560d1f025be4c285f58ad17fa4d597ff2e780ac6ad06cb7ae"}
        url = "https://rest.coincap.io/v3/assets/bitcoin"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")

    # Calculate total cost
    total = n * price

    # Print the result with formatting
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
