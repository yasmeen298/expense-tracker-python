# Expense Tracker Project

expenses = [] #list of all expenses in form of dictionary
print("Welcome to Expense Tracker")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View all expenses")
    print("3. Exit")

    choice= int(input("Please enter your choice "))

# 1. ADD Expense 
    if(choice == 1):
        date= input("Spent on which date?: ")
        category= input("Category of expense? (Food, Travel, Makeup, Books): ")
        description= input("Add details: ") 
        try:
                #We "try"to convert the input to a float here
            amount = float(input("Enter The amount:"))
                #If the float conversion works, these lines will run:
            expense= {
                 "date": date,
                 "category": category,
                 "description": description,
                 "amount": amount
        }
            expenses.append(expense)
            print("DONE. Expense added successfully")
        except ValueError:
                #If the user types a letter instead of a number , Python jumps here:
             print("INVALID INPUT! PLEASE ENTER A NUMBER FOR THE AMOUNT.")

# 2. VIEW ALL EXPENSES
    if (choice == 2):
     if( len(expenses)==0 ):
            print("No Expenses Added.")
     else:
            print("===== This is your complete expense =====")
            count= 1
            for eachspend in expenses:
                print(f"Expense Number {count} -> {eachspend["date"]}, {eachspend["category"]}, {eachspend["description"]}, {eachspend["amount"]} ")
                count= count+1

# 3. EXIT
    if choice == 3:
         print("THANK YOU FOR USING")
         break    