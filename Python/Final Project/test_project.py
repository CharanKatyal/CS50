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
)

# Define a constant for the test file path to avoid magic strings
TEST_FILE = "test_habits.csv"


def setup_function():
    """Fixture to set up a clean test file before each test."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def teardown_function():
    """Fixture to clean up the test file after each test."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_load_habits_no_file():
    """Test that load_habits creates a new file with the correct headers."""
    load_habits(TEST_FILE)  # This should create the file
    with open(TEST_FILE, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["habit_name", "streak", "longest_streak", "last_completed_date"]
    assert load_habits(TEST_FILE) == []


def test_save_habits():
    """Test that save_habits correctly writes data that load_habits can read."""
    habits_to_save = [
        {"habit_name": "Read", "streak": 5, "longest_streak": 10, "last_completed_date": "2023-10-26"},
        {"habit_name": "Exercise", "streak": 1, "longest_streak": 1, "last_completed_date": "2023-10-27"},
    ]
    save_habits(TEST_FILE, habits_to_save)
    loaded_habits = load_habits(TEST_FILE)
    assert loaded_habits == habits_to_save


def test_add_habit_new():
    """Test adding a new habit initializes it with correct default values."""
    habits = add_habit([], "Go to bed by 11pm")
    assert habits[0] == {
        "habit_name": "Go to bed by 11pm",
        "streak": 0,
        "longest_streak": 0,
        "last_completed_date": "never",
    }


def test_add_habit_duplicate():
    """Test that adding a case-insensitive duplicate habit is prevented."""
    initial_habits = [{"habit_name": "Drink water", "streak": 3, "longest_streak": 5, "last_completed_date": "2023-10-27"}]
    updated_habits = add_habit(initial_habits, "drink water")
    assert updated_habits == initial_habits


def test_delete_habit_existing():
    """Test deleting a habit that exists."""
    initial_habits = [{"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": "2023-10-26"}]
    updated_habits = delete_habit(initial_habits, "Read")
    assert len(updated_habits) == 0


def test_delete_habit_nonexistent():
    """Test that attempting to delete a nonexistent habit does not change the list."""
    initial_habits = [{"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": "2023-10-26"}]
    updated_habits = delete_habit(initial_habits, "Nonexistent Habit")
    assert updated_habits == initial_habits


def test_complete_habit_and_longest_streak():
    """Test completing a habit updates streak and longest_streak correctly."""
    yesterday = str(date.today() - timedelta(days=1))
    habits = [{"habit_name": "Coding", "streak": 3, "longest_streak": 3, "last_completed_date": yesterday}]
    
    # Continue streak, longest_streak should increase
    habits = complete_habit(habits, "Coding")
    assert habits[0]["streak"] == 4
    assert habits[0]["longest_streak"] == 4

    # Break streak, longest_streak should be preserved
    habits[0]["last_completed_date"] = "2023-01-01"
    habits = complete_habit(habits, "Coding")
    assert habits[0]["streak"] == 1
    assert habits[0]["longest_streak"] == 4


def test_complete_habit_already_completed():
    """Test completing a habit already completed today does not change its state."""
    today = str(date.today())
    initial_habits = [{"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": today}]
    updated_habits = complete_habit(initial_habits, "Read")
    assert updated_habits == initial_habits


def test_complete_habit_nonexistent():
    """Test that trying to complete a nonexistent habit does not change the list."""
    initial_habits = [{"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": "2023-10-26"}]
    updated_habits = complete_habit(initial_habits, "Nonexistent Habit")
    assert updated_habits == initial_habits

# Tests for the command processing logic

def test_process_command_add():
    """Test the 'add' command via the process_command function."""
    habits = process_command(["add", "New Habit"], [])
    assert len(habits) == 1 and habits[0]["habit_name"] == "New Habit"


def test_process_command_delete():
    """Test the 'delete' command via the process_command function."""
    initial_habits = [{"habit_name": "Old Habit", "streak": 1, "longest_streak": 1, "last_completed_date": "never"}]
    habits = process_command(["delete", "Old Habit"], initial_habits)
    assert len(habits) == 0


def test_process_command_invalid():
    """Test that an invalid command does not alter the habits list."""
    initial_habits = [{"habit_name": "My Habit", "streak": 1, "longest_streak": 1, "last_completed_date": "never"}]
    habits = process_command(["invalid_command", "My Habit"], initial_habits)
    assert habits == initial_habits
