"""
module5_oop.py
Object-oriented program for number storage and search functionality.
"""

class NumberStorage:
    """
    A class to handle storage and search operations for a collection of numbers.
    """
    
    def __init__(self):
        """Initialize empty number storage."""
        self.numbers = []
    
    def initialize(self, n):
        """
        Initialize storage for n numbers.
        
        Args:
            n (int): Number of elements to store
        """
        self.numbers = []
        print(f"Storage initialized for {n} numbers.")
    
    def insert_number(self, number):
        """
        Insert a number into the storage.
        
        Args:
            number (int/float): Number to insert
        """
        self.numbers.append(number)
    
    def search_number(self, x):
        """
        Search for a number in the storage.
        
        Args:
            x (int/float): Number to search for
            
        Returns:
            int: Index (1-based) if found, -1 if not found
        """
        try:
            # Find the first occurrence and return 1-based index
            index = self.numbers.index(x)
            return index + 1  # Convert to 1-based indexing
        except ValueError:
            return -1  # Number not found
    
    def get_size(self):
        """
        Get the current size of storage.
        
        Returns:
            int: Number of elements in storage
        """
        return len(self.numbers)
    
    def display_numbers(self):
        """Display all stored numbers (for debugging purposes)."""
        print(f"Stored numbers: {self.numbers}")


def main():
    """Main program execution."""
    # Create NumberStorage instance
    storage = NumberStorage()
    
    # Get N from user
    while True:
        try:
            n = int(input("Enter N (positive integer): "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Initialize storage
    storage.initialize(n)
    
    # Read N numbers from user
    print(f"Please enter {n} numbers (one by one):")
    for i in range(n):
        while True:
            try:
                number = float(input(f"Enter number {i + 1}: "))
                storage.insert_number(number)
                break
            except ValueError:
                print("Please enter a valid number.")
    
    # Get X from user to search
    while True:
        try:
            x = float(input("Enter X (number to search): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Search for X and output result
    result = storage.search_number(x)
    print(result)


if __name__ == "__main__":
    main()
