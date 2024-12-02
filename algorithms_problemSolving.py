"""
Introduction to Algorithms and Problem Solving
Algorithm Basics: An algorithm is a step-by-step procedure to solve a problem.
Input: The data the algorithm processes.
Output: The result produced by the algorithm.
Steps: Logical instructions executed to transform input into output.
Problem-Solving Steps:
Understand the problem.
Plan the algorithm (steps or flowchart).
Write the code.
Test with various inputs.
"""
# Example 1: Simple Algorithm - Finding the Maximum of Three Numbers
def find_maximum(a, b, c):
    """
    Find the maximum of three numbers using a simple algorithm.   
    Args:
        a (int/float): The first number.
        b (int/float): The second number.
        c (int/float): The third number.   
    Returns:
        int/float: The maximum of the three numbers.
    """
    # Check if 'a' is greater than or equal to both 'b' and 'c'
    if a >= b and a >= c:
        return a  # If true, 'a' is the maximum
    
    # If the above condition is false, check if 'b' is greater than or equal to both 'a' and 'c'
    elif b >= a and b >= c:
        return b  # If true, 'b' is the maximum
    
    # If neither 'a' nor 'b' is the maximum, 'c' must be the maximum
    else:
        return c  # Return 'c' as the maximum
# Example usage
max_value = find_maximum(10, 20, 15)  # Should return 20
print(f"The maximum value is: {max_value}")

# Program to find the largest number in a list using a simple algorithm
# Step 1: Define a function to find the largest number
def find_largest(numbers):
    # Step 2: Assume the first number is the largest
    largest = numbers[0]
    # Step 3: Iterate through the list
    for number in numbers:
        # Step 4: Compare each number with the current largest
        if number > largest:
            largest = number  # Update the largest number if a bigger one is found
    return largest  # Step 5: Return the largest number
# Example usage
numbers = [10, 25, 8, 56, 45]
print("The largest number is:", find_largest(numbers))


# Example 2: Algorithm for Linear Search
def linear_search(arr, target):
    """
    Linear Search is a simple search algorithm that checks every element in a list (or array) one by one to find the target value.
    It continues until the target is found or the entire list is checked.
Algorithm:
    Start at the first element of the list.
    Compare the target value with each element.
    If a match is found, return the index of the element.
    If the end of the list is reached and no match is found, return -1 to indicate the target is not in the list.
    Perform linear search on a list.   
    Args:
        arr (list): The list to search in.
        target: The value to search for.   
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    # Loop through each element in the list along with its index
    for index, value in enumerate(arr):
        # Check if the current element matches the target value
        if value == target:
            return index  # If found, return the index of the target
    # If the loop completes and the target is not found, return -1
    return -1

# Example usage
numbers = [10, 20, 30, 40, 50]
target_value = 30

# Perform linear search and print the result
result = linear_search(numbers, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the list.")


# Example 3: Algorithm for Calculating Factorial (Recursive Approach)
def factorial(n):
    """
    Factorial of a number nn (denoted as n!n!) is the product of all positive integers from 1 to n
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): The number to calculate the factorial for. Must be a non-negative integer.
    
    Returns:
        int: The factorial of the number.
    """
    # Base case: If n is 0 or 1, the factorial is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: Multiply the number by the factorial of (n - 1)
    else:
        return n * factorial(n - 1)

# Example usage
number = 5  # You can change this to test with other numbers
result = factorial(number)
print(f"The factorial of {number} is {result}.")


# Example 4: Problem Solving - Check if a Number is Prime
def is_prime(number):
    """
    Prime numbers are numbers greater than 1 that have no divisors other than 1 and themselves.
    A number is prime if it is only divisible by 1 and itself.
    Algorithm:
    Check if a number is divisible by any number from 2 to root of n
    If it is divisible, the number is not prime; otherwise, it is prime.
    Check if a number is prime.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):  # Check divisors up to the square root of the number
        if number % i == 0:
            return False
    return True
num = 29
print(f"{num} is prime:", is_prime(num))

# Example 5: Problem Solving - Generating Fibonacci Sequence
def generate_fibonacci(n):
    """
    The Fibonacci Sequence is a series of numbers in which each number is the sum of the two preceding ones.
    Starting from 0 and 1,
    Generate Fibonacci sequence up to n terms.  
    Args:
        n (int): The number of terms to generate in the Fibonacci sequence.    
    Returns:
        list: The Fibonacci sequence as a list of numbers.
    """
    # If the number of terms is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # If n is 1, return a list with only the first Fibonacci number (0)
    elif n == 1:
        return [0]
    
    # If n is 2, return a list with the first two Fibonacci numbers (0, 1)
    elif n == 2:
        return [0, 1]
    
    # For n > 2, generate the sequence by appending new terms
    else:
        # Initialize the sequence with the first two Fibonacci numbers (0, 1)
        fib = [0, 1]
        
        # Loop through and generate each subsequent Fibonacci number
        for i in range(2, n):
            # The next Fibonacci number is the sum of the last two numbers in the sequence
            fib.append(fib[i - 1] + fib[i - 2])
        
        # Return the complete Fibonacci sequence
        return fib
# Example usage
terms = 10  # You can change this to generate a different number of terms
result = generate_fibonacci(terms)
print(f"The Fibonacci sequence with {terms} terms is: {result}")


"""
Introduction to Object-Oriented Programming (OOP)
OOP organizes programs around objects and data. 
The four main principles of OOP are Encapsulation, Inheritance, Polymorphism, and Abstraction.
"""
# Defining a class in Python
class Person:
    def __init__(self, name, age):
        # Encapsulation: Properties (attributes) are part of the object
        self.name = name
        self.age = age

    def greet(self):
        # A method to greet the person
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example usage
person1 = Person("Alice", 30)
person1.greet()  # Accessing the method

# Inheritance Example: Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.student_id = student_id  # Add a new attribute specific to Student

    def greet(self):
        # Polymorphism: Overriding the greet method
        print(f"Hi, I am {self.name}, a student with ID {self.student_id}.")

# Example usage
student = Student("Anirudha", 40, "A12345")
student.greet()  # Calls the overridden method
