from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Deletes a node from a singly-linked list given only access to that node.
        The node to be deleted is not the tail.
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

def create_linked_list(values: List) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List:
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def get_node_by_index(head: Optional[ListNode], index: int) -> Optional[ListNode]:
    current = head
    for i in range(index):
        if not current:
            return None
        current = current.next
    return current

def test_delete_node():
    s = Solution()

    # Test Case 1: Delete a node in the middle
    print("\n--- Test Case 1: Delete from Middle ---")
    head1 = create_linked_list([4, 5, 1, 9])
    node_to_delete1 = get_node_by_index(head1, 1) # Node with value 5
    print(f"Initial list: {linked_list_to_list(head1)}, deleting node with value {node_to_delete1.val}")
    s.deleteNode(node_to_delete1)
    print(f"Final list:   {linked_list_to_list(head1)}") # Expected: [4, 1, 9]

    # Test Case 2: Delete the head of the given list portion
    print("\n--- Test Case 2: Delete the Head ---")
    head2 = create_linked_list([4, 5, 1, 9])
    node_to_delete2 = get_node_by_index(head2, 0) # Node with value 4
    print(f"Initial list: {linked_list_to_list(head2)}, deleting node with value {node_to_delete2.val}")
    s.deleteNode(node_to_delete2)
    print(f"Final list:   {linked_list_to_list(head2)}") # Expected: [5, 1, 9]

    # Test Case 3: Delete the node before the tail
    print("\n--- Test Case 3: Delete Before Tail ---")
    head3 = create_linked_list([4, 5, 1, 9])
    node_to_delete3 = get_node_by_index(head3, 2) # Node with value 1
    print(f"Initial list: {linked_list_to_list(head3)}, deleting node with value {node_to_delete3.val}")
    s.deleteNode(node_to_delete3)
    print(f"Final list:   {linked_list_to_list(head3)}") # Expected: [4, 5, 9]

    # Test Case 4: List with duplicate values
    print("\n--- Test Case 4: List with Duplicates ---")
    head4 = create_linked_list([1, 2, 3, 2, 4])
    node_to_delete4 = get_node_by_index(head4, 1) # The first node with value 2
    print(f"Initial list: {linked_list_to_list(head4)}, deleting node with value {node_to_delete4.val}")
    s.deleteNode(node_to_delete4)
    print(f"Final list:   {linked_list_to_list(head4)}") # Expected: [1, 3, 2, 4]

    # Test Case 5: Minimal three-node list
    print("\n--- Test Case 5: Minimal Middle Deletion ---")
    head5 = create_linked_list([10, 20, 30])
    node_to_delete5 = get_node_by_index(head5, 1) # Node with value 20
    print(f"Initial list: {linked_list_to_list(head5)}, deleting node with value {node_to_delete5.val}")
    s.deleteNode(node_to_delete5)
    print(f"Final list:   {linked_list_to_list(head5)}") # Expected: [10, 30]
    
    # Test Case 6: Minimal two-node list (delete head)
    print("\n--- Test Case 6: Minimal Head Deletion ---")
    head6 = create_linked_list([10, 20])
    node_to_delete6 = get_node_by_index(head6, 0) # Node with value 10
    print(f"Initial list: {linked_list_to_list(head6)}, deleting node with value {node_to_delete6.val}")
    s.deleteNode(node_to_delete6)
    print(f"Final list:   {linked_list_to_list(head6)}") # Expected: [20]
    
    # Test Case 7: Longer list
    print("\n--- Test Case 7: Longer List ---")
    head7 = create_linked_list([1, 2, 3, 4, 5, 6])
    node_to_delete7 = get_node_by_index(head7, 3) # Node with value 4
    print(f"Initial list: {linked_list_to_list(head7)}, deleting node with value {node_to_delete7.val}")
    s.deleteNode(node_to_delete7)
    print(f"Final list:   {linked_list_to_list(head7)}") # Expected: [1, 2, 3, 5, 6]

    # Test Case 8: List with negative numbers
    print("\n--- Test Case 8: List with Negative Numbers ---")
    head8 = create_linked_list([-5, -10, -15, -20])
    node_to_delete8 = get_node_by_index(head8, 2) # Node with value -15
    print(f"Initial list: {linked_list_to_list(head8)}, deleting node with value {node_to_delete8.val}")
    s.deleteNode(node_to_delete8)
    print(f"Final list:   {linked_list_to_list(head8)}") # Expected: [-5, -10, -20]

    # Test Case 9: List with zero
    print("\n--- Test Case 9: List with Zero ---")
    head9 = create_linked_list([1, 2, 0, 4])
    node_to_delete9 = get_node_by_index(head9, 2) # Node with value 0
    print(f"Initial list: {linked_list_to_list(head9)}, deleting node with value {node_to_delete9.val}")
    s.deleteNode(node_to_delete9)
    print(f"Final list:   {linked_list_to_list(head9)}") # Expected: [1, 2, 4]

    # Test Case 10: Delete the second occurrence of a duplicate
    print("\n--- Test Case 10: Delete Second Duplicate ---")
    head10 = create_linked_list([1, 8, 5, 8, 9])
    node_to_delete10 = get_node_by_index(head10, 3) # The second node with value 8
    print(f"Initial list: {linked_list_to_list(head10)}, deleting node with value {node_to_delete10.val}")
    s.deleteNode(node_to_delete10)
    print(f"Final list:   {linked_list_to_list(head10)}") # Expected: [1, 8, 5, 9]

test_delete_node()