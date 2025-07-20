# daily_reminder.py

# Prompt for a single task
Task = input("Enter your task for today: ").strip()

# Prompt for task priority
Priority = input("Enter the priority level (high, medium, low): ").strip()

# Ask if the task is time-bound
Time_bound = input("Is the task time-bound? (yes/no): ").strip()

# Process the task based on priority using match-case
match priority:
    case "high":
        reminder = f"Your HIGH priority task: '{Task}'"
    case "medium":
        reminder = f"Your medium priority task: '{Task}'"
    case "low":
        reminder = f"Your low priority task: '{Task}'"
    case _:
        reminder = f"Your task: '{Task}' (Priority not recognized)"

# Modify reminder if the task is time-bound
if Time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Print the customized reminder
print(reminder)
