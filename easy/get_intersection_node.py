from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA

def test_get_intersection_node():
    sol = Solution()
    
    # Helper function to create linked list from list and return head and tail
    def create_linked_list(lst):
        if not lst:
            return None, None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head, current  # return head and tail
    
    # Test case 1: Intersection at node with value 8
    common, _ = create_linked_list([8, 4, 5])
    headA, _ = create_linked_list([4, 1])
    headB, _ = create_linked_list([5, 0, 1])
    # Attach common part
    tailA = headA
    while tailA.next:
        tailA = tailA.next
    tailA.next = common
    tailB = headB
    while tailB.next:
        tailB = tailB.next
    tailB.next = common
    print(sol.getIntersectionNode(headA, headB).val) # Expected output: 8
    
    # Test case 2: No intersection
    headA, _ = create_linked_list([2, 6, 4])
    headB, _ = create_linked_list([1, 5])
    print(sol.getIntersectionNode(headA, headB)) # Expected output: None
    
    # Test case 3: Intersection at node with value 2
    common, _ = create_linked_list([2, 4])
    headA, _ = create_linked_list([1])
    headB, _ = create_linked_list([3])
    # Attach common part
    tailA = headA
    while tailA.next:
        tailA = tailA.next
    tailA.next = common
    tailB_next = headB
    while tailB_next.next:
        tailB_next = tailB_next.next
    tailB_next.next = common
    print(sol.getIntersectionNode(headA, headB).val) # Expected output: 2

    # Test case 4: Intersection at head
    common, _ = create_linked_list([7, 8, 9])
    headA = common
    headB = common
    print(sol.getIntersectionNode(headA, headB).val) # Expected output: 7

    # Test case 5: Intersection at last node
    common, _ = create_linked_list([10])
    headA, _ = create_linked_list([1, 2, 3])
    headB, _ = create_linked_list([4, 5, 6])
    # Attach common part
    tailA = headA
    while tailA.next:
        tailA = tailA.next
    tailA.next = common
    tailB = headB
    while tailB.next:
        tailB = tailB.next
    tailB.next = common
    print(sol.getIntersectionNode(headA, headB).val) # Expected output: 10

test_get_intersection_node()