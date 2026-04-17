import json
import os

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
    date=input("Enter date(YYYY-MM-DD):")
    category=input("Enter category:")
    amount=float(input("Enter amount:"))
    description=input("Enter description:")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    data = load_data()
    data.append(expense)
    save_data(data)

    print("Expense added successfully!")