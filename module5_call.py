"""
module5_call.py
Main program that uses the NumberStorage class from module5_mod.py
"""

from module5_mod import NumberStorage


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
