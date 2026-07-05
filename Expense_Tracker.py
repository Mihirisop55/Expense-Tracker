# Expense tracker

import matplotlib.pyplot as plt
import pandas

Expense = []
Amount = []
Date = []
money=True

print("------ Expense Tracker -------")
print("1. Add New expense (press 1)")
print("2. View all expense (press 2)")
print("3. View summary (press 3)")
print("4. Get CSV file (press 4)")
print("5. Exit (press 5)")
print("------------------------------")
while money:
    try:
        reply = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        print("Please enter a valid choice")
    else:
        if reply<1 or reply>5:
            print("Invalid choice")
            print("Please enter a valid choice")
            print()
        elif reply==1:
            expense = input("Enter the expense: ")
            amount = int(input("Enter the amount: "))
            date = input("Enter the date (YYYY-MM-DD): ")
            Expense.append(expense)
            Amount.append(amount)
            Date.append(date)
            print("Your Expense has been added successfully")
            print()
        elif reply==2 and len(Expense)==0:
            print("Please add some expenses to use this feature")
            print()
        elif reply==2 and len(Expense)>0:
            data = {"Date": Date, "Expense": Expense, "Amount": Amount}
            df = pandas.DataFrame(data)
            print(df)
            print()
        elif reply==3 and len(Expense)==0:
            print("Please add some expenses to use this feature")
            print()
        elif reply==3 and len(Expense)>0:
            print("Here is a Pie Chart for your expenses")
            plt.pie(Amount, labels=Expense, autopct='%1.1f%%')
            plt.title("Expense Summary")
            plt.fontweight = 'bold'
            plt.show()
            print()
        elif reply==4 and len(Expense)==0:
            print("Please add some expenses to use this feature")
            print()
        elif reply==4 and len(Expense)>0:
            df = pandas.DataFrame({"Expense": Expense, "Amount": Amount, "Date": Date})
            df.to_csv("Expenses.csv", index=False)
            print("CSV file generated successfully")
            print()
        elif reply==5:
            print("Thank you for using the Expense Tracker")
            money=False
