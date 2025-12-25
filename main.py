from budget import Budget
from transaction import Income, Expense


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("💰 BUDGET PLANNER")
    print("="*50)
    print("1. Add category")
    print("2. Add income")
    print("3. Add expense")
    print("4. Show balance")
    print("5. Show monthly report")
    print("6. Exit")
    print("="*50)


def get_float_input(prompt: str) -> float:
    """Get validated float input from user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("⚠ Please enter a positive number!")
                continue
            return value
        except ValueError:
            print("⚠ Invalid input! Please enter a number.")


def main():
    """Main program loop."""
    print("\n🎉 Welcome to Budget Planner!")
    
    # Initialize budget
    try:
        initial = float(input("Enter your initial balance (or 0): $"))
        budget = Budget(initial)
    except ValueError:
        print("Invalid input. Starting with $0.00")
        budget = Budget(0.0)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            # Add category
            name = input("Enter category name: ").strip()
            if not name:
                print("⚠ Category name cannot be empty!")
                continue
            
            limit = get_float_input(f"Enter monthly limit for '{name}': $")
            budget.add_category(name, limit)
        
        elif choice == "2":
            # Add income
            amount = get_float_input("Enter income amount: $")
            note = input("Enter description (optional): ").strip()
            
            try:
                income = Income(amount, note=note)
                budget.add_transaction(income)
            except ValueError as e:
                print(f"⚠ Error: {e}")
        
        elif choice == "3":
            # Add expense
            categories = budget.get_categories()
            if not categories:
                print("⚠ No categories available! Please create a category first.")
                continue
            
            print("\nAvailable categories:")
            for i, cat in enumerate(categories, 1):
                print(f"  {i}. {cat}")
            
            cat_choice = input("Enter category number: ").strip()
            try:
                cat_index = int(cat_choice) - 1
                if cat_index < 0 or cat_index >= len(categories):
                    print("⚠ Invalid category number!")
                    continue
                category = categories[cat_index]
            except ValueError:
                print("⚠ Invalid input!")
                continue
            
            amount = get_float_input("Enter expense amount: $")
            note = input("Enter description (optional): ").strip()
            
            try:
                expense = Expense(amount, category, note=note)
                budget.add_transaction(expense)
            except ValueError as e:
                print(f"⚠ Error: {e}")
        
        elif choice == "4":
            # Show balance
            print(f"\n💰 Current Balance: ${budget.calculate_balance():.2f}")
        
        elif choice == "5":
            # Show monthly report
            budget.generate_monthly_report()
        
        elif choice == "6":
            # Exit
            print("\n👋 Thank you for using Budget Planner!")
            print("💡 Remember to track your spending regularly!")
            break
        
        else:
            print("⚠ Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()