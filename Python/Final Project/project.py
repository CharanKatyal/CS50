import sys
import csv
import os
from datetime import date, timedelta

FILEPATH = "habits.csv"

def main():
    """Main function to run the habit tracker CLI."""
    if len(sys.argv) > 1 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print_help()
        sys.exit(0)

    load_habits(FILEPATH)
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
            habits = process_command(args, habits)
            save_habits(FILEPATH, habits)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Saving habits... Goodbye!")
            save_habits(FILEPATH, habits)
            break

def process_command(args, habits):
    """Processes a single command and returns the updated habits list."""
    command = args[0].lower()
    identifier = args[1] if len(args) > 1 else None

    # Define valid commands
    commands_with_no_args = {"list", "stats", "reminders", "help"}
    commands_with_name_arg = {"add"}
    commands_with_id_or_name_arg = {"complete", "delete", "reset"}

    # Validate the command first
    if command not in commands_with_no_args | commands_with_name_arg | commands_with_id_or_name_arg:
        print(f"Invalid command: '{command}'. Type 'help' for available commands.")
        return habits

    # Process commands
    if command == 'help':
        print_help()
    elif command == 'list':
        list_habits(habits)
    elif command == 'stats':
        show_analytics(habits)
    elif command == 'reminders':
        show_reminders(habits)
    elif command == 'add':
        if not identifier:
            print("The 'add' command requires a habit name.")
        else:
            return add_habit(habits, identifier)
    elif command in commands_with_id_or_name_arg:
        if not identifier:
            print(f"Command '{command}' requires a habit name or ID.")
            return habits
        
        target_habit = find_habit_by_identifier(identifier, habits)
        if not target_habit:
            print(f"Habit '{identifier}' not found.")
            return habits

        habit_name = target_habit["habit_name"]
        if command == "complete":
            return complete_habit(habits, habit_name)
        elif command == "delete":
            return delete_habit(habits, habit_name)
        elif command == "reset":
            return reset_habit(habits, habit_name)

    return habits

def find_habit_by_identifier(identifier, habits):
    """Finds a habit by its 1-based ID or case-insensitive name."""
    try:
        habit_id = int(identifier)
        if 1 <= habit_id <= len(habits):
            return habits[habit_id - 1]
    except ValueError:
        for habit in habits:
            if habit["habit_name"].lower() == identifier.lower():
                return habit
    return None

def print_help():
    """Prints the help message with available commands."""
    print("Usage: python project.py [command] [argument]")
    print("\nCommands:")
    print("  list                 - Show all habits with their IDs.")
    print("  stats                - Display habit analytics.")
    print("  reminders            - Show habits not completed today.")
    print("  add <habit name>     - Create a new habit.")
    print("  complete <id|name>   - Mark a habit as done for today.")
    print("  delete <id|name>     - Remove a habit.")
    print("  reset <id|name>      - Reset a habit's streak to 0.")
    print("  help, -h, --help     - Display this help message.")
    print("  (no arguments)       - Run in interactive mode.")
    print("\nIn interactive mode, type 'exit' to save and quit.")

def list_habits(habits):
    """Prints a formatted list of all habits with their 1-based ID."""
    print("\n--- Your Habits ---")
    if not habits:
        print("You haven't added any habits yet. Use 'add <habit name>' to start.")
    else:
        for i, habit in enumerate(habits):
            print(f"[{i + 1}] {habit['habit_name']} | Streak: {habit['streak']} | Longest: {habit['longest_streak']}")
    print("-------------------\n")

def show_reminders(habits):
    """Prints habits that have not been completed today."""
    today_str = str(date.today())
    pending_habits = [h for h in habits if h["last_completed_date"] != today_str]
    print("\n--- Pending Habits for Today ---")
    if not pending_habits:
        print("Great job! All habits completed for today.")
    else:
        for i, habit in enumerate(pending_habits):
            original_index = habits.index(habit)
            print(f"[{original_index + 1}] {habit['habit_name']}")
    print("--------------------------------\n")

def reset_habit(habits, name):
    """Resets a habit's streak to 0 by name."""
    for habit in habits:
        if habit["habit_name"].lower() == name.lower():
            habit["streak"] = 0
            print(f"Streak for '{name}' has been reset to 0.")
            return habits
    print(f"Habit '{name}' not found.")
    return habits

def show_analytics(habits):
    """Calculates and displays habit statistics."""
    if not habits:
        print("No habits to analyze.")
        return
    total_habits = len(habits)
    longest_current_streak_habit = max(habits, key=lambda x: x.get("streak", 0), default=None)
    best_longest_streak_habit = max(habits, key=lambda x: x.get("longest_streak", 0), default=None)
    print("\n--- Habit Analytics ---")
    print(f"Total habits tracked: {total_habits}")
    if longest_current_streak_habit:
        print(f"Longest current streak: '{longest_current_streak_habit['habit_name']}' ({longest_current_streak_habit['streak']} days)")
    if best_longest_streak_habit:
        print(f"Best all-time streak: '{best_longest_streak_habit['habit_name']}' ({best_longest_streak_habit['longest_streak']} days)")
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
    """Deletes a habit by name."""
    initial_len = len(habits)
    habits = [h for h in habits if h["habit_name"].lower() != name.lower()]
    if len(habits) < initial_len:
        print(f"Deleted habit: '{name}'")
    else:
        print(f"Habit '{name}' not found.")
    return habits

def complete_habit(habits, name):
    """Marks a habit as complete for today by name."""
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
            if habit["streak"] > habit['longest_streak']:
                habit['longest_streak'] = habit['streak']
            habit["last_completed_date"] = today_str
            print(f"Good work! Streak for '{name}' is now {habit['streak']}.")
            return habits
    print(f"Habit '{name}' not found.")
    return habits

if __name__ == "__main__":
    main()
