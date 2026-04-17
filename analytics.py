from expense_manager import load_data
from datetime import datetime
import matplotlib.pyplot as plt

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

def category_analysis():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    category_totals={}

    for expense in data:
        category=expense["category"]
        amount=expense["amount"]

        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount

    print("\n---Category-wise Spending---")

    for category,total in category_totals.items():
        print(f"{category} : ₹{total}")

    
    max_category = max(category_totals, key=category_totals.get)

    print(f"\nHighest Spending Category: {max_category}")
    print(f"Amount Spent: ₹{category_totals[max_category]}")

    total_spending = sum(category_totals.values())

    for category,total in category_totals.items():
        percentage=(total/total_spending)*100

        if percentage>40:
            print(f"High spending on {category} ({percentage:.1f}%)")

def generate_pie_chart():
    data = load_data()

    if not data:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in data:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Category-wise Spending")
    plt.show()