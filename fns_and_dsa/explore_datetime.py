import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time using datetime.now()
    current_date = datetime.datetime.now()
    
    # Print the current date and time in a readable format
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    # Get the current date
    current_date = datetime.datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + datetime.timedelta(days=days_to_add)
    
    # Print the future date in the format YYYY-MM-DD
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Get the number of days from the user
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(days_to_add)

if __name__ == "__main__":
    main()
