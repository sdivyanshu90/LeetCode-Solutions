from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def height(node=root):
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            chord = le = ri = 0
            if node.left:
                le = height(node.left)
                chord += 1 + le
            if node.right:
                ri = height(node.right)
                chord += 1 + ri
            self.diameter = max(chord, self.diameter)
            return 1+max(le, ri)
        height()
        return self.diameter

def test_diameter_of_binary_tree():
    s = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    print(s.diameterOfBinaryTree(root1)) # Expected output: 3

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(s.diameterOfBinaryTree(root2)) # Expected output: 1

    # Test case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(5)
    root3.right.right = TreeNode(6)
    root3.left.left.left = TreeNode(7)
    print(s.diameterOfBinaryTree(root3)) # Expected output: 5

    # Test case 4
    root4 = None
    print(s.diameterOfBinaryTree(root4)) # Expected output: 0

    # Test case 5
    root5 = TreeNode(1)
    print(s.diameterOfBinaryTree(root5)) # Expected output: 0

test_diameter_of_binary_tree()