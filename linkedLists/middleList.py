class ListNode:
    """ListNode class represents a node in a singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val      # Value stored in the node
        self.next = next     # Reference to next node

class Solution:
    def middleNode(self, head):
        """
        Find the middle node of a singly linked list using the fast/slow pointer approach.
        
        Args:
            head: ListNode - the head node of the linked list
            
        Returns:
            ListNode - the middle node of the linked list
            (if even number of nodes, returns the second middle node)
        """
        ahead = head  # Fast pointer that moves two steps at a time
        
        while ahead and ahead.next:
            ahead = ahead.next.next  # Move fast pointer two steps
            head = head.next         # Move slow pointer one step
            
        return head  # When fast reaches end, slow is at middle

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
    print("\n=== Testing Middle Node of Linked List ===\n")
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
    
    # Test Case 1: Odd length list
    print("Test Case 1: Odd length list (1->2->3->4->5)")
    list1 = create_list([1, 2, 3, 4, 5])
    print("Full list: ", end="")
    solution.printList(list1)
    middle1 = solution.middleNode(list1)
    print(f"Middle node value: {middle1.val}")
    print()
    
    # Test Case 2: Even length list
    print("Test Case 2: Even length list (1->2->3->4->5->6)")
    list2 = create_list([1, 2, 3, 4, 5, 6])
    print("Full list: ", end="")
    solution.printList(list2)
    middle2 = solution.middleNode(list2)
    print(f"Middle node value: {middle2.val} (second middle)")
    print()
    
    # Test Case 3: Single element list
    print("Test Case 3: Single element list (42)")
    list3 = create_list([42])
    print("Full list: ", end="")
    solution.printList(list3)
    middle3 = solution.middleNode(list3)
    print(f"Middle node value: {middle3.val}")
    print()
    
    # Test Case 4: Two element list
    print("Test Case 4: Two element list (10->20)")
    list4 = create_list([10, 20])
    print("Full list: ", end="")
    solution.printList(list4)
    middle4 = solution.middleNode(list4)
    print(f"Middle node value: {middle4.val} (second element)")
    print()
    
    # Test Case 5: Empty list
    print("Test Case 5: Empty list")
    list5 = create_list([])
    print("Full list: ", end="")
    solution.printList(list5)
    try:
        middle5 = solution.middleNode(list5)
        print(f"Middle node value: {middle5.val}")
    except AttributeError:
        print("Middle node of empty list is None")
    print()
    
    print("=== Testing Complete ===")