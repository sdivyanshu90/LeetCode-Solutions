from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        current = head
        while current:
            copy_node = Node(current.val)
            copy_node.next = current.next
            current.next = copy_node
            current = copy_node.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        current = head
        new_head = head.next
        while current:
            copied_node = current.next
            current.next = copied_node.next
            if copied_node.next:
                copied_node.next = copied_node.next.next
            current = current.next

        return new_head

def test_copyRandomList():
    solution = Solution()
    
    # Test Case 1
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1
    
    copied_list_head = solution.copyRandomList(node1)
    
    # Print the copied list to verify
    current = copied_list_head
    while current:
        random_val = current.random.val if current.random else None
        print(f'Node val: {current.val}, Random points to: {random_val}')
        current = current.next
    # Expected output: 
    # Node val: 7, Random points to: None
    # Node val: 13, Random points to: 7
    # Node val: 11, Random points to: 1
    # Node val: 10, Random points to: 11
    # Node val: 1, Random points to: 7

    # Test Case 2: Empty list
    print(solution.copyRandomList(None))  # Expected output: None

    # Test Case 3: Single node with no random pointer
    single_node = Node(1)
    copied_single_node = solution.copyRandomList(single_node)
    print(f'Node val: {copied_single_node.val}, Random points to: {copied_single_node.random}')  # Expected output: Node val: 1, Random points to: None

    # Test Case 4: Single node with random pointer to itself
    single_node_self_random = Node(1)
    single_node_self_random.random = single_node_self_random
    copied_single_node_self_random = solution.copyRandomList(single_node_self_random)
    print(f'Node val: {copied_single_node_self_random.val}, Random points to: {copied_single_node_self_random.random.val}')  # Expected output: Node val: 1, Random points to: 1

    # Test Case 5: Two nodes with cross random pointers
    nodeA = Node(1)
    nodeB = Node(2)
    nodeA.next = nodeB
    nodeA.random = nodeB
    nodeB.random = nodeA
    copied_list_head_2 = solution.copyRandomList(nodeA)
    current = copied_list_head_2
    while current:
        random_val = current.random.val if current.random else None
        print(f'Node val: {current.val}, Random points to: {random_val}')
        current = current.next  
        
    # Expected output: 
    # Node val: 1, Random points to: 1
    # Node val: 1, Random points to: 2
    # Node val: 2, Random points to: 1

test_copyRandomList()