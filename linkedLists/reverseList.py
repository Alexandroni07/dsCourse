class ListNode:
    """ListNode class represents a node in a singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val      # Value stored in the node
        self.next = next    # Reference to next node

class Solution:
    def reverseList(self, head):
        """
        Reverse a singly linked list iteratively.
        
        Args:
            head: ListNode - the head node of the linked list to reverse
            
        Returns:
            ListNode - the head node of the reversed linked list
        """
        new_list = None  # This will become the new head of the reversed list
        
        while head:
            # Store the next node before we overwrite head.next
            next_node = head.next  
            
            # Reverse the link - point current node to the new list
            head.next = new_list  
            
            # Move new_list forward to include the current node
            new_list = head  
            
            # Move to the next node in the original list
            head = next_node  
            
        return new_list

    def printList(self, head):
        """Helper method to print the linked list values"""
        values = []
        current = head
        while current:
            values.append(str(current.val))
            current = current.next
        print(" -> ".join(values) if values else "Empty List")

# Test Cases
if __name__ == "__main__":
    print("\n=== Testing Linked List Reversal ===\n")
    solution = Solution()
    
    # Helper function to create a linked list from a list of values
    def create_list(values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    # Test Case 1: Normal case
    print("Test Case 1: Reverse 1->2->3->4->5")
    list1 = create_list([1, 2, 3, 4, 5])
    print("Original list: ", end="")
    solution.printList(list1)
    reversed1 = solution.reverseList(list1)
    print("Reversed list: ", end="")
    solution.printList(reversed1)
    print()
    
    # Test Case 2: Single element
    print("Test Case 2: Reverse single element list")
    list2 = create_list([42])
    print("Original list: ", end="")
    solution.printList(list2)
    reversed2 = solution.reverseList(list2)
    print("Reversed list: ", end="")
    solution.printList(reversed2)
    print()
    
    # Test Case 3: Empty list
    print("Test Case 3: Reverse empty list")
    list3 = create_list([])
    print("Original list: ", end="")
    solution.printList(list3)
    reversed3 = solution.reverseList(list3)
    print("Reversed list: ", end="")
    solution.printList(reversed3)
    print()
    
    # Test Case 4: Large list
    print("Test Case 4: Reverse large list")
    list4 = create_list(list(range(1, 11)))
    print("Original list: ", end="")
    solution.printList(list4)
    reversed4 = solution.reverseList(list4)
    print("Reversed list: ", end="")
    solution.printList(reversed4)
    print()
    
    print("=== Testing Complete ===")