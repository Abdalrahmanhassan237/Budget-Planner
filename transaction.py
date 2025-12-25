
from abc import ABC, abstractmethod
from datetime import datetime


class Transaction(ABC):
    
    def __init__(self, amount: float, date: str = None, note: str = ""):
        
        self.__amount = self._validate_amount(amount)
        self.__date = date if date else datetime.now().strftime("%Y-%m-%d")
        self.__note = note
    
    def _validate_amount(self, amount: float) -> float:
        """Validate that amount is positive."""
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        return amount
    
    # Getters for encapsulated attributes
    def get_amount(self) -> float:
        """Return the transaction amount."""
        return self.__amount
    
    def get_date(self) -> str:
        """Return the transaction date."""
        return self.__date
    
    def get_note(self) -> str:
        """Return the transaction note."""
        return self.__note
    
    @abstractmethod
    def apply(self, balance: float) -> float:
        """Apply transaction to balance and return new balance."""
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """Return the transaction type as a string."""
        pass
    
    def __str__(self) -> str:
        """String representation of transaction."""
        return f"[{self.get_date()}] {self.get_type()}: ${self.get_amount():.2f} - {self.get_note()}"


class Income(Transaction):
    
    def apply(self, balance: float) -> float:
        """
        Apply income to balance (increases it).
        Demonstrates POLYMORPHISM by overriding abstract method.
        """
        return balance + self.get_amount()
    
    def get_type(self) -> str:
        """Return transaction type."""
        return "INCOME"


class Expense(Transaction):

    
    def __init__(self, amount: float, category: str, date: str = None, note: str = ""):
        
        super().__init__(amount, date, note)
        
        self.__category = category
    
    def get_category(self) -> str:
        """Return the expense category."""
        return self.__category
    
    def apply(self, balance: float) -> float:
        return balance - self.get_amount()
    
    def get_type(self) -> str:
        """Return transaction type with category."""
        return f"EXPENSE ({self.get_category()})"