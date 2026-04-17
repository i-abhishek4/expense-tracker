from expense_manager import load_data
from datetime import datetime

def monthly_summary():
    data=load_data()

    if not data:
        print("No expenses found.")
        return

    month_input=input("Enter month and year (MM-YYYY):")

    total=0
    count=0

    for expense in data:
        try:
            expense_date=datetime.strptime(expense["date"], "%d-%m-%Y")
            formatted_date=expense_date.strftime("%m-%Y")

            if formatted_date==month_input:
                total+=expense["amount"]
                count+=1

        except ValueError:
            continue

    print(f"\nSummary for {month_input}:")
    print(f"Total Expenses :₹{total}")
    print(f"Number of Transactions :{count}")