from expense_manager import add_expense,view_expenses

def menu():
    print("\nExpense Tracker")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Monthly Summary")
    print("4.Category Analysis")
    print("5.Exit")

while True:
    menu()
    choice=input("Enter your choice:")

    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        print("Monthly Summary selected")
    elif choice=="4":
        print("Category Analysis selected")
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.Try again.")