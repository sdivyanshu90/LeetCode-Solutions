from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head
        
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            
            current = current.next
        
        before.next = after_head.next
        after.next = None        
        return before_head.next

def test_partition():
    solution = Solution()

    # Test case 1
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    x = 3
    result = solution.partition(head, x)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Test case 2
    head = ListNode(2)
    head.next = ListNode(1)
    x = 2
    result = solution.partition(head, x)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Test case 3
    head = None
    x = 0
    result = solution.partition(head, x)
    if result is None:
        print("None")

    # Test case 4
    head = ListNode(3)
    head.next = ListNode(5)
    head.next.next = ListNode(8)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(10)
    head.next.next.next.next.next = ListNode(2)
    head.next.next.next.next.next.next = ListNode(1)
    x = 5
    result = solution.partition(head, x)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

    # Test case 5
    head = ListNode(1)
    x = 0
    result = solution.partition(head, x)
    while result:
        print(result.val, end=" -> ")
        result = result.next
    print("None")

test_partition()