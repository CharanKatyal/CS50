import os
import csv
from datetime import date, timedelta
import pytest
from project import (
    load_habits,
    save_habits,
    add_habit,
    delete_habit,
    complete_habit,
    process_command,
    reset_habit,
    find_habit_by_identifier,
    list_habits,
)

TEST_FILE = "test_habits.csv"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Manages the test file before and after each test."""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


@pytest.fixture
def sample_habits():
    """Provides a standard set of habits for testing."""
    return [
        {"habit_name": "Read", "streak": 10, "longest_streak": 15, "last_completed_date": str(date.today())},
        {"habit_name": "Code", "streak": 5, "longest_streak": 5, "last_completed_date": str(date.today() - timedelta(days=2))},
        {"habit_name": "Walk the Dog", "streak": 20, "longest_streak": 25, "last_completed_date": str(date.today() - timedelta(days=1))},
    ]


# --- Test Core Logic --- #

def test_add_habit():
    habits = add_habit([], "Exercise")
    assert len(habits) == 1 and habits[0]["habit_name"] == "Exercise"

def test_add_duplicate_habit(capsys):
    habits = add_habit([{"habit_name": "Read", "streak": 1, "longest_streak": 1, "last_completed_date": "never"}], "Read")
    assert len(habits) == 1
    captured = capsys.readouterr()
    assert "already exists" in captured.out

def test_list_habits(capsys, sample_habits):
    list_habits(sample_habits)
    captured = capsys.readouterr()
    assert "[1] Read" in captured.out
    assert "[2] Code" in captured.out
    assert "[3] Walk the Dog" in captured.out

# --- Test find_habit_by_identifier --- #

def test_find_by_id(sample_habits):
    assert find_habit_by_identifier("1", sample_habits) == sample_habits[0]
    assert find_habit_by_identifier("3", sample_habits) == sample_habits[2]

def test_find_by_name(sample_habits):
    assert find_habit_by_identifier("Code", sample_habits) == sample_habits[1]
    assert find_habit_by_identifier("walk the dog", sample_habits) == sample_habits[2]

def test_find_by_invalid_id(sample_habits):
    assert find_habit_by_identifier("99", sample_habits) is None

def test_find_by_nonexistent_name(sample_habits):
    assert find_habit_by_identifier("Nonexistent", sample_habits) is None

# --- Test process_command with IDs --- #

def test_process_command_delete_by_id(sample_habits):
    habits = process_command(["delete", "2"], sample_habits)
    assert len(habits) == 2
    assert "Code" not in [h["habit_name"] for h in habits]

def test_process_command_complete_by_id(sample_habits):
    habits = process_command(["complete", "3"], sample_habits)
    assert habits[2]["streak"] == 21

def test_process_command_reset_by_id(sample_habits):
    habits = process_command(["reset", "1"], sample_habits)
    assert habits[0]["streak"] == 0

# --- Test process_command with Names (Regression) --- #

def test_process_command_delete_by_name(sample_habits, capsys):
    habits = process_command(["delete", "Read"], sample_habits)
    assert len(habits) == 2
    captured = capsys.readouterr()
    assert "Deleted habit: 'Read'" in captured.out

def test_process_command_complete_by_name(sample_habits):
    habits = process_command(["complete", "Walk the Dog"], sample_habits)
    assert habits[2]["streak"] == 21

def test_process_command_invalid_command(sample_habits, capsys):
    process_command(["unknown_command", "1"], sample_habits)
    captured = capsys.readouterr()
    assert "Invalid command" in captured.out

# --- Test Data Persistence --- #

def test_load_and_save_habits(sample_habits):
    save_habits(TEST_FILE, sample_habits)
    loaded = load_habits(TEST_FILE)
    assert loaded == sample_habits

def test_load_creates_file():
    assert load_habits(TEST_FILE) == []
    assert os.path.exists(TEST_FILE)
