from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]

def test_lca_deepest_leaves():
    solution = Solution()

    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    result = solution.lcaDeepestLeaves(root)
    print(result.val)  # Expected output: 2

    # Test case 2
    root = TreeNode(1)
    result = solution.lcaDeepestLeaves(root)
    print(result.val)  # Expected output: 1

    # Test case 3
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    result = solution.lcaDeepestLeaves(root)
    print(result.val)  # Expected output: 2

    # Test case 4
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(4)
    result = solution.lcaDeepestLeaves(root)
    print(result.val)  # Expected output: 0

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    result = solution.lcaDeepestLeaves(root)
    print(result.val)  # Expected output: 1

test_lca_deepest_leaves()