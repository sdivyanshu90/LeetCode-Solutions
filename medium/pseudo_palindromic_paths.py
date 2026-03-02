from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def preorder(node, path):
            nonlocal count
            if node:
                path = path ^ (1 << node.val)
                if node.left is None and node.right is None:
                    if path & (path - 1) == 0:
                        count += 1
                else:                    
                    preorder(node.left, path)
                    preorder(node.right, path) 
        
        count = 0
        preorder(root, 0)
        return count

def test_pseudo_palindromic_paths():
    solution = Solution()

    # Test case 1
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    print(solution.pseudoPalindromicPaths(root))  # Expected output: 1

    # Test case 2
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = None
    root.left.right = None
    root.right.left = None
    root.right.right = None
    print(solution.pseudoPalindromicPaths(root))  # Expected output: 0

    # Test case 3
    root = TreeNode(9)
    print(solution.pseudoPalindromicPaths(root))  # Expected output: 1

    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.pseudoPalindromicPaths(root))  # Expected output: 0

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    print(solution.pseudoPalindromicPaths(root))  # Expected output: 2

test_pseudo_palindromic_paths()