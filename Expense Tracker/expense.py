expenses = []
while True:
 print("1. Add Expense")
 print("2. View Expenses")
 print("3. Total Spending")
 print("4. Highest Expense")
 print("5. Exit")

 choice = input("Enter Choice: ")

 if choice == "1":
  for i in range(3):
        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        expenses.append([category, amount])

        print("Expense Added Successfully!")

 elif choice == "2":

        print("All Expenses:")

        for expense in expenses:
            print(expense)

 elif choice == "3":

        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total Spending:", total)

 elif choice == "4":

        if len(expenses) == 0:
            print("No Expenses Found")

        else:

            amounts = []

            for expense in expenses:
                amounts.append(expense[1])

            print("Highest Expense:", max(amounts))


 elif choice == "5":

    print("Thank You")
    break

 else:

    print("Invalid Choice")

