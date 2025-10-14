from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def test_reverse_list():
    s = Solution()

    # Test Case 1: Standard list with multiple nodes
    print("\n--- Test Case 1: Standard List ---")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(f"Initial list: {linked_list_to_list(head1)}")
    reversed_head1 = s.reverseList(head1)
    print(f"Reversed list: {linked_list_to_list(reversed_head1)}") # Expected: [5, 4, 3, 2, 1]

    # Test Case 2: Empty list
    print("\n--- Test Case 2: Empty List ---")
    head2 = create_linked_list([])
    print(f"Initial list: {linked_list_to_list(head2)}")
    reversed_head2 = s.reverseList(head2)
    print(f"Reversed list: {linked_list_to_list(reversed_head2)}") # Expected: []

    # Test Case 3: List with a single node
    print("\n--- Test Case 3: Single Node List ---")
    head3 = create_linked_list([42])
    print(f"Initial list: {linked_list_to_list(head3)}")
    reversed_head3 = s.reverseList(head3)
    print(f"Reversed list: {linked_list_to_list(reversed_head3)}") # Expected: [42]

    # Test Case 4: List with two nodes
    print("\n--- Test Case 4: Two Node List ---")
    head4 = create_linked_list([1, 99])
    print(f"Initial list: {linked_list_to_list(head4)}")
    reversed_head4 = s.reverseList(head4)
    print(f"Reversed list: {linked_list_to_list(reversed_head4)}") # Expected: [99, 1]

    # Test Case 5: List with all identical elements
    print("\n--- Test Case 5: All Identical Elements ---")
    head5 = create_linked_list([7, 7, 7, 7])
    print(f"Initial list: {linked_list_to_list(head5)}")
    reversed_head5 = s.reverseList(head5)
    print(f"Reversed list: {linked_list_to_list(reversed_head5)}") # Expected: [7, 7, 7, 7]

    # Test Case 6: List with duplicate values
    print("\n--- Test Case 6: List with Duplicates ---")
    head6 = create_linked_list([1, 2, 3, 2, 1])
    print(f"Initial list: {linked_list_to_list(head6)}")
    reversed_head6 = s.reverseList(head6)
    print(f"Reversed list: {linked_list_to_list(reversed_head6)}") # Expected: [1, 2, 3, 2, 1]

    # Test Case 7: A longer list
    print("\n--- Test Case 7: Longer List ---")
    head7 = create_linked_list([10, 20, 30, 40, 50, 60, 70])
    print(f"Initial list: {linked_list_to_list(head7)}")
    reversed_head7 = s.reverseList(head7)
    print(f"Reversed list: {linked_list_to_list(reversed_head7)}") # Expected: [70, 60, 50, 40, 30, 20, 10]

    # Test Case 8: List containing zero
    print("\n--- Test Case 8: List with Zero ---")
    head8 = create_linked_list([5, 0, -5])
    print(f"Initial list: {linked_list_to_list(head8)}")
    reversed_head8 = s.reverseList(head8)
    print(f"Reversed list: {linked_list_to_list(reversed_head8)}") # Expected: [-5, 0, 5]

    # Test Case 9: Palindromic list
    print("\n--- Test Case 9: Palindromic List ---")
    head9 = create_linked_list(['a', 'b', 'c', 'b', 'a'])
    print(f"Initial list: {linked_list_to_list(head9)}")
    reversed_head9 = s.reverseList(head9)
    print(f"Reversed list: {linked_list_to_list(reversed_head9)}") # Expected: ['a', 'b', 'c', 'b', 'a']

    # Test Case 10: List with negative numbers
    print("\n--- Test Case 10: List with Negative Numbers ---")
    head10 = create_linked_list([-1, -2, -3, -4])
    print(f"Initial list: {linked_list_to_list(head10)}")
    reversed_head10 = s.reverseList(head10)
    print(f"Reversed list: {linked_list_to_list(reversed_head10)}") # Expected: [-4, -3, -2, -1]

test_reverse_list()