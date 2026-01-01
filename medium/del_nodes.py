from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        if not root:
            return []

        to_delete_set = set(to_delete)
        forest = []

        nodes_queue = deque([root])

        while nodes_queue:
            current_node = nodes_queue.popleft()

            if current_node.left:
                nodes_queue.append(current_node.left)
                if current_node.left.val in to_delete_set:
                    current_node.left = None

            if current_node.right:
                nodes_queue.append(current_node.right)
                if current_node.right.val in to_delete_set:
                    current_node.right = None

            if current_node.val in to_delete_set:
                if current_node.left:
                    forest.append(current_node.left)
                if current_node.right:
                    forest.append(current_node.right)

        if root.val not in to_delete_set:
            forest.append(root)

        return forest


def test_del_nodes():
    solution = Solution()

    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    to_delete = [3, 5]
    result = solution.delNodes(root, to_delete)
    print(len(result))  # Expected output: 3

    # Test case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    to_delete = [1, 2]
    result = solution.delNodes(root, to_delete)
    print(len(result))  # Expected output: 1

    # Test case 3
    root = TreeNode(1)
    to_delete = [1]
    result = solution.delNodes(root, to_delete)
    print(len(result))  # Expected output: 0

    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    to_delete = [2]
    result = solution.delNodes(root, to_delete)
    print(len(result))  # Expected output: 2

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    to_delete = [4]
    result = solution.delNodes(root, to_delete)
    print(len(result))  # Expected output: 1

test_del_nodes()