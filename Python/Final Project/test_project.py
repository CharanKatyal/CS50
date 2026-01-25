import os
import csv
from datetime import date, timedelta
from project import load_habits, save_habits, add_habit, delete_habit, complete_habit

# Define a constant for the test file path to avoid magic strings
TEST_FILE = "test_habits.csv"


def setup_function():
    """ Fixture to set up a clean test file before each test. """
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def teardown_function():
    """ Fixture to clean up the test file after each test. """
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_load_habits_no_file():
    """ Test that load_habits creates a new file with headers if one doesn't exist. """
    habits = load_habits(TEST_FILE)
    assert os.path.exists(TEST_FILE)
    assert habits == []
    with open(TEST_FILE, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert header == ["habit_name", "streak", "longest_streak", "last_completed_date"]


def test_save_habits():
    """ Test that save_habits correctly writes data to the CSV file. """
    habits_to_save = [
        {"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": "2023-10-26"},
        {"habit_name": "Exercise", "streak": 10, "longest_streak": 15, "last_completed_date": "2023-10-27"}
    ]
    save_habits(TEST_FILE, habits_to_save)

    # Read the file back to verify its contents
    with open(TEST_FILE, 'r') as f:
        reader = csv.DictReader(f)
        loaded_habits = list(reader)
        # Convert numeric strings back to int for comparison
        for habit in loaded_habits:
            habit['streak'] = int(habit['streak'])
            habit['longest_streak'] = int(habit['longest_streak'])
        assert loaded_habits == habits_to_save


def test_add_habit_new():
    """ Test adding a completely new habit. """
    initial_habits = []
    new_habits = add_habit(initial_habits, "Go to bed by 11pm")
    assert len(new_habits) == 1
    assert new_habits[0]["habit_name"] == "Go to bed by 11pm"
    assert new_habits[0]["streak"] == 0
    assert new_habits[0]["longest_streak"] == 0
    assert new_habits[0]["last_completed_date"] == "never"


def test_add_habit_duplicate():
    """ Test that adding a duplicate habit (case-insensitive) is prevented. """
    initial_habits = [
        {"habit_name": "Drink water", "streak": 3, "longest_streak": 5, "last_completed_date": "2023-10-27"}
    ]
    # Try adding the same habit but with different casing
    new_habits = add_habit(initial_habits, "drink water")
    assert len(new_habits) == 1
    assert new_habits[0]["habit_name"] == "Drink water"

def test_delete_habit():
    """ Test deleting an existing habit. """
    initial_habits = [
        {"habit_name": "Read", "streak": 5, "longest_streak": 5, "last_completed_date": "2023-10-26"},
        {"habit_name": "Exercise", "streak": 10, "longest_streak": 15, "last_completed_date": "2023-10-27"}
    ]
    updated_habits = delete_habit(initial_habits, "Read")
    assert len(updated_habits) == 1
    assert updated_habits[0]["habit_name"] == "Exercise"

def test_complete_habit_and_longest_streak():
    """ Test that completing a habit updates the streak and longest_streak correctly. """
    yesterday = str(date.today() - timedelta(days=1))
    initial_habits = [
        {"habit_name": "Coding", "streak": 3, "longest_streak": 3, "last_completed_date": yesterday}
    ]

    # Continue the streak
    habits = complete_habit(initial_habits, "Coding")
    assert habits[0]["streak"] == 4
    assert habits[0]["longest_streak"] == 4

    # Break the streak
    habits[0]["last_completed_date"] = "2023-01-01" # A long time ago
    habits = complete_habit(habits, "Coding")
    assert habits[0]["streak"] == 1
    assert habits[0]["longest_streak"] == 4 # Longest streak should not change

