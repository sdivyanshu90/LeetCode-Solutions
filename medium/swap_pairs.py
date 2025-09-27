from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp = head
        while temp is not None and temp.next is not None:
            temp.val, temp.next.val = temp.next.val, temp.val
            temp = temp.next.next

        return head

def test_swap_pairs():
    sol = Solution()

    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test case 1
    head = create_linked_list([1, 2, 3, 4])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 4, 3]

    # Test case 2
    head = create_linked_list([])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: []

    # Test case 3
    head = create_linked_list([1])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [1]

    # Test case 4
    head = create_linked_list([1, 2, 3])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 3]

    # Test case 5
    head = create_linked_list([1, 2, 3, 4, 5])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 4, 3, 5]

    # Test case 6
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 4, 3, 6, 5]

    # Test case 7
    head = create_linked_list([1, 2])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1]

    # Test case 8
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 4, 3, 6, 5, 7]

    # Test case 9
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 4, 3, 6, 5, 8, 7]

    # Test case 10
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    swapped = sol.swapPairs(head)
    print(linked_list_to_list(swapped))  # Expected output: [2, 1, 4, 3, 6, 5, 8, 7, 9]

test_swap_pairs()