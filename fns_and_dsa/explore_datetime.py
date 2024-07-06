from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days} days:", formatted_future_date)

# Display the current date and time
display_current_datetime()

# Prompt the user to enter the number of days
days = int(input("Enter the number of days to add to the current date: "))

# Calculate and display the future date
calculate_future_date(days)
