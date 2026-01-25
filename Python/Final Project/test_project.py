import os
import csv
from datetime import date, timedelta
from project import (
    load_habits,
    save_habits,
    add_habit,
    delete_habit,
    complete_habit,
    process_command,
    show_analytics,
    show_reminders, # Import new functions
    reset_habit,
)

# Define a constant for the test file path
TEST_FILE = "test_habits.csv"

def setup_function():
    """Set up a clean test file before each test."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def teardown_function():
    """Clean up the test file after each test."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

# ... (previous tests remain unchanged) ...

def test_show_analytics(capsys):
    """Test the analytics display."""
    habits = [
        {"habit_name": "Read", "streak": 10, "longest_streak": 15, "last_completed_date": "2023-10-27"},
        {"habit_name": "Code", "streak": 20, "longest_streak": 20, "last_completed_date": "2023-10-27"},
    ]
    show_analytics(habits)
    captured = capsys.readouterr()
    assert "Total habits tracked: 2" in captured.out
    assert "longest current streak: 'Code' (20 days)" in captured.out

# New tests for reminders and reset

def test_show_reminders(capsys):
    """Test that reminders for uncompleted habits are shown correctly."""
    today_str = str(date.today())
    habits = [
        {"habit_name": "Read", "streak": 1, "longest_streak": 1, "last_completed_date": today_str},
        {"habit_name": "Write", "streak": 2, "longest_streak": 2, "last_completed_date": "2023-10-26"},
    ]
    show_reminders(habits)
    captured = capsys.readouterr()
    assert "- Write" in captured.out
    assert "- Read" not in captured.out

def test_show_reminders_all_completed(capsys):
    """Test the reminders display when all habits are completed."""
    today_str = str(date.today())
    habits = [{"habit_name": "Read", "streak": 1, "longest_streak": 1, "last_completed_date": today_str}]
    show_reminders(habits)
    captured = capsys.readouterr()
    assert "All habits completed" in captured.out

def test_reset_habit():
    """Test that a habit's streak can be reset to 0."""
    habits = [{"habit_name": "Meditate", "streak": 10, "longest_streak": 15, "last_completed_date": "2023-10-27"}]
    updated_habits = reset_habit(habits, "Meditate")
    assert updated_habits[0]["streak"] == 0
    assert updated_habits[0]["longest_streak"] == 15 # Longest streak should not change

def test_reset_habit_nonexistent():
    """Test that trying to reset a nonexistent habit doesn't change the list."""
    initial_habits = [{"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": "2023-10-26"}]
    updated_habits = reset_habit(initial_habits, "Nonexistent Habit")
    assert updated_habits == initial_habits

def test_process_command_reminders(capsys):
    """Test the 'reminders' command via the process_command function."""
    habits = [{"habit_name": "Exercise", "streak": 1, "longest_streak": 1, "last_completed_date": "never"}]
    process_command(["reminders"], habits)
    captured = capsys.readouterr()
    assert "- Exercise" in captured.out

def test_process_command_reset():
    """Test the 'reset' command via the process_command function."""
    habits = [{"habit_name": "Journal", "streak": 7, "longest_streak": 7, "last_completed_date": "2023-10-27"}]
    updated_habits = process_command(["reset", "Journal"], habits)
    assert updated_habits[0]["streak"] == 0

# (Keep all other existing tests)

def test_load_habits_no_file():
    """Test that load_habits creates a new file with the correct headers."""
    load_habits(TEST_FILE)
    with open(TEST_FILE, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["habit_name", "streak", "longest_streak", "last_completed_date"]
    assert load_habits(TEST_FILE) == []

def test_save_habits():
    """Test saving and loading habits."""
    habits_to_save = [
        {"habit_name": "Read", "streak": 5, "longest_streak": 10, "last_completed_date": "2023-10-26"},
    ]
    save_habits(TEST_FILE, habits_to_save)
    loaded_habits = load_habits(TEST_FILE)
    assert loaded_habits == habits_to_save

def test_add_habit_new():
    """Test adding a new habit."""
    habits = add_habit([], "New Habit")
    assert habits[0]["habit_name"] == "New Habit"

def test_delete_habit_existing():
    """Test deleting an existing habit."""
    habits = [{"habit_name": "Old Habit", "streak": 1, "longest_streak": 1, "last_completed_date": "never"}]
    habits = delete_habit(habits, "Old Habit")
    assert len(habits) == 0

def test_complete_habit_and_streak():
    """Test completing a habit updates streak and longest_streak."""
    yesterday = str(date.today() - timedelta(days=1))
    habits = [{"habit_name": "Coding", "streak": 3, "longest_streak": 3, "last_completed_date": yesterday}]
    habits = complete_habit(habits, "Coding")
    assert habits[0]["streak"] == 4 and habits[0]["longest_streak"] == 4

def test_process_command_add():
    """Test the 'add' command processor."""
    habits = process_command(["add", "Test Habit"], [])
    assert len(habits) == 1 and habits[0]["habit_name"] == "Test Habit"
