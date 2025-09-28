from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

display_current_datetime()

# Prompt user for number of days
number_of_days = int(input("Enter the number of days to add to the current date: "))

# Part 2: Calculate future date
def calculate_future_date():
    current_date = datetime.now()                      # current date variable
    add_days = timedelta(days=number_of_days)          # duration to add
    future_date = current_date + add_days              # calculate future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

calculate_future_date()
