"""
### Problem 1: Check for Balanced Parentheses
Problem Statement:  
Given a string of parentheses (e.g., `{[()]}`), check if it is balanced. A string is balanced if every opening parenthesis has a corresponding closing one, and they are correctly nested.

Solution:  
Use a stack to push opening parentheses and pop them when matching closing parentheses are encountered.
"""
def is_balanced_parentheses(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in "([{":  # If it's an opening parenthesis
            stack.append(char)
        elif char in ")]}":  # If it's a closing parenthesis
            if not stack or stack.pop() != pairs[char]:
                return False  # Unmatched parenthesis
    return not stack  # True if stack is empty (all matched)

# Example usage
print(is_balanced_parentheses("{[()]}"))  # Output: True
print(is_balanced_parentheses("{[(])}"))  # Output: False

"""
### Problem 2: Reverse a String Using a Stack
Problem Statement:  
Reverse a given string (e.g., `"hello"`) using a stack.

Solution:  
Push all characters onto a stack and then pop them to reverse the order.
"""
def reverse_string_using_stack(string):
    stack = []
    for char in string:
        stack.append(char)
    reversed_string = ''.join(stack.pop() for _ in range(len(stack)))
    return reversed_string

# Example usage
print(reverse_string_using_stack("hello"))  # Output: "olleh"

"""
### Problem 3: Implement a Queue Using Two Stacks
Problem Statement:  
Implement a queue using two stacks such that enqueue and dequeue operations are performed efficiently.

Solution:  
Use one stack for enqueue and another for dequeue. Transfer elements when needed.
"""
class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []  # Stack for enqueue
        self.stack_out = []  # Stack for dequeue

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())  # Transfer elements
        return self.stack_out.pop() if self.stack_out else None  # Return dequeued element

# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

"""
### Problem 4: Find the First Negative Number in Every Window of Size `k`
Problem Statement:  
Given an array and a window size `k`, find the first negative number in each window. 
If no negative number is found, return `0`.

Solution:  
Use a queue to store the indices of negative numbers within the current window.
"""
def first_negative_in_window(arr, k):
    queue = []
    result = []
    
    for i in range(len(arr)):
        if arr[i] < 0:
            queue.append(i)  # Store the index of the negative number
        
        # Remove elements that are out of the current window
        if queue and queue[0] < i - k + 1:
            queue.pop(0)
        
        # If the current index is valid for a result
        if i >= k - 1:
            result.append(arr[queue[0]] if queue else 0)
    
    return result

# Example usage
print(first_negative_in_window([12, -1, -7, 8, -15, 30, 16, 28], 3))
# Output: [-1, -1, -7, -15, -15, 0]

"""
### Problem 5: Implement a Stack That Supports `getMin` in O(1)
Problem Statement:  
Design a stack that supports standard operations (`push`, `pop`, `top`) and 
an additional operation, `getMin`, which returns the minimum element in the stack in O(1) time.

Solution:  
Use an auxiliary stack to keep track of the minimum value at each level.
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Auxiliary stack to track minimums

    def push(self, value):
        self.stack.append(value)
        # Push the smaller value between the new value and the current minimum
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if self.stack:
            popped = self.stack.pop()
            if popped == self.min_stack[-1]:  # Remove from min stack if it was the minimum
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

# Example usage
min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # Output: 3
min_stack.push(2)
min_stack.push(1)
print(min_stack.getMin())  # Output: 1
min_stack.pop()
print(min_stack.getMin())  # Output: 2

