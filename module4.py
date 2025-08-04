# Ask user for N (number of elements)
N = int(input("Enter the number of elements N: "))

# Read N numbers one by one and store them in a list
numbers = []
for i in range(N):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

# Ask user for X (number to search for)
X = int(input("Enter the number X to search for: "))

# Search for X in the list and find its index
result = -1
for i in range(N):
    if numbers[i] == X:
        result = i + 1  # Index from 1 to N (not 0 to N-1)
        break

# Output the result
print(result)