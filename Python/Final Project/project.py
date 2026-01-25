import sys
import csv
import os
from datetime import date, timedelta

FILEPATH = "habits.csv"

def main():
    """
    Main function to run the habit tracker CLI.
    Parses commands: list, add, complete, delete.
    """
    # Ensure the habits file exists before any operation
    load_habits(FILEPATH)

    args = sys.argv[1:]
    command = args[0] if args else "list" # Default to 'list' if no command is given

    habits = load_habits(FILEPATH)

    if command == "add" and len(args) > 1:
        habit_name = args[1]
        habits = add_habit(habits, habit_name)
        print(f"Added habit: '{habit_name}'")

    elif command == "complete" and len(args) > 1:
        habit_name = args[1]
        habits = complete_habit(habits, habit_name)
    
    elif command == "delete" and len(args) > 1:
        habit_name = args[1]
        habits = delete_habit(habits, habit_name)

    elif command == "list":
        list_habits(habits)

    else:
        sys.exit("Usage: python project.py [add|complete|delete|list] [habit_name]")

    save_habits(FILEPATH, habits)


def load_habits(filepath):
    """
    Loads habits from the CSV file. If the file doesn't exist, it's created.
    Returns a list of habit dictionaries.
    """
    if not os.path.exists(filepath):
        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["habit_name", "streak", "longest_streak", "last_completed_date"])
        return []

    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        # Convert numeric strings to integers
        habits_list = []
        for row in reader:
            row['streak'] = int(row['streak']) if 'streak' in row else 0
            row['longest_streak'] = int(row['longest_streak']) if 'longest_streak' in row else 0
            habits_list.append(row)
        return habits_list


def save_habits(filepath, habits):
    """
    Saves the list of habits back to the CSV file.
    """
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["habit_name", "streak", "longest_streak", "last_completed_date"])
        writer.writeheader()
        writer.writerows(habits)


def add_habit(habits, name):
    """
    Adds a new habit to the list, avoiding duplicates.
    Returns the updated list of habits.
    """
    for habit in habits:
        if habit["habit_name"].lower() == name.lower():
            print(f"Habit '{name}' already exists.")
            return habits # Return original list if duplicate
    habits.append({"habit_name": name, "streak": 0, "longest_streak": 0, "last_completed_date": "never"})
    return habits

def delete_habit(habits, name):
    """
    Deletes a habit from the list.
    Returns the updated list of habits.
    """
    habit_to_delete = None
    for habit in habits:
        if habit["habit_name"].lower() == name.lower():
            habit_to_delete = habit
            break
    
    if habit_to_delete:
        habits.remove(habit_to_delete)
        print(f"Deleted habit: '{name}'")
    else:
        print(f"Habit '{name}' not found.")
        
    return habits

def complete_habit(habits, name):
    """
    Marks a habit as complete for today, updating its streak and longest_streak.
    Returns the updated list of habits.
    """
    today = date.today()
    yesterday = today - timedelta(days=1)
    habit_found = False

    for habit in habits:
        if habit["habit_name"].lower() == name.lower():
            habit_found = True
            last_completed = habit["last_completed_date"]

            if last_completed == str(today):
                print(f"'{name}' already completed today.")
                break

            current_streak = int(habit["streak"])
            if last_completed == str(yesterday):
                habit["streak"] = current_streak + 1
            else:
                habit["streak"] = 1
            
            # Update the longest streak if the current streak is greater
            if habit["streak"] > habit["longest_streak"]:
                habit["longest_streak"] = habit["streak"]

            print(f"Good work! Streak for '{name}' is now {habit['streak']}.")

            habit["last_completed_date"] = str(today)
            break

    if not habit_found:
        print(f"Habit '{name}' not found.")

    return habits


def list_habits(habits):
    """
    Prints a formatted list of all habits and their current streaks.
    """
    print("\n--- Your Habits ---")
    if not habits:
        print("You haven't added any habits yet. Use 'add [habit_name]' to start.")
    else:
        for habit in habits:
            print(f"- {habit['habit_name']} | Streak: {habit['streak']} | Longest Streak: {habit['longest_streak']}")
    print("-------------------\n")


if __name__ == "__main__":
    main()
