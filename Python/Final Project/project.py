import sys
import csv
import os
from datetime import date, timedelta

FILEPATH = "habits.csv"

def main():
    """
    Main function to run the habit tracker CLI.
    """
    load_habits(FILEPATH)  # Ensure file exists

    if len(sys.argv) > 1:
        habits = load_habits(FILEPATH)
        updated_habits = process_command(sys.argv[1:], habits)
        save_habits(FILEPATH, updated_habits)
    else:
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
                save_habits(FILEPATH, habits)
                break
            
            if command == "help":
                print_help()
                continue

            habits = process_command(args, habits)
            # Save after every action in interactive mode
            save_habits(FILEPATH, habits)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Saving habits... Goodbye!")
            save_habits(FILEPATH, habits)
            break

def process_command(args, habits):
    """Processes a single command and returns the updated habits list."""
    command = args[0].lower()
    habit_name = args[1] if len(args) > 1 else None

    if command == "add" and habit_name:
        return add_habit(habits, habit_name)
    elif command == "complete" and habit_name:
        return complete_habit(habits, habit_name)
    elif command == "delete" and habit_name:
        return delete_habit(habits, habit_name)
    elif command == "reset" and habit_name:
        return reset_habit(habits, habit_name)
    elif command == "list":
        list_habits(habits)
    elif command == "stats":
        show_analytics(habits)
    elif command == "reminders":
        show_reminders(habits)
    else:
        print(f"Invalid command: '{command}'. Type 'help' for available commands.")
    
    return habits

def print_help():
    """Prints the help message with available commands."""
    print("\nCommands:")
    print("  list                 - Show all habits and their streaks.")
    print("  stats                - Display habit analytics.")
    print("  reminders            - Show habits not completed today.")
    print("  add <habit>          - Create a new habit.")
    print("  complete <habit>     - Mark a habit as done for today.")
    print("  delete <habit>     - Remove a habit.")
    print("  reset <habit>        - Reset a habit's streak to 0.")
    print("  help                 - Display this help message.")
    print("  exit                 - Save and exit the tracker.\n")

def show_reminders(habits):
    """Prints habits that have not been completed today."""
    today_str = str(date.today())
    pending_habits = [h for h in habits if h["last_completed_date"] != today_str]

    print("\n--- Pending Habits for Today ---")
    if not pending_habits:
        print("Great job! All habits completed for today.")
    else:
        for habit in pending_habits:
            print(f"- {habit['habit_name']}")
    print("--------------------------------\n")

def reset_habit(habits, name):
    """Resets the streak of a specific habit to 0."""
    habit_found = False
    for habit in habits:
        if habit["habit_name"].lower() == name.lower():
            habit["streak"] = 0
            print(f"Streak for '{name}' has been reset to 0.")
            habit_found = True
            break
    
    if not habit_found:
        print(f"Habit '{name}' not found.")
        
    return habits


def show_analytics(habits):
    """Calculates and displays habit statistics."""
    if not habits:
        print("No habits to analyze. Add some habits first!")
        return

    total_habits = len(habits)
    longest_current_streak_habit = max(habits, key=lambda x: x["streak"])
    best_longest_streak_habit = max(habits, key=lambda x: x["longest_streak"])

    print("\n--- Habit Analytics ---")
    print(f"Total habits tracked: {total_habits}")
    print(f"Habit with longest current streak: '{longest_current_streak_habit['habit_name']}' ({longest_current_streak_habit['streak']} days)")
    print(f"Habit with best all-time streak: '{best_longest_streak_habit['habit_name']}' ({best_longest_streak_habit['longest_streak']} days)")
    print("-----------------------\n")

def load_habits(filepath):
    """Loads habits from the CSV file."""
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
    """Saves the list of habits back to the CSV file."""
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["habit_name", "streak", "longest_streak", "last_completed_date"])
        writer.writeheader()
        writer.writerows(habits)

def add_habit(habits, name):
    """Adds a new habit, avoiding duplicates."""
    if any(h["habit_name"].lower() == name.lower() for h in habits):
        print(f"Habit '{name}' already exists.")
        return habits
    habits.append({"habit_name": name, "streak": 0, "longest_streak": 0, "last_completed_date": "never"})
    print(f"Added habit: '{name}'")
    return habits

def delete_habit(habits, name):
    """Deletes a habit."""
    initial_len = len(habits)
    habits = [h for h in habits if h["habit_name"].lower() != name.lower()]
    if len(habits) < initial_len:
        print(f"Deleted habit: '{name}'")
    else:
        print(f"Habit '{name}' not found.")
    return habits

def complete_habit(habits, name):
    """Marks a habit as complete for today."""
    today_str = str(date.today())
    yesterday_str = str(date.today() - timedelta(days=1))
    
    for habit in habits:
        if habit["habit_name"].lower() == name.lower():
            if habit["last_completed_date"] == today_str:
                print(f"'{name}' already completed today.")
                return habits

            if habit["last_completed_date"] == yesterday_str:
                habit["streak"] += 1
            else:
                habit["streak"] = 1

            if habit["streak"] > habit["longest_streak"]:
                habit["longest_streak"] = habit["streak"]

            habit["last_completed_date"] = today_str
            print(f"Good work! Streak for '{name}' is now {habit['streak']}.")
            return habits

    print(f"Habit '{name}' not found.")
    return habits

def list_habits(habits):
    """Prints a formatted list of all habits."""
    print("\n--- Your Habits ---")
    if not habits:
        print("You haven't added any habits yet. Use 'add [habit_name]' to start.")
    else:
        for habit in habits:
            print(f"- {habit['habit_name']} | Streak: {habit['streak']} | Longest Streak: {habit['longest_streak']}")
    print("-------------------\n")

if __name__ == "__main__":
    main()
