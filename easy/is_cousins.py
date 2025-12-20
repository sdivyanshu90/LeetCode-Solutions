from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        queue = deque([(root, None, 0)])
        x_info = y_info = None
        
        while queue:
            for _ in range(len(queue)):
                node, parent, depth = queue.popleft()

                if node.val == x:
                    x_info = (parent, depth)
                if node.val == y:
                    y_info = (parent, depth)

                if node.left:
                    queue.append((node.left, node, depth + 1))
                if node.right:
                    queue.append((node.right, node, depth + 1))

            if x_info and y_info:
                return x_info[1] == y_info[1] and x_info[0] != y_info[0]

        return False

def test_is_cousins():
    solution = Solution()
    
    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    print(solution.isCousins(root, 4, 5))  # Expected output: True

    # Test case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(solution.isCousins(root, 4, 3))  # Expected output: False

    # Test case 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print(solution.isCousins(root, 2, 3))  # Expected output: False

    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    print(solution.isCousins(root, 4, 5))  # Expected output: True

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    print(solution.isCousins(root, 4, 2))  # Expected output: False

test_is_cousins()