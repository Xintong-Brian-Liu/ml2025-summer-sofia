# Assignment #4.2: GitHub and Python Introduction

## Overview
This assignment introduces basic Python programming concepts and GitHub repository management. You'll create a simple Python program that demonstrates user input handling and array operations.

## Prerequisites
- A GitHub account (create one at [github.com](https://github.com) if you don't have one)

## Tasks

### 1. Repository Setup
- Create a new **public** repository named `ml2025-summer-sofia` on GitHub

### 2. Python Program Development
Create a Python program (`module4.py`) that implements the following functionality:

#### Program Requirements:
1. **Input N**: Prompt the user to enter a positive integer N
2. **Input Numbers**: Ask the user to provide N numbers one by one
3. **Input X**: Ask the user to enter an integer X
4. **Output**: 
   - Return `-1` if X is not found among the N numbers
   - Return the **1-based index** of X if it exists in the previously entered numbers

#### Technical Notes:
- Use the `input()` function for all user input
- Handle the numbers as a sequence (array/list)
- Index counting starts from 1 (not 0)

### 3. File Submission
- Name your Python file `module4.py`
- Upload it to your `ml2025-summer-sofia` repository

## Example Usage
```
Enter a positive integer N: 3
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter integer X to search: 20
Output: 2
```

---

# Assignment #5: Object-Oriented Programming (OOP) in Python

## Overview
This assignment extends the previous module by implementing the same functionality using Object-Oriented Programming principles. You'll create Python programs that demonstrate proper class design and modular programming.

## Tasks

### 1. Single-File OOP Implementation (`module5_oop.py`)
Create a Python program that implements the number storage and search functionality using OOP:

#### Requirements:
- **Class-Based Design**: All data processing should be handled by a custom class
- **Core Methods**: 
  - Data initialization
  - Data insertion (one number at a time)
  - Data search functionality
- **Same User Interface**: Program should behave identically to `module4.py`
- **Error Handling**: Include input validation and error handling

#### Class Structure:
```python
class NumberStorage:
    def __init__(self):
        # Initialize storage
        
    def initialize(self, n):
        # Prepare storage for n numbers
        
    def insert_number(self, number):
        # Add a number to storage
        
    def search_number(self, x):
        # Search for x, return 1-based index or -1
```

### 2. Modular Implementation
Create a modular version split into two files:

#### `module5_mod.py`
- Contains **only** the `NumberStorage` class definition
- No main execution code
- Well-documented class with docstrings

#### `module5_call.py`
- Contains the main program logic
- Imports and uses the `NumberStorage` class from `module5_mod.py`
- Handles all user interaction

### 3. File Organization
Your repository should contain:
```
ml2025-summer-sofia/
├── module4.py          # Original procedural implementation
├── module5_oop.py      # Single-file OOP implementation
├── module5_mod.py      # Class module
├── module5_call.py     # Main program using the module
└── README.md           # This file
```

## Example Usage
Both OOP implementations should produce identical output:

```
Enter N (positive integer): 3
Storage initialized for 3 numbers.
Please enter 3 numbers (one by one):
Enter number 1: 10
Enter number 2: 20
Enter number 3: 30
Enter X (number to search): 20
2
```

```
Enter N (positive integer): 4
Storage initialized for 4 numbers.
Please enter 4 numbers (one by one):
Enter number 1: 5
Enter number 2: 15
Enter number 3: 25
Enter number 4: 35
Enter X (number to search): 100
-1
```

## Submission
Upload all files (`module5_oop.py`, `module5_mod.py`, `module5_call.py`) to your existing `ml2025-summer-sofia` repository.
