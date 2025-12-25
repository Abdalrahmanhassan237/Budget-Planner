class Category:
    def __init__(self, name: str, limit: float):
        
        self.__name = name
        self.__limit = limit if limit > 0 else 0
        self.__spent = 0.0
    
    
    def get_name(self) -> str:
        """Return category name."""
        return self.__name
    
    def get_limit(self) -> float:
        """Return spending limit."""
        return self.__limit
    
    def get_spent(self) -> float:
        """Return amount spent."""
        return self.__spent
    
    def add_expense(self, amount: float) -> None:
        
        if amount > 0:
            self.__spent += amount
    
    def remaining(self) -> float:
        """Calculate remaining budget in category."""
        return self.__limit - self.__spent
    
    def is_over_budget(self) -> bool:
        """Check if spending exceeds limit."""
        return self.__spent > self.__limit
    
    def get_usage_percentage(self) -> float:
        """Calculate percentage of limit used."""
        if self.__limit == 0:
            return 0.0
        return (self.__spent / self.__limit) * 100
    
    def reset_spent(self) -> None:
        """Reset spent amount (for new month)."""
        self.__spent = 0.0
    
    def __str__(self) -> str:
        """String representation of category."""
        status = "OVER BUDGET!" if self.is_over_budget() else "✓"
        return (f"{self.get_name()}: ${self.get_spent():.2f} / ${self.get_limit():.2f} "
                f"({self.get_usage_percentage():.1f}%) {status}")