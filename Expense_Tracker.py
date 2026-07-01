# Expense tracker

import matplotlib.pyplot as plt
import pandas

Expense = []
Amount = []
money=True

print("---- Expense Tracker ----")
print("1. Add New expense (press 1)")
print("2. View all expense (press 2)")
print("3. View summary (press 3)")
print("4. Exit (press 4)")
while money:
    try:
        reply = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        print("Please enter a valid choice")
    else:
        if reply<1 or reply>4:
            print("Invalid choice")
            print("Please enter a valid choice")
        elif reply==1:
            expense = input("Enter the expense: ")
            amount = int(input("Enter the amount: "))
            Expense.append(expense)
            Amount.append(amount)
            print("Your Expense has been added successfully")
        elif reply==2:
            data = {"Expense": Expense, "Amount": Amount}
            df = pandas.DataFrame(data)
            print(df)
        elif reply==3:
            print("Here is a Pie Chart for your expenses")
            plt.pie(Amount, labels=Expense, autopct='%1.1f%%')
            plt.title("Expense Summary")
            plt.show()
        elif reply==4:
            print("Thank you for using the Expense Tracker")
            money=False
