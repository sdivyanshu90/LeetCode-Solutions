from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff

def test_min_diff_in_bst():
    solution = Solution()
    
    # Test case 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(solution.minDiffInBST(root)) # Expected: 1
    
    # Test case 2
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    print(solution.minDiffInBST(root)) # Expected: 1
    
    # Test case 3
    root = TreeNode(27)
    root.left = TreeNode(14)
    root.right = TreeNode(35)
    root.left.right = TreeNode(19)
    print(solution.minDiffInBST(root)) # Expected: 5
    
    # Test case 4
    root = TreeNode(90)
    root.left = TreeNode(69)
    root.right = TreeNode(91)
    root.left.right = TreeNode(89)
    print(solution.minDiffInBST(root)) # Expected: 1

    # Test case 5
    root = TreeNode(236)
    root.left = TreeNode(104)
    root.right = TreeNode(701)
    root.left.right = TreeNode(227)
    root.right.right = TreeNode(911)
    print(solution.minDiffInBST(root)) # Expected: 9

test_min_diff_in_bst()