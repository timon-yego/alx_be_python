#Personal Daily Reminder
#Prompt the user for a task description
task = input("Enter your task: ")

#Prompt for the task’s priority 
priority = input("Priority (high/medium/low):")

#prompt the user for the time sensitivity of the task
time_bound = input("Is it time-bound? (yes/no):")

#Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: 'task' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention soon.")
        else:
            priny(f"Reminder: '{task}' is a medium priority task.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: 'task' is a low priority task thet should be done when possible.")
        else:
            print(f"Note: 'task' is a low priority task. Consider completing it when you have free time..")

    case _:
        print(f"Error: Invalid priority level. Please enter high, medium, or low.")

