import json
import os
from datetime import datetime

PATH ="data/expenses.json"

def load_data():
    if not os.path.exists(PATH):
        return []
    
    with open(PATH,"r") as file:
        return json.load(file)

def save_data(data):
    with open(PATH,"w") as file:
        json.dump(data,file,indent=4)

def add_expense():
    while True:
        date_input=input("Enter date(DD-MM-YYYY):")
        try:
            date_obj=datetime.strptime(date_input,"%d-%m-%Y")
            date=date_obj.strftime("%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format.Please use DD-MM-YYYY.")
    category=input("Enter category:")
    amount=float(input("Enter amount:"))
    description=input("Enter description:")

    expense={
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    data=load_data()
    data.append(expense)
    save_data(data)

    print("Expense added successfully!")

def view_expenses():
    data=load_data()

    if not data:
        print("No expenses found.")
        return

    print("\n---All Expenses---")

    for i, expense in enumerate(data, start=1):
        print(f"\nExpense {i}:")
        print(f"Date       :{expense['date']}")
        print(f"Category   :{expense['category']}")
        print(f"Amount     :₹{expense['amount']}")
        print(f"Description:{expense['description']}")