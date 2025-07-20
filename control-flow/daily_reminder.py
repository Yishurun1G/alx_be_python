# daily_reminder.py

# Prompt for a single task
task = input("Enter your task for today: ").strip()

# Prompt for task priority
priority = input("Enter the priority level (high, medium, low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"Your HIGH priority task: '{task}'"
    case "medium":
        reminder = f"Your medium priority task: '{task}'"
    case "low":
        reminder = f"Your low priority task: '{task}'"
    case _:
        reminder = f"Your task: '{task}' (priority not recognized)"

# Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the customized reminder
print(reminder)
