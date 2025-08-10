# meal.py - By Charan Katyal

def main():
    # Prompt the user for time input
    time = input("What time is it? ")

    # Convert the time to a float representing hours
    time_in_hours = convert(time)

    # Check if the time is within any meal time range
    if 7.0 <= time_in_hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_hours <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_hours <= 19.0:
        print("dinner time")

def convert(time):
    # Split the time string into hours and minutes
    hours, minutes = time.split(":")

    # Convert hours and minutes to integers
    hours = int(hours)
    minutes = int(minutes)

    # Convert time to float representation (e.g., 7:30 -> 7.5)
    return hours + minutes / 60.0

if __name__ == "__main__":
    main()
