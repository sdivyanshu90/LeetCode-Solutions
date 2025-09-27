from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = temp = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1, curr = list1.next, list1
            else:
                curr.next = list2
                list2, curr = list2.next, list2
        if list1 or list2:
            if list1:
                curr.next = list1
            else:
                curr.next = list2
        return temp.next

def test_merge_two_lists():
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
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 1, 2, 3, 4, 4]

    # Test case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: []

    # Test case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [0]

    # Test case 4
    list1 = create_linked_list([5, 6, 7])
    list2 = create_linked_list([1, 2, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6, 7]

    # Test case 5
    list1 = create_linked_list([2, 4, 6])
    list2 = create_linked_list([1, 3, 5])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6]

    # Test case 6
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 1, 1, 1, 1, 1]

    # Test case 7
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4, 6, 8, 10])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test case 8
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([2, 3, 6])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6]

    # Test case 9
    list1 = create_linked_list([0, 9, 10])
    list2 = create_linked_list([5, 7, 8])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [0, 5, 7, 8, 9, 10]

    # Test case 10
    list1 = create_linked_list([1, 2, 4, 6  , 8])
    list2 = create_linked_list([3, 5, 7, 9, 10])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test_merge_two_lists()