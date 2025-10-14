from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        
        return curr is None


def create_linked_list(values: List) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List:
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


def test_is_palindrome():
    s = Solution()

    # Test Case 1: Palindrome with an odd number of nodes
    head1 = create_linked_list([1, 2, 3, 2, 1])
    print(f"\nInput: {linked_list_to_list(head1)}")
    print(f"Output: {s.isPalindrome(head1)}") # Expected: True

    # Test Case 2: Palindrome with an even number of nodes
    head2 = create_linked_list([1, 2, 2, 1])
    print(f"\nInput: {linked_list_to_list(head2)}")
    print(f"Output: {s.isPalindrome(head2)}") # Expected: True

    # Test Case 3: Not a palindrome
    head3 = create_linked_list([1, 2, 3, 4, 5])
    print(f"\nInput: {linked_list_to_list(head3)}")
    print(f"Output: {s.isPalindrome(head3)}") # Expected: False

    # Test Case 4: Empty list (edge case)
    head4 = create_linked_list([])
    print(f"\nInput: {linked_list_to_list(head4)}")
    print(f"Output: {s.isPalindrome(head4)}") # Expected: True

    # Test Case 5: Single node list (edge case)
    head5 = create_linked_list([42])
    print(f"\nInput: {linked_list_to_list(head5)}")
    print(f"Output: {s.isPalindrome(head5)}") # Expected: True

    # Test Case 6: Two nodes that are not a palindrome
    head6 = create_linked_list([1, 0])
    print(f"\nInput: {linked_list_to_list(head6)}")
    print(f"Output: {s.isPalindrome(head6)}") # Expected: False

    # Test Case 7: Two nodes that are a palindrome
    head7 = create_linked_list([5, 5])
    print(f"\nInput: {linked_list_to_list(head7)}")
    print(f"Output: {s.isPalindrome(head7)}") # Expected: True

    # Test Case 8: A longer list that is not a palindrome
    head8 = create_linked_list([1, 2, 3, 4, 2, 1])
    print(f"\nInput: {linked_list_to_list(head8)}")
    print(f"Output: {s.isPalindrome(head8)}") # Expected: False

    # Test Case 9: All elements are the same
    head9 = create_linked_list([7, 7, 7, 7, 7])
    print(f"\nInput: {linked_list_to_list(head9)}")
    print(f"Output: {s.isPalindrome(head9)}") # Expected: True

    # Test Case 10: Mismatch at the very end
    head10 = create_linked_list([1, 2, 3, 2, 5])
    print(f"\nInput: {linked_list_to_list(head10)}")
    print(f"Output: {s.isPalindrome(head10)}") # Expected: False

test_is_palindrome()