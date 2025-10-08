from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def test_hasCycle():
    solution = Solution()
    
    # Test Case 1: List with a cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle here
    
    print(solution.hasCycle(node1))  # Expected output: True

    # Test Case 2: List without a cycle
    nodeA = ListNode(1)
    nodeB = ListNode(2)
    
    nodeA.next = nodeB  # No cycle here
    
    print(solution.hasCycle(nodeA))  # Expected output: False

    # Test Case 3: Single node without a cycle
    single_node = ListNode(1)
    
    print(solution.hasCycle(single_node))  # Expected output: False

    # Test Case 4: Single node with a cycle (node points to itself)
    single_node_cycle = ListNode(1)
    single_node_cycle.next = single_node_cycle  # Creates a cycle here
    
    print(solution.hasCycle(single_node_cycle))  # Expected output: True

    # Test Case 5: Empty list
    print(solution.hasCycle(None))  # Expected output: False

test_hasCycle()