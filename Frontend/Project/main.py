expensesList = []
print(" Welcome to Expense Tracker : Try to Spend Less ")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice= int(input("Please enter your choice :"))
    
    if(choice==1):
        date= input("Date of expenses:")
        category= input("Type of expenses: (Food,Travel,Books,Tea,Ladki bagi,Books):")
        description= input(" Give More Details:")
        amount= float(input("Enter the Amount:"))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print(" \n Done bro. Expenses added Succesfully")

    elif(choice == 2):
        if (len(expensesList) ==0):  
            print("No Expenses Added. go and spend your money.")
        else:
            print("==== This is your All Expenses====")
            count=1
            for eachkharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachkharcha["date"]}, {eachkharcha["category"]},{eachkharcha["description"]}, {eachkharcha ["amount"]}")
                count+=1

    elif(choice == 3):
        total = 0
        for eachkharcha in expensesList:
            total = total + eachkharcha ["amount"]   

        print("\n Total expenses = ", total) 


    elif(choice == 4):
        print("Thankyou for Using My Website ")
        break
    else:
        print("Invalid Choice Try Again")               





       

