expenses = []

print("Welcome to Expense Tracker 💰")

while True:
    print("\n======= MENU =======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Spending by Category")
    print("5. Exit")
    print("=====================")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        print("\n--- Add New Expense ---")
        date = input("Enter date (DD-MM-YYYY): ").strip()
        category = input("Enter category (Food, Travel, Shopping, etc.): ").strip()
        description = input("Enter short description: ").strip()
        
        try:
            amount = float(input("Enter amount ($): "))
        except ValueError:
            print("❌ Invalid amount! Please enter a valid number.")
            continue
            
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        
        expenses.append(expense)
        print("✅ Expense added successfully!")
        
    elif choice == "2":
        if len(expenses) == 0:
            print("\n⚠ No expenses recorded yet.")
        else:
            print("\n--- All Expenses ---")
            print(f"{'S.No':<6} | {'Date':<12} | {'Category':<15} | {'Description':<20} | {'Amount ($)':<10}")
            print("-" * 75)
            
            serial_num = 1
            for item in expenses:
                print(f"{serial_num:<6} | {item['date']:<12} | {item['category']:<15} | {item['description']:<20} | ${item['amount']:<10.2f}")
                serial_num += 1
            print("-" * 75)
            
    elif choice == "3":
        if len(expenses) == 0:
            print("\n⚠ No expenses recorded yet.")
        else:
            total_spending = 0
            for item in expenses:
                total_spending += item["amount"]
            print(f"\n💰 Total Spending = ${total_spending:.2f}")
            
    elif choice == "4":
        if len(expenses) == 0:
            print("\n⚠ No expenses recorded yet.")
        else:
            category_summary = {}
            
            for item in expenses:
                cat = item["category"]
                if cat in category_summary:
                    category_summary[cat] += item["amount"]
                else:
                    category_summary[cat] = item["amount"]
            
            print("\n📊 Spending by Category:")
            print("-" * 35)
            for cat, amt in category_summary.items():
                print(f"{cat:<15}: ${amt:<10.2f}")
            print("-" * 35)
            
    elif choice == "5":
        print("\n👋 Thanks for using Expense Tracker! Goodbye!")
        break
        
    else:
        print("\n❌ Invalid choice! Please select a number between 1 and 5.")