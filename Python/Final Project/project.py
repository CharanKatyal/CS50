import sys
import csv
import os
from datetime import date, timedelta

FILEPATH = "habits.csv"

def main():
    """
    Main function to run the habit tracker CLI.
    Runs in argument-based mode or interactive mode.
    """
    load_habits(FILEPATH)  # Ensure file exists before any operations

    if len(sys.argv) > 1:
        # If arguments are passed, run in single-command mode
        habits = load_habits(FILEPATH)
        updated_habits = process_command(sys.argv[1:], habits)
        save_habits(FILEPATH, updated_habits)
    else:
        # Otherwise, run in interactive mode
        run_interactive_mode()

def run_interactive_mode():
    """Runs the habit tracker in a continuous interactive loop."""
    print("\n--- Welcome to Your Interactive Habit Tracker ---")
    print_help()
    habits = load_habits(FILEPATH)

    while True:
        try:
            user_input = input("> ").strip()
            if not user_input:
                continue

            args = user_input.split(maxsplit=1)
            command = args[0].lower()

            if command == "exit":
                print("Saving habits... Goodbye!")
                break
            
            if command == "help":
                print_help()
                continue

            habits = process_command(args, habits)
            save_habits(FILEPATH, habits) # Save after each action

        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Saving habits... Goodbye!")
            save_habits(FILEPATH, habits)
            break

def process_command(args, habits):
    """Processes a single command and returns the updated habits list."""
    command = args[0].lower()
    habit_name = args[1] if len(args) > 1 else None

    if command == "add" and habit_name:
        habits = add_habit(habits, habit_name)
    elif command == "complete" and habit_name:
        habits = complete_habit(habits, habit_name)
    elif command == "delete" and habit_name:
        habits = delete_habit(habits, habit_name)
    elif command == "list":
        list_habits(habits)
    else:
        print(f"Invalid command: '{command}'. Type 'help' for available commands.")
    
    return habits

def print_help():
    """Prints the help message with available commands."""
    print("\nCommands:")
    print("  list               - Show all habits and their streaks.")
    print("  add <habit name>   - Create a new habit.")
    print("  complete <habit name>- Mark a habit as done for today.")
    print("  delete <habit name>  - Remove a habit.")
    print("  help               - Display this help message.")
    print("  exit               - Save and exit the tracker.\n")

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
        habits_list = []
        for row in reader:
            row['streak'] = int(row.get('streak', 0) or 0)
            row['longest_streak'] = int(row.get('longest_streak', 0) or 0)
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
            return habits
    habits.append({"habit_name": name, "streak": 0, "longest_streak": 0, "last_completed_date": "never"})
    print(f"Added habit: '{name}'")
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
                return habits

            current_streak = int(habit["streak"])
            if last_completed == str(yesterday):
                habit["streak"] = current_streak + 1
            else:
                habit["streak"] = 1
            
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
