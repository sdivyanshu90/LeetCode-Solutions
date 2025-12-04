from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        sizes, rm = [length // k] * k, length % k
        for i in range(rm):
            sizes[i] += 1

        res = []
        curr = head
        for size in sizes:
            if not size:
                res.append(None)
                continue
            res.append(curr)
            for i in range(size-1):
                curr = curr.next
            print(curr.val)
            curr.next, curr = None, curr.next
        return res

def test_split_list_to_parts():
    solution = Solution()

    # Helper function to create linked list from list
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # Helper function to print linked list parts
    def print_linked_list_parts(parts):
        for part in parts:
            vals = []
            while part:
                vals.append(part.val)
                part = part.next
            print(vals)

    # Test Case 1
    head = create_linked_list([1, 2, 3])
    k = 5
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1], [2], [3], [], []]

    # Test Case 2
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 3
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1,2,3,4], [5,6,7], [8,9,10]]

    # Test Case 3: Empty list
    head = create_linked_list([])
    k = 3
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[], [], []]

    # Test Case 4: Single node list
    head = create_linked_list([1])
    k = 1
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1]]

    # Test Case 5: More parts than nodes
    head = create_linked_list([1, 2])
    k = 4
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1], [2], [], []]

    # Test Case 6: Equal parts
    head = create_linked_list([1, 2, 3, 4])
    k = 2
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1,2], [3,4]]

    # Test Case 7: Large k with single node
    head = create_linked_list([1])
    k = 10
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1], [], [], [], [], [], [], [], [], []]

    # Test Case 8: Large list with small k
    head = create_linked_list(list(range(1, 21)))  # List from 1 to 20
    k = 4
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1-5], [6-10], [11-15], [16-20]]

    # Test Case 9: All nodes in one part
    head = create_linked_list([1, 2, 3, 4, 5])
    k = 1
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1,2,3,4,5]]

    # Test Case 10: Large array with many parts
    head = create_linked_list(list(range(1, 101)))  # List from 1 to 100
    k = 10
    parts = solution.splitListToParts(head, k)
    print_linked_list_parts(parts)  # Expected: [[1-10], [11-20], ..., [91-100]]

test_split_list_to_parts()