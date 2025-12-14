from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

def test_middle_node():
    solution = Solution()

    # Test case 1
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    middle1 = solution.middleNode(head1)
    print(middle1.val)  # Expected output: 3

    # Test case 2
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(5)
    head2.next.next.next.next.next = ListNode(6)
    middle2 = solution.middleNode(head2)
    print(middle2.val)  # Expected output: 4

    # Test case 3
    head3 = ListNode(10)
    middle3 = solution.middleNode(head3)
    print(middle3.val)  # Expected output: 10

    # Test case 4
    head4 = ListNode(1)
    head4.next = ListNode(2)
    head4.next.next = ListNode(3)
    head4.next.next.next = ListNode(4)
    head4.next.next.next.next = ListNode(5)
    head4.next.next.next.next.next = ListNode(6)
    head4.next.next.next.next.next.next = ListNode(7)
    middle4 = solution.middleNode(head4)
    print(middle4.val)  # Expected output: 4

    # Test case 5
    head5 = ListNode(1)
    head5.next = ListNode(2)
    middle5 = solution.middleNode(head5)
    print(middle5.val)  # Expected output: 2

test_middle_node()