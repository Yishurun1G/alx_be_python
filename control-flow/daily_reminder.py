# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ").strip()

# Prompt for task priority
priority = input("Priority (high/medium/low): ").strip().lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to determine base reminder message
match priority:
    case "high":
        base_msg = f"'{task}' is a high priority task"
    case "medium":
        base_msg = f"'{task}' is a medium priority task"
    case "low":
        base_msg = f"'{task}' is a low priority task"
    case _:
        base_msg = f"'{task}' has an unrecognized priority"

# Modify message based on time sensitivity
if time_bound == "yes":
    reminder = f"Reminder: {base_msg} that requires immediate attention today!"
else:
    reminder = f"Note: {base_msg}. Consider completing it when you have free time."

# Print the customized reminder
print(reminder)

