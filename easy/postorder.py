from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        if not root:
            return result
        self._traverse_postorder(root, result)
        return result

    def _traverse_postorder(
        self, current_node: "Node", postorder_list: List[int]
    ) -> None:
        if not current_node:
            return

        for child_node in current_node.children:
            if child_node is None:
                continue
            self._traverse_postorder(child_node, postorder_list)

        postorder_list.append(current_node.val)

def test_postorder():
    s = Solution()

    # Test case 1
    root1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print(s.postorder(root1))  # Expected output: [5, 6, 3, 2, 4, 1]

    # Test case 2
    root2 = Node(1)
    print(s.postorder(root2))  # Expected output: [1]

    # Test case 3
    root3 = Node(1, [])
    print(s.postorder(root3))  # Expected output: [1]

    # Test case 4
    root4 = Node(1, [Node(2), Node(3, [Node(4), Node(5)]), Node(6)])
    print(s.postorder(root4))  # Expected output: [2, 4, 5, 3, 6, 1]

    # Test case 5
    root5 = Node(10, [Node(20), Node(30, [Node(40)])])
    print(s.postorder(root5))  # Expected output: [20, 40, 30, 10]

test_postorder()