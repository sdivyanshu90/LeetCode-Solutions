from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, 0, float("inf"))]
        while stack:
            node, mx, mn = stack.pop()
            if not node:
                continue
            result = max(result, mx-node.val, node.val-mn)
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            stack.append((node.left, mx, mn))
            stack.append((node.right, mx, mn))
        return result

def test_max_ancestor_diff():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(8)
    root1.left = TreeNode(3)
    root1.right = TreeNode(10)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(6)
    root1.left.right.left = TreeNode(4)
    root1.left.right.right = TreeNode(7)
    root1.right.right = TreeNode(14)
    root1.right.right.left = TreeNode(13)
    print(solution.maxAncestorDiff(root1))  # Expected output: 7

    # Test case 2
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(0)
    root2.right.right.left = TreeNode(3)
    print(solution.maxAncestorDiff(root2))  # Expected output: 3

    # Test case 3
    root3 = TreeNode(5)
    root3.left = TreeNode(2)
    root3.right = TreeNode(13)
    print(solution.maxAncestorDiff(root3))  # Expected output: 8

    # Test case 4
    root4 = TreeNode(0)
    print(solution.maxAncestorDiff(root4))  # Expected output: 0

    # Test case 5
    root5 = TreeNode(4)
    root5.left = TreeNode(9)
    root5.right = TreeNode(2)
    root5.left.left = TreeNode(3)
    root5.left.right = TreeNode(5)
    root5.right.right = TreeNode(7)
    print(solution.maxAncestorDiff(root5))  # Expected output: 6

test_max_ancestor_diff()