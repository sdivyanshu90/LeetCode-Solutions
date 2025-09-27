from typing import List, Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

def test_merge_k_lists():
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
    lists = [create_linked_list([1, 4, 5]), create_linked_list([1, 3, 4]), create_linked_list([2, 6])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [1, 1, 2, 3, 4, 4, 5, 6]

    # Test case 2
    lists = []
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: []

    # Test case 3
    lists = [create_linked_list([])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: []

    # Test case 4
    lists = [create_linked_list([2]), create_linked_list([]), create_linked_list([-1])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [-1, 2]

    # Test case 5
    lists = [create_linked_list([1, 3, 5]), create_linked_list([2, 4, 6]), create_linked_list([0, 7, 8])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Test case 6
    lists = [create_linked_list([1, 2, 3]), create_linked_list([4, 5, 6]), create_linked_list([7, 8, 9])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test case 7
    lists = [create_linked_list([1]), create_linked_list([0]), create_linked_list([2])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [0, 1, 2]

    # Test case 8
    lists = [create_linked_list([-10, -5, 0]), create_linked_list([-6, -3, 2]), create_linked_list([-1, 1, 3])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [-10, -6, -5, -3, -1, 0, 1, 2, 3]

    # Test case 9
    lists = [create_linked_list([5, 10, 15]), create_linked_list([3, 6, 9]), create_linked_list([8, 12, 20])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [3, 5, 6, 8, 9, 10, 12, 15, 20]  

    # Test case 10
    lists = [create_linked_list([1, 4, 7]), create_linked_list([2, 5, 8]), create_linked_list([3, 6, 9])]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

test_merge_k_lists()