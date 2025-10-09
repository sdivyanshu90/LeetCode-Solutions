from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return

        temp_arr = []
        temp = head
        while temp is not None:
            temp_arr.append(temp.val)
            temp = temp.next

        i = 0
        temp_arr.sort()
        temp = head
        while temp is not None:
            temp.val = temp_arr[i]
            i = i + 1
            temp = temp.next

        return head

def test_insertion_sort_list():
    sol = Solution()
    
    # Helper function to convert list to linked list
    def to_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    # Helper function to convert linked list to list
    def to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    # Test case 1
    head = to_linked_list([4, 2, 1, 3])
    sorted_head = sol.insertionSortList(head)
    print(to_list(sorted_head)) # Expected output: [1, 2, 3, 4]
    
    # Test case 2
    head = to_linked_list([-1, 5, 3, 4, 0])
    sorted_head = sol.insertionSortList(head)
    print(to_list(sorted_head)) # Expected output: [-1, 0, 3, 4, 5]

    # Test case 3
    head = to_linked_list([-100, -300, -200, -100])
    sorted_head = sol.insertionSortList(head)
    print(to_list(sorted_head)) # Expected output: [-300, -200, -100, -100]

    # Test case 4
    head = to_linked_list([1])
    sorted_head = sol.insertionSortList(head)
    print(to_list(sorted_head)) # Expected output: [1]

    # Test case 5
    head = to_linked_list([2, 1, 3, 5, 4])
    sorted_head = sol.insertionSortList(head)
    print(to_list(sorted_head)) # Expected output: [1, 2, 3, 4, 5]

test_insertion_sort_list()