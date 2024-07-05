import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: " , formatted_date)

def calculate_future_date(days):
    current_date = datetime.datetime.now().date()
    future_date = current_date + datetime.timedelta(days=days)
    print(f"Future date after {days} days: {future_date}")

def main():
    display_current_datetime()
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

if __name__ == "__main__":
    main()