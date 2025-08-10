# tip.py - By Charan Katyal

def main():
    dollars = dollars_to_float(input("How much was the meal: "))
    percent = percent_to_float(input("What percentage would you like to tip: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove the '$' and convert the remaining string to a float
    return float(d.strip('$'))


def percent_to_float(p):
    # Remove the '%' and convert the remaining string to a float, then divide by 100
    return float(p.strip('%')) / 100

main()
