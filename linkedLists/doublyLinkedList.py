class Node:
    """Node class represents a node in the doubly linked list"""
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None    # Reference to next node
        self.prev = None    # Reference to previous node


class DoublyLinkedList:
    """DoublyLinkedList class implements a doubly linked list with head and tail pointers"""
    def __init__(self):
        self.head = None  # First node in the list
        self.tail = None  # Last node in the list

    def add_to_front(self, value):
        """Add a new node with given value to the front of the list"""
        new_node = Node(value)
        if not self.head:  # If list is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f"Added {value} to front. Current list: {self}")

    def add_to_end(self, value):
        """Add a new node with given value to the end of the list"""
        new_node = Node(value)
        if not self.tail:  # If list is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"Added {value} to end. Current list: {self}")

    def remove_from_front(self):
        """Remove and return the value from the front of the list"""
        if not self.head:
            print("List is empty, nothing to remove from front.")
            return None
            
        removed_value = self.head.value
        if self.head == self.tail:  # Only one node in list
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        print(f"Removed {removed_value} from front. Current list: {self}")
        return removed_value

    def remove_from_end(self):
        """Remove and return the value from the end of the list"""
        if not self.tail:
            print("List is empty, nothing to remove from end.")
            return None
            
        removed_value = self.tail.value
        if self.head == self.tail:  # Only one node in list
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        print(f"Removed {removed_value} from end. Current list: {self}")
        return removed_value

    def __str__(self):
        """String representation of the list for printing"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values) if values else "Empty List"


# Test Cases
if __name__ == "__main__":
    print("\n=== Testing Doubly Linked List ===\n")
    
    # Create a new doubly linked list
    dll = DoublyLinkedList()
    print("Created new empty list:", dll)
    
    # Test adding to front
    dll.add_to_front(10)
    dll.add_to_front(20)
    dll.add_to_front(30)
    
    # Test adding to end
    dll.add_to_end(40)
    dll.add_to_end(50)
    
    # Test removing from front
    val = dll.remove_from_front()
    print(f"Removed value: {val}")
    
    # Test removing from end
    val = dll.remove_from_end()
    print(f"Removed value: {val}")
    
    # Test removing all elements
    print("\nRemoving all elements:")
    dll.remove_from_front()
    dll.remove_from_front()
    dll.remove_from_end()  # Should handle empty list case
    
    # Test edge cases
    print("\nTesting edge cases:")
    empty_list = DoublyLinkedList()
    empty_list.remove_from_front()  # Should print empty message
    empty_list.remove_from_end()    # Should print empty message
    
    # Test single element case
    print("\nTesting single element case:")
    single = DoublyLinkedList()
    single.add_to_front(100)
    single.remove_from_end()
    single.add_to_end(200)
    single.remove_from_front()
    
    print("\n=== Testing Complete ===")