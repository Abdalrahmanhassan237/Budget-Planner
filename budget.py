from typing import List, Dict
from transaction import Transaction, Income, Expense
from category import Category


class Budget:
    
    def __init__(self, initial_balance: float = 0.0):
        
        self.__initial_balance = initial_balance
        self.__transactions: List[Transaction] = []
        self.__categories: Dict[str, Category] = {}
    
    def add_category(self, name: str, limit: float) -> None:
        if name in self.__categories:
            print(f"⚠ Category '{name}' already exists!")
            return
        
        self.__categories[name] = Category(name, limit)
        print(f"✓ Category '{name}' created with limit ${limit:.2f}")
    
    def category_exists(self, name: str) -> bool:
        """Check if category exists."""
        return name in self.__categories
    
    def add_transaction(self, transaction: Transaction) -> None:
        
        if isinstance(transaction, Expense):
            category_name = transaction.get_category()
            if not self.category_exists(category_name):
                print(f"⚠ Error: Category '{category_name}' does not exist!")
                print("Please create the category first.")
                return
            
            # Update category spending
            
            self.__categories[category_name].add_expense(transaction.get_amount())
        
        
        self.__transactions.append(transaction)
        print(f"✓ Transaction added: {transaction}")
    
    def calculate_balance(self) -> float:
        
        balance = self.__initial_balance
        
        # POLYMORPHISM: Each transaction type implements apply() differently
        for transaction in self.__transactions:
            balance = transaction.apply(balance)
        
        return balance
    
    def get_total_income(self) -> float:
        
        return sum(t.get_amount() for t in self.__transactions if isinstance(t, Income))
    
    def get_total_expenses(self) -> float:
        
        return sum(t.get_amount() for t in self.__transactions if isinstance(t, Expense))
    
    def generate_monthly_report(self) -> None:
        print("\n" + "="*60)
        print("📊 MONTHLY BUDGET REPORT")
        print("="*60)
        
        # Balance summary
        print(f"\n💰 BALANCE SUMMARY:")
        print(f"   Initial Balance:  ${self.__initial_balance:.2f}")
        print(f"   Total Income:     ${self.get_total_income():.2f}")
        print(f"   Total Expenses:   ${self.get_total_expenses():.2f}")
        print(f"   Current Balance:  ${self.calculate_balance():.2f}")
        
        # Category breakdown
        print(f"\n📁 CATEGORY BREAKDOWN:")
        if not self.__categories:
            print("   No categories created yet.")
        else:
            for category in self.__categories.values():
                print(f"   {category}")
        
        # Recent transactions
        print(f"\n📝 RECENT TRANSACTIONS ({len(self.__transactions)} total):")
        if not self.__transactions:
            print("   No transactions yet.")
        else:
            # Show last 10 transactions
            for transaction in self.__transactions[-10:]:
                print(f"   {transaction}")
        
        print("="*60 + "\n")
    
    def get_categories(self) -> List[str]:
        """Return list of category names."""
        return list(self.__categories.keys())