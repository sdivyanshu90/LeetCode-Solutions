from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = dummy.next
        
        for i in range(1,left):
            cur = cur.next
            prev = prev.next
                
        for i in range(right-left):
            temp = cur.next
            cur.next = temp.next
            temp.next  = prev.next
            prev.next = temp
        
        return dummy.next

def test_reverse_between():
    solution = Solution()

    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        dummy = ListNode(0)
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list
    def linked_list_to_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    # Test Case 1
    head = create_linked_list([1,2,3,4,5])
    left, right = 2, 4
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [1,4,3,2,5]

    # Test Case 2
    head = create_linked_list([5])
    left, right = 1, 1
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [5]

    # Test Case 3
    head = create_linked_list([1,2])
    left, right = 1, 2
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [2,1]

    # Test Case 4
    head = create_linked_list([1,2,3])
    left, right = 1, 2
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [2,1,3]

    # Test Case 5
    head = create_linked_list([1,2,3])
    left, right = 2, 3
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [1,3,2]

    # Test Case 6
    head = create_linked_list([1,2,3,4,5])
    left, right = 1, 5
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [5,4,3,2,1]

    # Test Case 7
    head = create_linked_list([1,2,3,4,5])
    left, right = 3, 3
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [1,2,3,4,5]

    # Test Case 8
    head = create_linked_list([1,2,3,4,5])
    left, right = 4, 5
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [1,2,3,5,4]

    # Test Case 9
    head = create_linked_list([1])
    left, right = 1, 1
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [1]

    # Test Case 10
    head = create_linked_list([1,2,3,4,5])
    left, right = 2, 5
    new_head = solution.reverseBetween(head, left, right)
    print(linked_list_to_list(new_head)) # Output: [1,5,4,3,2]

test_reverse_between()