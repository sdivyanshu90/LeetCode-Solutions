from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        while l1 != None:
            n1 = n1 * 10 + l1.val
            l1 = l1.next
        
        while l2 != None:
            n2 = n2 * 10 + l2.val
            l2= l2.next
        dummyList = dummy = ListNode(0)

        for i in str(n1 + n2):
            dummy.next = ListNode(int(i))
            dummy = dummy.next
        return dummyList.next

def test_add_two_numbers():
    s = Solution()

    # Test case 1
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")  # Expected output: 7 -> 8 -> 0 -> 7 ->
        result = result.next
    print("None")

    # Test case 2
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")  # Expected output: 8 -> 0 -> 7 ->
        result = result.next
    print("None")

    # Test case 3
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")  # Expected output: 0 ->
        result = result.next
    print("None")

    # Test case 4
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    l2 = ListNode(1)
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")  # Expected output: 1 -> 0 -> 0 -> 0 -> 0 ->
        result = result.next
    print("None")

    # Test case 5
    l1 = ListNode(1)
    l2 = ListNode(9, ListNode(9, ListNode(9)))
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" -> ")  # Expected output: 1 -> 0 -> 0 -> 0 ->
        result = result.next
    print("None")

test_add_two_numbers()