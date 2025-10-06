from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

def test_min_depth():
    solution = Solution()

    # Test case 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(solution.minDepth(root1))  # Expected output: 2

    # Test case 2: Single node tree
    root2 = TreeNode(1)
    print(solution.minDepth(root2))  # Expected output: 1

    # Test case 3: Empty tree
    print(solution.minDepth(None))  # Expected output: 0

    # Test case 4: Left-skewed tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    print(solution.minDepth(root4))  # Expected output: 3

    # Test case 5: Right-skewed tree
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    print(solution.minDepth(root5))  # Expected output: 3

test_min_depth()