"""
module5_mod.py
Module containing the NumberStorage class for number storage and search operations.
"""

class NumberStorage:
    """
    A class to handle storage and search operations for a collection of numbers.
    
    This class provides functionality to:
    - Initialize storage for a specific number of elements
    - Insert numbers into the storage
    - Search for numbers and return their position
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
