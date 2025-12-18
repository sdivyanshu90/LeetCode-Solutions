from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        seen = set()
        def dfs(node):
            if node:
                seen.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(seen) == 1

def test_is_unival_tree():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(1)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(1)
    root1.right.right = TreeNode(1)
    print(solution.isUnivalTree(root1))  # Expected output: True

    # Test case 2
    root2 = TreeNode(2)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(2)
    print(solution.isUnivalTree(root2))  # Expected output: False

    # Test case 3
    root3 = TreeNode(3)
    print(solution.isUnivalTree(root3))  # Expected output: True

    # Test case 4
    root4 = TreeNode(4)
    root4.left = TreeNode(4)
    root4.right = TreeNode(4)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(4)
    root4.right.left = TreeNode(4)
    root4.right.right = TreeNode(5)
    print(solution.isUnivalTree(root4))  # Expected output: False

    # Test case 5
    root5 = None
    print(solution.isUnivalTree(root5))  # Expected output: False

test_is_unival_tree()