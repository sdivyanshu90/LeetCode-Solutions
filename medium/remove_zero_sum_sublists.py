from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        root = ListNode(0, head)
        summ, d, node = 0, {}, root
        while node:
            summ += node.val
            if summ in d:
                prev = d[summ]
                tmp = prev.next
                tmp_sum = summ
                while tmp != node:
                    tmp_sum += tmp.val
                    if tmp_sum in d and d[tmp_sum] == tmp:
                        d.pop(tmp_sum)
                    tmp = tmp.next
                prev.next = node.next
                node = prev
            else:
                d[summ] = node
            node = node.next
        return root.next

def test_remove_zero_sum_sublists():
    solution = Solution()

    # Test Case 1
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(-3)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(1)
    result = solution.removeZeroSumSublists(head)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output) # Expected Output: [3, 1]

    # Test Case 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(-3)
    head.next.next.next.next = ListNode(4)
    result = solution.removeZeroSumSublists(head)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output) # Expected Output: [1, 2, 4]

    # Test Case 3
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(-6)
    head.next.next.next.next = ListNode(4)
    result = solution.removeZeroSumSublists(head)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output) # Expected Output: [4]

    # Test Case 4
    head = ListNode(0)
    head.next = ListNode(0)
    head.next.next = ListNode(0)
    result = solution.removeZeroSumSublists(head)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output) # Expected Output: []

    # Test Case 5
    head = None
    result = solution.removeZeroSumSublists(head)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output) # Expected Output: []

test_remove_zero_sum_sublists()