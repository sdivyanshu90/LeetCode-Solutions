from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ""

        if head is None:
            return
        
        temp = head
        while temp is not None:
            res += str(temp.val)
            temp = temp.next
        
        return int(res, 2)

def test_get_decimal_value():
    solution = Solution()

    # Test case 1
    head = ListNode(1, ListNode(0, ListNode(1)))
    print(solution.getDecimalValue(head))  # Expected output: 5

    # Test case 2
    head = ListNode(0)
    print(solution.getDecimalValue(head))  # Expected output: 0

    # Test case 3
    head = ListNode(1)
    print(solution.getDecimalValue(head))  # Expected output: 1

    # Test case 4
    head = ListNode(1, ListNode(0))
    print(solution.getDecimalValue(head))  # Expected output: 2

    # Test case 5
    head = ListNode(1, ListNode(1, ListNode(1)))
    print(solution.getDecimalValue(head))  # Expected output: 7

test_get_decimal_value()