from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        return head

def test_reorder_list():
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
    head = to_linked_list([1, 2, 3, 4])
    sol.reorderList(head)
    print(to_list(head)) # Expected output: [1, 4, 2, 3]
    
    # Test case 2
    head = to_linked_list([1, 2, 3, 4, 5])
    sol.reorderList(head)
    print(to_list(head)) # Expected output: [1, 5, 2, 4, 3]
    
    # Test case 3 (single element)
    head = to_linked_list([1])
    sol.reorderList(head)
    print(to_list(head)) # Expected output: [1]
    
    # Test case 4 (two elements)
    head = to_linked_list([1, 2])
    sol.reorderList(head)
    print(to_list(head)) # Expected output: [1, 2]
    
    # Test case 5 
    head = to_linked_list([0,1,2,3,4,5,6,7,8,9])
    sol.reorderList(head)
    print(to_list(head)) # Expected output: [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]

test_reorder_list()