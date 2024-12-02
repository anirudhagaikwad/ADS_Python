"""
print Statement: Used for outputting messages to the console.
input Function: Captures user input.
Data Types: float is used for numeric input to handle decimal values.
String Interpolation: f"..." is used to format strings for user-friendly output.
"""

# Print a welcome message
print("Welcome to Python Programming!")

# Input: Take user input
name = input("What is your name? ")

# Output: Print a greeting message
print(f"Hello, {name}! Let's do a simple computation.")

# Perform a simple computation
# Input: Take two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compute the sum
sum_result = num1 + num2

# Output: Display the result
print(f"The sum of {num1} and {num2} is {sum_result}.")


"""
Data Types:
Examples include int, float, string, bool, list, tuple, set, and dict.
type() shows the data type of a variable.
Operators:
Arithmetic Operators: Perform basic math operations.
Comparison Operators: Compare two values.
Logical Operators: Combine conditions (and, or, not).
Bitwise Operators: Operate at the binary level (&, |, ^, ~, <<, >>).
"""

# Demonstrating Python Data Types
print("Data Types in Python:")

# Integer
int_var = 10
print(f"Integer: {int_var} | Type: {type(int_var)}")

# Float
float_var = 20.5
print(f"Float: {float_var} | Type: {type(float_var)}")

# String
string_var = "Hello, Python!"
print(f"String: '{string_var}' | Type: {type(string_var)}")

# Boolean
bool_var = True
print(f"Boolean: {bool_var} | Type: {type(bool_var)}")

# List
list_var = [1, 2, 3, 4, 5]
print(f"List: {list_var} | Type: {type(list_var)}")

# =======================
# List Manipulations
# =======================
list_var = [1, 2, 3, 4, 5]
print("=== List Manipulations ===")
print(f"Original List: {list_var}")

# Adding elements
list_var.append(6)
print(f"After append(6): {list_var}")

list_var.extend([7, 8])
print(f"After extend([7, 8]): {list_var}")

list_var.insert(2, 99)
print(f"After insert(2, 99): {list_var}")

# Removing elements
list_var.remove(3)
print(f"After remove(3): {list_var}")

popped = list_var.pop(1)
print(f"After pop(1) (removed {popped}): {list_var}")

# Sorting and reversing
list_var.sort()
print(f"After sort(): {list_var}")

list_var.reverse()
print(f"After reverse(): {list_var}")

# Tuple
tuple_var = (10, 20, 30)
print(f"Tuple: {tuple_var} | Type: {type(tuple_var)}")
# =======================
# Tuple Manipulations
# =======================
tuple_var = (10, 20, 30)
print("\n=== Tuple Manipulations ===")
print(f"Original Tuple: {tuple_var}")

# Accessing elements
print(f"Element at index 1: {tuple_var[1]}")

# Concatenating tuples
new_tuple = tuple_var + (40, 50)
print(f"After concatenation with (40, 50): {new_tuple}")

# Tuple unpacking
a, b, c = tuple_var
print(f"Unpacked values: a={a}, b={b}, c={c}")

# Set
set_var = {1, 2, 3, 4}
print(f"Set: {set_var} | Type: {type(set_var)}")
# =======================
# Set Manipulations
# =======================
set_var = {1, 2, 3, 4}
print("\n=== Set Manipulations ===")
print(f"Original Set: {set_var}")

# Adding elements
set_var.add(5)
print(f"After add(5): {set_var}")

# Removing elements
set_var.discard(2)
print(f"After discard(2): {set_var}")

# Set operations
set_var_2 = {3, 4, 5, 6}
union_set = set_var.union(set_var_2)
print(f"Union with {set_var_2}: {union_set}")

intersection_set = set_var.intersection(set_var_2)
print(f"Intersection with {set_var_2}: {intersection_set}")

difference_set = set_var.difference(set_var_2)
print(f"Difference with {set_var_2}: {difference_set}")

# Dictionary
dict_var = {"name": "Anirudha", "age": 25}
print(f"Dictionary: {dict_var} | Type: {type(dict_var)}")

# =======================
# Dictionary Manipulations
# =======================
dict_var = {"name": "Anirudha", "age": 25}
print("\n=== Dictionary Manipulations ===")
print(f"Original Dictionary: {dict_var}")

# Adding and updating
dict_var["city"] = "Mumbai"
print(f"After adding 'city': {dict_var}")

dict_var["age"] = 26
print(f"After updating 'age': {dict_var}")

# Removing elements
removed_value = dict_var.pop("city")
print(f"After pop('city') (removed '{removed_value}'): {dict_var}")

# Accessing elements
print(f"Name: {dict_var['name']}")

# Dictionary methods
keys = dict_var.keys()
values = dict_var.values()
items = dict_var.items()
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Items: {items}")

print("\nOperators in Python:")

# Arithmetic Operators
a, b = 10, 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Floor Division: {a} // {b} = {a // b}")

# Comparison Operators
print("\nComparison Operators:")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical Operators
x, y = True, False
print("\nLogical Operators:")
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# Bitwise Operators
print("\nBitwise Operators:")
m, n = 5, 3  # Binary: 5 = 101, 3 = 011
print(f"{m} & {n}: {m & n}")  # AND
print(f"{m} | {n}: {m | n}")  # OR
print(f"{m} ^ {n}: {m ^ n}")  # XOR
print(f"~{m}: {~m}")  # NOT
print(f"{m} << 1: {m << 1}")  # Left Shift
print(f"{m} >> 1: {m >> 1}")  # Right Shift


"""
if-elif-else Statement:
Used for decision-making.
Executes code blocks based on conditions.
Loops:
For Loop: Iterates over a range or collection.
While Loop: Executes as long as a condition is true.
Nested Loops:
Loops inside another loop.
break and continue:
break: Exits the loop prematurely.
continue: Skips the current iteration and moves to the next.
"""


# Control Flow in Python

# Example of an if-else statement
print("Control Flow - if Statements:")
number = int(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print(f"The number {number} is zero.")

# Example of a for loop
print("\nFor Loop Example:")
print("Numbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Example of a while loop
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Incrementing the counter

#for in decrement order
for i in range(5, 0, -1):  # Start at 5, stop at 0 (exclusive), decrement by -1
    print(i, end=" ")  # Print the number with a space
print()  # Add a newline after the loop

#while in decrement order
i = 5  # Initialize the counter
while i > 0:  # Continue while i is greater than 0
    print(i, end=" ")  # Print the number with a space
    i -= 1  # Decrement i by 1
print()  # Add a newline after the loop

# Nested Loops Example
"""
Outer Loop (for i in range(1, 4)):

    The variable i takes values 1, 2, and 3 in sequential iterations.
    For each value of i, the inner loop executes completely.

Inner Loop (for j in range(1, 4)):

    The variable j takes values 1, 2, and 3 for each iteration of the outer loop.

Output:
    The print statement inside the inner loop displays the current values of i and j during each iteration.
    For each value of i, the inner loop iterates 3 times (for j = 1, 2, 3), producing 3 lines of output per value of i    
"""
print("\nNested Loop Example:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# Break and Continue
print("\nBreak and Continue Examples:")

# Break example
print("Using break:")
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at", num)
        break
    print(num)

# Continue example
print("\nUsing continue:")
for num in range(1, 10):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)

"""
Functions:
Definition: def function_name(parameters):
Blocks of reusable code to organize logic.
Types of Functions:
Without Arguments: No input parameters.
With Arguments: Accepts parameters.
With Return Value: Returns a result.
Default Arguments: Provides a default value for parameters.
Variable-length Arguments: Handles an arbitrary number of inputs using *args.
Keyword Arguments: Explicitly assign values using parameter names.
Modularization:
The main() function organizes code and is the program's entry point.
if __name__ == "__main__": ensures the script runs only when executed directly.
"""

# Demonstrating Functions in Python

# Function without arguments and without return value
def greet():
    print("Hello! Welcome to Python programming.")

# Function with arguments and without return value
def greet_user(name):
    print(f"Hello, {name}! Have a great day.")

# Function with arguments and return value
def add_numbers(a, b):
    return a + b

# Function with default arguments
def multiply_numbers(a, b=2):
    return a * b

# Function with variable-length arguments
def print_items(*items):
    print("Items:", items)

# Function with keyword arguments
def user_details(name, age, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

# Main function to demonstrate modularization
def main():
    # Calling functions
    greet()
    greet_user("Anirudha")

    # Using return values
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    print(f"Sum of {num1} and {num2} is {result}")

    # Default arguments
    product = multiply_numbers(5)  # b defaults to 2
    print(f"Product of 5 and default value 2 is {product}")

    # Variable-length arguments
    print_items("Apple", "Banana", "Cherry")

    # Keyword arguments
    user_details(name="Anirudha", age=25, city="Latur")

# Entry point of the program
if __name__ == "__main__":
    main()

# Function to find occurrences of a character in a string
def find_character(string, char):
    # Use a list comprehension with enumerate to get all indices where 'char' matches
    indices = [i for i, c in enumerate(string) if c == char]
    # Count the number of occurrences of 'char'
    count = len(indices)
    # Print the results: how many times the character is found and its indices
    print(f"Character '{char}' is found {count} times at indices {indices}.")

# Function to find occurrences of a substring in a string
def find_substring(string, substring):
    start = 0  # Start searching from the beginning of the string
    indices = []  # List to store the start and end indices of all matches
    while start < len(string):  # Continue until the end of the string
        # Use the `find` method to locate the substring starting at the current `start`
        start = string.find(substring, start)
        if start == -1:  # If `find` returns -1, the substring is no longer found
            break
        # Add the start and end indices (inclusive) of the found substring to the list
        indices.append((start, start + len(substring) - 1))
        # Increment `start` to continue searching after the current match
        start += 1
    # Count the number of matches found
    count = len(indices)
    # Print the results: how many times the substring is found and the ranges of indices
    print(f"Substring '{substring}' is found {count} times at index ranges {indices}.")


"""
Arrays:
Use the array module for arrays of specific data types.
Efficient for numerical operations.
Stacks:
LIFO (Last In, First Out) data structure.
append() to push and pop() to pop.
Queues:
FIFO (First In, First Out) data structure.
Use collections.deque for efficient operations.

"""

import array

print("=== Arrays in Python ===")

# Creating an array of integers
numbers = array.array('i', [10, 20, 30, 40, 50])
print("Original Array:", numbers)

# Adding Elements
numbers.append(60)
print("After append(60):", numbers)

# Extending Array
numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)

# Inserting Elements
numbers.insert(3, 35)  # Insert 35 at index 3
print("After insert(3, 35):", numbers)

# Removing Elements
numbers.pop(2)  # Removes the element at index 2
print("After pop(2):", numbers)

numbers.remove(40)  # Removes the first occurrence of 40
print("After remove(40):", numbers)

# Accessing Elements
print("Element at Index 1:", numbers[1])

# Slicing
print("Slice [1:4]:", numbers[1:4])

# Updating Elements
numbers[0] = 15
print("After updating index 0 to 15:", numbers)

# Searching for an Element
index_of_70 = numbers.index(70)  # Returns the index of the first occurrence of 70
print("Index of 70:", index_of_70)

# Reversing the Array
numbers.reverse()
print("After reverse():", numbers)

# Copying the Array
copied_array = numbers[:]
print("Copied Array:", copied_array)

# Iterating Through the Array
print("Iterating Through Array:")
for num in numbers:
    print(num, end=" ")
print()

# Converting Array to a List
list_representation = numbers.tolist()
print("Array as List:", list_representation)

# Sorting (requires conversion to list first as `array` module doesn't support in-place sort)
sorted_array = array.array('i', sorted(numbers))
print("Sorted Array:", sorted_array)

# Array Operations
# Element-wise addition, subtraction, multiplication, and division can be done using list comprehension
added_array = array.array('i', [x + 10 for x in numbers])
print("Element-wise Addition (+10):", added_array)

multiplied_array = array.array('i', [x * 2 for x in numbers])
print("Element-wise Multiplication (*2):", multiplied_array)

# Checking Array Length
print("Length of Array:", len(numbers))

# =======================
# Array Manipulations (NumPy)
# =======================
# Importing NumPy for Array manipulations
import numpy as np
array_var = np.array([1, 2, 3, 4, 5])
print("\n=== Array Manipulations (NumPy) ===")
print(f"Original Array: {array_var}")

# Adding elements
array_var = np.append(array_var, [6])
print(f"After append([6]): {array_var}")

# Removing elements
array_var = np.delete(array_var, 2)
print(f"After delete(index 2): {array_var}")

# Updating elements
array_var[1] = 99
print(f"After updating index 1 to 99: {array_var}")

# Array operations
array_var = array_var * 2
print(f"After element-wise multiplication by 2: {array_var}")

# Sorting
sorted_array = np.sort(array_var)
print(f"After sort(): {sorted_array}")


# Stack Implementation and Manipulations
print("=== Stack Implementation ===")

stack = []

# Push (Add element to the stack)
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after push operations:", stack)

# Pop (Remove element from the top of the stack)
popped_element = stack.pop()
print(f"Popped Element: {popped_element}")
print("Stack after pop operation:", stack)

# Peek (View the top element without removing it)
if stack:
    top_element = stack[-1]
    print(f"Top Element (Peek): {top_element}")

# Check if the stack is empty
is_empty = len(stack) == 0
print(f"Is Stack Empty? {is_empty}")

# Get Stack Size
stack_size = len(stack)
print(f"Stack Size: {stack_size}")

# Iterate Through the Stack
print("Iterating through Stack (top to bottom):")
for element in reversed(stack):
    print(element, end=" ")
print()

#Queue Implementation and Manipulations
from collections import deque

print("\n=== Queue Implementation ===")

queue = deque()

# Enqueue (Add element to the end of the queue)
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueue operations:", queue)

# Dequeue (Remove element from the front of the queue)
dequeued_element = queue.popleft()
print(f"Dequeued Element: {dequeued_element}")
print("Queue after dequeue operation:", queue)

# Peek (View the front element without removing it)
if queue:
    front_element = queue[0]
    print(f"Front Element (Peek): {front_element}")

# Check if the queue is empty
is_empty = len(queue) == 0
print(f"Is Queue Empty? {is_empty}")

# Get Queue Size
queue_size = len(queue)
print(f"Queue Size: {queue_size}")

# Iterate Through the Queue
print("Iterating through Queue (front to back):")
for element in queue:
    print(element, end=" ")
print()

"""
Input/Output:
input() function to accept user input.
print() function for formatted output.
File Handling:
Open files using open() with modes like "r", "w", "a", etc.
Use with for safe handling, ensuring the file is closed automatically.
Operations:
Write: Write content to a file ("w" mode overwrites the file).
Append: Add new content to an existing file ("a" mode).
Read: Read file content line-by-line or all at once ("r" mode).
File Safety:
Check for file existence using os.path.exists() before performing operations like deletion.
"""

# Demonstrating Input and Output in Python

# Simple input and output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")

# File Handling in Python
# Writing to a file
print("\nWriting to a file:")
with open("example.txt", "w") as file:
    file.write("Hello, this is an example of file handling in Python.\n")
    file.write(f"Name: {name}, Age: {age}\n")
print("Data has been written to 'example.txt'.")

# Reading from a file
print("\nReading from the file:")
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending data to a file
print("\nAppending to the file:")
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")
print("Data has been appended to 'example.txt'.")

# Reading the file again to verify appended data
print("\nReading the updated file:")
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("Updated File Content:\n", updated_content)

# Handling files safely: Check if the file exists before opening
import os

file_path = "example.txt"
if os.path.exists(file_path):
    print("\nDeleting the file for cleanup:")
    os.remove(file_path)  # Delete the file
    print(f"'{file_path}' has been deleted.")
else:
    print(f"File '{file_path}' does not exist.")

# File operations in different modes:
# "r": Read-only mode (default)
# "w": Write mode (overwrites file content)
# "a": Append mode (adds content to the end)
# "x": Create mode (fails if the file exists)
# "r+": Read and write mode
# "w+": Write and read mode

"""
performing arithmetic operations on numbers from a file and saving the results in a new file.
"""
# File names
input_file = "num.txt"
output_file = "results.txt"

# Open the input file to read numbers
with open(input_file, "r") as infile:
    # Read all lines and convert them to a list of integers
    numbers = [int(line.strip()) for line in infile]

# Perform arithmetic operations
results = []  # List to store operation results
for num in numbers:
    # Perform desired operations (example: add, subtract, multiply, divide)
    addition = num + 5
    subtraction = num - 5
    multiplication = num * 2
    division = round(num / 2, 2)  # Rounded to 2 decimal places

    # Append results as a formatted string
    results.append(
        f"Number: {num}, Addition: {addition}, Subtraction: {subtraction}, "
        f"Multiplication: {multiplication}, Division: {division}"
    )

# Write the results to the output file
with open(output_file, "w") as outfile:
    for result in results:
        outfile.write(result + "\n")

print(f"Arithmetic operations completed. Results saved in '{output_file}'.")

"""
Exception Handling:
try Block: Code that might raise exceptions.
except Block: Handles specific exceptions like ZeroDivisionError, TypeError, etc.
else Block: Executes if no exceptions are raised.
finally Block: Executes whether or not an exception occurs (useful for cleanup tasks like closing files).
Common Exceptions:
ZeroDivisionError: Division by zero.
TypeError: Operation on incompatible types.
ValueError: Invalid value for an operation.
Debugging with Assertions:
assert statements are used for debugging by ensuring certain conditions are met.
Syntax: assert condition, "Error message if condition is False"
Best Practices:
Use specific exceptions to handle errors effectively.
Avoid catching generic exceptions unless absolutely necessary (except Exception as e).
Log exceptions for debugging.
"""

# Demonstrating Exception Handling in Python

def divide_numbers(a, b):
    try:
        # Attempt to perform division
        result = a / b
        print(f"Result of {a} / {b} is {result}")
    except ZeroDivisionError as e:
        # Handle division by zero
        print(f"Error: Division by zero is not allowed. ({e})")
    except TypeError as e:
        # Handle invalid data types
        print(f"Error: Invalid data types for division. ({e})")
    else:
        # Execute if no exception occurs
        print("Division was successful!")
    finally:
        # Execute regardless of whether an exception occurs
        print("Execution of divide_numbers() is complete.\n")

# Debugging Example Using `assert`
def calculate_square_root(x):
    try:
        assert x >= 0, "Cannot calculate the square root of a negative number."
        import math
        return math.sqrt(x)
    except AssertionError as e:
        print(f"Error: {e}")

# Main function
def main():
    # Example of exception handling
    print("Exception Handling Examples:")
    divide_numbers(10, 2)  # Valid division
    divide_numbers(10, 0)  # Division by zero
    divide_numbers(10, "five")  # Invalid data type
    
    # Example of debugging using `assert`
    print("\nDebugging with Assertions:")
    print(f"Square root of 16 is {calculate_square_root(16)}")
    calculate_square_root(-4)  # Will raise an assertion error

# Entry point of the program
if __name__ == "__main__":
    main()


