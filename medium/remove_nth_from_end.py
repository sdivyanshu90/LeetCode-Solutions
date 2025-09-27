from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        prev = None

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        prev.next = slow.next
        return head

def test_remove_nth_from_end():
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
    head = create_linked_list([1, 2, 3, 4, 5])
    n = 2
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 2
    head = create_linked_list([1])
    n = 1
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 3
    head = create_linked_list([1, 2])
    n = 1
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 4
    head = create_linked_list([1, 2])
    n = 2
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 5
    head = create_linked_list([1, 2, 3])
    n = 3
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 6
    head = create_linked_list([1, 2, 3])
    n = 1
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 7
    head = create_linked_list([1, 2, 3])
    n = 2
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 8
    head = create_linked_list([1, 2, 3, 4])
    n = 4
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 9
    head = create_linked_list([1, 2, 3, 4])
    n = 3
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

    # Test case 10
    head = create_linked_list([1, 2, 3, 4])
    n = 2
    print(linked_list_to_list(sol.removeNthFromEnd(head, n)))

test_remove_nth_from_end()