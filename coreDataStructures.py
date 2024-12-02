"""
A stack is a data structure that follows the LIFO (Last In, First Out) principle. 
This means that the last element added (pushed) to the stack will be the first to be removed (popped). 
Think of a stack as a pile of plates—the plate added last is removed first.
Key Operations in a Stack:

    Push: Add an element to the top of the stack.
    Pop: Remove and return the top element of the stack.
    Peek/Top: View the top element without removing it.
    IsEmpty: Check if the stack is empty.
    Size: Return the total number of elements in the stack.
"""
class Stack:
    def __init__(self):
        """Initialize the stack with an empty list."""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack.
        
        Args:
            item: The element to be added to the stack.
        """
        self.stack.append(item)  # Append the element to the list
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item from the stack.
        
        Returns:
            The top element of the stack if it's not empty.
            If the stack is empty, returns None.
        """
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
            return None
        removed_item = self.stack.pop()  # Remove the last element
        print(f"Popped: {removed_item}")
        return removed_item

    def peek(self):
        """View the top element of the stack without removing it.
        
        Returns:
            The top element if the stack is not empty.
            If the stack is empty, returns None.
        """
        if self.is_empty():
            print("Stack is empty! No top element.")
            return None
        return self.stack[-1]  # Access the last element

    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack.
        
        Returns:
            The number of elements currently in the stack.
        """
        return len(self.stack)

    def display(self):
        """Display the current state of the stack."""
        print("Current Stack (Top -> Bottom):", self.stack[::-1])  # Reverse for top-to-bottom display

# Example Usage
if __name__ == "__main__":
    # Create an instance of Stack
    s = Stack()

    # Add elements to the stack
    s.push(5)
    s.push(10)
    s.push(15)

    # Display the stack
    s.display()

    # View the top element
    print(f"Top Element: {s.peek()}")

    # Remove elements from the stack
    s.pop()
    s.display()

    # Check if the stack is empty
    print(f"Is the stack empty? {s.is_empty()}")

    # Display the size of the stack
    print(f"Stack Size: {s.size()}")

"""
A queue is a data structure that follows the FIFO (First In, First Out) principle. 
This means that elements are added at the end (enqueue) and removed from the front (dequeue). 
Think of it like a line of people waiting to get into a theater—the person who joins first leaves first.
Key Operations in a Queue:

    Enqueue: Add an element to the rear of the queue.
    Dequeue: Remove and return the element from the front of the queue.
    Peek/Front: View the front element without removing it.
    IsEmpty: Check if the queue is empty.
    Size: Return the total number of elements in the queue.
"""
class Queue:
    def __init__(self):
        """Initialize the queue with an empty list."""
        self.queue = []

    def enqueue(self, item):
        """Add an item to the rear of the queue.
        
        Args:
            item: The element to be added to the queue.
        """
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the item from the front of the queue.
        
        Returns:
            The front element of the queue if it's not empty.
            If the queue is empty, returns None.
        """
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        removed_item = self.queue.pop(0)  # Remove the front element
        print(f"Dequeued: {removed_item}")
        return removed_item

    def peek(self):
        """View the front element of the queue without removing it.
        
        Returns:
            The front element if the queue is not empty.
            If the queue is empty, returns None.
        """
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self):
        """Return the size of the queue.
        
        Returns:
            The number of elements currently in the queue.
        """
        return len(self.queue)

    def display(self):
        """Display the current state of the queue."""
        print("Current Queue:", self.queue)

# Example Usage
if __name__ == "__main__":
    # Create an instance of Queue
    q = Queue()

    # Add elements to the queue
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    # Display the queue
    q.display()

    # View the front element
    print(f"Front Element: {q.peek()}")

    # Remove elements from the queue
    q.dequeue()
    q.display()

    # Check if the queue is empty
    print(f"Is the queue empty? {q.is_empty()}")

    # Display the size of the queue
    print(f"Queue Size: {q.size()}")

"""
A singly linked list is a data structure where each element (node) contains two parts:
    Data: The actual value stored in the node.
    Pointer: A reference to the next node in the sequence.
The last node points to None, indicating the end of the list.
head as the Entry Point:
    The head keeps track of the starting point of the list.
    If the list is empty, the head is set to None
Insertion:
    At the beginning.
    At the end.
    At a specific position.
Deletion:
    From the beginning.
    From the end.
    A specific value or position.
Traversal:
    Iterate through the list to print or access elements.
Search:
    Find if a specific value exists in the list.
Size:
    Count the number of nodes in the list
"""
class Node:
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data  # Store data
        self.next = None  # Initialize next as None


class SinglyLinkedList:
    def __init__(self):
        """Initialize the linked list with a head pointer."""
        self.head = None  # Initially, the list is empty

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list.
        
        Args:
            data: The value to be added to the list.
        """
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the list.
        
        Args:
            data: The value to be added to the list.
        """
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, the new node becomes the head
            self.head = new_node
            print(f"Inserted {data} as the first element in the list.")
            return
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node  # Link the last node to the new node
        print(f"Inserted {data} at the end.")

    def delete_from_beginning(self):
        """Remove the node at the beginning of the list."""
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        removed_data = self.head.data  # Get the data of the head
        self.head = self.head.next  # Update the head to the next node
        print(f"Deleted {removed_data} from the beginning.")

    def delete_from_end(self):
        """Remove the node at the end of the list."""
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.next is None:  # If there's only one node
            removed_data = self.head.data
            self.head = None
            print(f"Deleted {removed_data} (only node in the list).")
            return
        # Traverse to the second-last node
        current = self.head
        while current.next.next:
            current = current.next
        removed_data = current.next.data  # Get the data of the last node
        current.next = None  # Remove the link to the last node
        print(f"Deleted {removed_data} from the end.")

    def display(self):
        """Display all elements in the list."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Current List: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of list

    def search(self, key):
        """Search for a specific value in the list.
        
        Args:
            key: The value to search for.
        
        Returns:
            True if the value exists, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:  # Check if the current node has the key
                print(f"Found {key} in the list.")
                return True
            current = current.next
        print(f"{key} not found in the list.")
        return False

    def size(self):
        """Count the number of nodes in the list.
        
        Returns:
            The total number of nodes.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Size of the list: {count}")
        return count


# Example Usage
if __name__ == "__main__":
    # Create an instance of SinglyLinkedList
    sll = SinglyLinkedList()

    # Insert elements
    sll.insert_at_beginning(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.insert_at_beginning(5)

    # Display the list
    sll.display()

    # Delete elements
    sll.delete_from_beginning()
    sll.delete_from_end()

    # Display the list
    sll.display()

    # Search for an element
    sll.search(20)
    sll.search(100)

    # Display the size of the list
    sll.size()

"""
A doubly linked list is a linear data structure where each node contains:
    A data field to store the value.
    A next pointer to link to the next node in the sequence.
    A previous pointer to link to the previous node in the sequence.
The head points to the first node, while the tail points to the last node. 
The inclusion of previous pointers enables traversal in both directions (forward and backward).
"""
class Node:
    def __init__(self, data):
        """Initialize a node with data and pointers to next and previous nodes."""
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        """Initialize the doubly linked list with head and tail pointers."""
        self.head = None  # Points to the first node
        self.tail = None  # Points to the last node

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = self.tail = new_node  # Both head and tail point to the new node
        else:
            new_node.next = self.head  # Link the new node's next to the current head
            self.head.prev = new_node  # Link the current head's previous to the new node
            self.head = new_node  # Update the head to the new node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)  # Create a new node
        if self.tail is None:  # If the list is empty
            self.head = self.tail = new_node  # Both head and tail point to the new node
        else:
            new_node.prev = self.tail  # Link the new node's previous to the current tail
            self.tail.next = new_node  # Link the current tail's next to the new node
            self.tail = new_node  # Update the tail to the new node
        print(f"Inserted {data} at the end.")

    def delete_from_beginning(self):
        """Remove the node at the beginning of the list."""
        if self.head is None:  # If the list is empty
            print("List is empty. Nothing to delete.")
            return
        if self.head == self.tail:  # If there is only one node
            removed_data = self.head.data
            self.head = self.tail = None  # Update both head and tail to None
        else:
            removed_data = self.head.data
            self.head = self.head.next  # Update the head to the next node
            self.head.prev = None  # Remove the previous link of the new head
        print(f"Deleted {removed_data} from the beginning.")

    def delete_from_end(self):
        """Remove the node at the end of the list."""
        if self.tail is None:  # If the list is empty
            print("List is empty. Nothing to delete.")
            return
        if self.head == self.tail:  # If there is only one node
            removed_data = self.tail.data
            self.head = self.tail = None  # Update both head and tail to None
        else:
            removed_data = self.tail.data
            self.tail = self.tail.prev  # Update the tail to the previous node
            self.tail.next = None  # Remove the next link of the new tail
        print(f"Deleted {removed_data} from the end.")

    def display_forward(self):
        """Display all elements in the list from head to tail."""
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        print("List (head -> tail): ", end="")
        current = self.head
        while current:  # Traverse from head to tail
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Display all elements in the list from tail to head."""
        if self.tail is None:  # If the list is empty
            print("List is empty.")
            return
        print("List (tail -> head): ", end="")
        current = self.tail
        while current:  # Traverse from tail to head
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

    def search(self, key):
        """Search for a specific value in the list.
        
        Args:
            key: The value to search for.
        
        Returns:
            True if the value exists in the list, False otherwise.
        """
        current = self.head  # Start from the head
        while current:  # Traverse the list
            if current.data == key:  # Check if the current node's data matches the key
                print(f"Found {key} in the list.")
                return True
            current = current.next
        print(f"{key} not found in the list.")
        return False

    def size(self):
        """Count the number of nodes in the list."""
        count = 0
        current = self.head  # Start from the head
        while current:  # Traverse the list and count nodes
            count += 1
            current = current.next
        print(f"Size of the list: {count}")
        return count


# Example Usage
if __name__ == "__main__":
    # Create an instance of DoublyLinkedList
    dll = DoublyLinkedList()

    # Insert elements
    dll.insert_at_beginning(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)

    # Display the list forward and backward
    dll.display_forward()
    dll.display_backward()

    # Delete elements
    dll.delete_from_beginning()
    dll.delete_from_end()

    # Display the list
    dll.display_forward()

    # Search for an element
    dll.search(20)
    dll.search(100)

    # Display the size of the list
    dll.size()

"""
A Circular Linked List (CLL) is a variation of a linked list where:
    The last node points back to the first node, creating a circular structure.
    It can be implemented as singly circular linked list (only next pointer) or doubly circular linked list (both next and prev pointers).
The circular structure provides advantages for applications like:
    Buffer management.
    Round-robin scheduling.
    Applications requiring repetitive traversal.
Head Node:
    Points to the first node.
    In a singly circular linked list, the next pointer of the last node points back to head.
Traversal:
    The traversal must detect when it has reached back to the head to stop.
Insertion and Deletion:
    Operations are similar to singly linked lists but need to ensure the circular connection is maintained.
"""
class Node:
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None  # Pointer to the next node


class CircularLinkedList:
    def __init__(self):
        """Initialize the circular linked list with a head pointer."""
        self.head = None  # Points to the first node in the list

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the circular linked list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Point head to the new node
            new_node.next = new_node  # Point the new node's next to itself
        else:
            # Traverse to the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            # Insert the new node at the beginning
            new_node.next = self.head
            self.head = new_node
            current.next = self.head  # Update the last node's next to the new head
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        """Insert a new node at the end of the circular linked list."""
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Point head to the new node
            new_node.next = new_node  # Point the new node's next to itself
        else:
            # Traverse to the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            # Insert the new node at the end
            current.next = new_node
            new_node.next = self.head  # Point the new node's next to head
        print(f"Inserted {data} at the end.")

    def delete_from_beginning(self):
        """Delete the node at the beginning of the circular linked list."""
        if self.head is None:  # If the list is empty
            print("List is empty. Nothing to delete.")
            return
        if self.head.next == self.head:  # If there is only one node
            removed_data = self.head.data
            self.head = None  # Remove the single node
        else:
            # Traverse to the last node
            current = self.head
            while current.next != self.head:
                current = current.next
            # Remove the first node
            removed_data = self.head.data
            self.head = self.head.next  # Update head to the next node
            current.next = self.head  # Update the last node's next to the new head
        print(f"Deleted {removed_data} from the beginning.")

    def delete_from_end(self):
        """Delete the node at the end of the circular linked list."""
        if self.head is None:  # If the list is empty
            print("List is empty. Nothing to delete.")
            return
        if self.head.next == self.head:  # If there is only one node
            removed_data = self.head.data
            self.head = None  # Remove the single node
        else:
            # Traverse to the second last node
            current = self.head
            while current.next.next != self.head:
                current = current.next
            # Remove the last node
            removed_data = current.next.data
            current.next = self.head  # Update the second last node's next to head
        print(f"Deleted {removed_data} from the end.")

    def display(self):
        """Display all elements in the circular linked list."""
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        print("List elements: ", end="")
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # Stop when back to head
                break
        print("(head)")

    def search(self, key):
        """Search for a specific value in the circular linked list.
        
        Args:
            key: The value to search for.
        
        Returns:
            True if the value exists in the list, False otherwise.
        """
        if self.head is None:  # If the list is empty
            print(f"{key} not found in the list.")
            return False
        current = self.head
        while True:
            if current.data == key:  # Check if the current node's data matches the key
                print(f"Found {key} in the list.")
                return True
            current = current.next
            if current == self.head:  # Stop when back to head
                break
        print(f"{key} not found in the list.")
        return False


# Example Usage
if __name__ == "__main__":
    # Create an instance of CircularLinkedList
    cll = CircularLinkedList()

    # Insert elements
    cll.insert_at_beginning(10)
    cll.insert_at_end(20)
    cll.insert_at_end(30)
    cll.insert_at_beginning(5)

    # Display the list
    cll.display()

    # Delete elements
    cll.delete_from_beginning()
    cll.delete_from_end()

    # Display the list
    cll.display()

    # Search for an element
    cll.search(20)
    cll.search(100)
