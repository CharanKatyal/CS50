# HabitCLI
#### Video Demo:  <URL HERE>

#### Description:
This is a command-line application for tracking daily habits. It's built with Python and is designed to be simple, fast, and easy to use directly from your terminal.

## Overview

The Habit Tracker CLI helps you build new habits and monitor your progress over time. You can add, complete, and delete habits. The tracker will monitor your "streaks" (consecutive days a habit is completed) and celebrate your progress.

The application can be run in two modes:
1.  **Single Command Mode**: Execute a specific command and the program exits.
2.  **Interactive Mode**: Enter a loop that allows you to run multiple commands.

## Features

- **Add, Delete, and Complete Habits**: The core functions for managing your habits.
- **Streak Tracking**: Automatically tracks your current streak and your all-time longest streak for each habit.
- **Habit Analytics**: The `stats` command provides an overview of your progress, including your best-performing habits.
- **Daily Reminders**: The `reminders` command shows you which habits are still pending for the day.
- **ID-based Commands**: Use a simple numeric ID (e.g., `complete 1`) to interact with habits quickly.
- **Data Persistence**: All habit data is stored locally in a `habits.csv` file.
- **Robust Error Handling**: The application provides clear feedback for invalid commands or arguments.

## Usage

To use the tracker, navigate to the project directory and run the `project.py` script.

### Interactive Mode

For a continuous session, run the script without any arguments:
```bash
python project.py
```
You will be welcomed by the interactive prompt, where you can type commands. To exit, type `exit`.

### Single Command Mode

To execute a single command, provide it as an argument:
```bash
python project.py list
python project.py add "Read for 15 minutes"
python project.py complete 1
```

## Commands

The application uses a simple command structure: `[command] [argument]`

| Command              | Alias    | Description                                       | Example                               |
| -------------------- | -------- | ------------------------------------------------- | ------------------------------------- |
| **`list`**           |          | Show all habits, their streaks, and their IDs.    | `list`                                |
| **`stats`**          |          | Display habit analytics and progress.             | `stats`                               |
| **`reminders`**      |          | Show habits not yet completed today.              | `reminders`                           |
| **`add`**            |          | Create a new habit.                               | `add "Go for a run"`                  |
| **`complete`**       |          | Mark a habit as done for today.                   | `complete 1` or `complete "Go for a run"` |
| **`delete`**         |          | Remove a habit from your list.                    | `delete 2` or `delete "Drink water"`  |
| **`reset`**          |          | Reset a habit's streak to zero.                   | `reset 3` or `reset "Meditate"`       |
| **`help`**           | `-h`, `--help` | Display the help message with all commands.       | `help`                                |
| **`exit`**           |          | (Interactive Mode Only) Save changes and exit.    | `exit`                                |


## Data Storage

Your habit data is stored in a `habits.csv` file in the same directory as the script. This file is created automatically if it doesn't exist. You can view or even edit this file directly, but be careful not to corrupt the data format.

**Columns:**
- `habit_name`: The name of the habit.
- `streak`: The current number of consecutive days the habit has been completed.
- `longest_streak`: The all-time longest streak for that habit.
- `last_completed_date`: The date the habit was last marked as complete.
