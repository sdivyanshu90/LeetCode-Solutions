from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        string = str(root.val)
        if root.left or root.right:
            string += f'({self.tree2str(root.left)})'
        if root.right:
            string += f'({self.tree2str(root.right)})'
        return string

def test_tree2str():
    s = Solution()

    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(s.tree2str(root))  # Expected output: "1(2(4))(3)"

    # Test case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    print(s.tree2str(root))  # Expected output: "1(2()(4))(3)"

    # Test case 3
    root = TreeNode(1)
    print(s.tree2str(root))  # Expected output: "1"

    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(s.tree2str(root))  # Expected output: "1(2)"

    # Test case 5
    root = TreeNode(1)
    root.right = TreeNode(3)
    print(s.tree2str(root))  # Expected output: "1()(3)"

test_tree2str()