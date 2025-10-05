from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr = head

        while True:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            if not curr:
                break
        return head

def test_delete_duplicates():
    solution = Solution()

    # Test case 1
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Test case 2
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Test case 3
    head = None
    result = solution.deleteDuplicates(head)
    if not result:
        print("None")

    # Test case 4
    head = ListNode(1)
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Test case 5
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    result = solution.deleteDuplicates(head)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

test_delete_duplicates()