# daily_reminder.py

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high":
        base_msg = f"'{task}' is a high priority task"
    case "medium":
        base_msg = f"'{task}' is a medium priority task"
    case "low":
        base_msg = f"'{task}' is a low priority task"
    case _:
        base_msg = f"'{task}' has an unrecognized priority"

if time_bound == "yes":
    print(f"Reminder: {base_msg} that requires immediate attention today!")
else:
    print(f"Note: {base_msg}. Consider completing it when you have free time.")
