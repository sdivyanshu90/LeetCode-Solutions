from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def search(node):
            if not node:
                return 
            if low <= node.val <= high:
                self.ans += node.val
                search(node.left)
                search(node.right)
            elif node.val < low:
                search(node.right)
            elif node.val > high:
                search(node.left)
        self.ans = 0
        search(root)
        return self.ans

def test_range_sum_bst():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right.right = TreeNode(18)
    low1, high1 = 7, 15
    print(solution.rangeSumBST(root1, low1, high1))  # Expected output: 32

    # Test case 2
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.right = TreeNode(15)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(7)
    root2.left.right.left = TreeNode(6)
    root2.right.right = TreeNode(18)
    low2, high2 = 6, 10
    print(solution.rangeSumBST(root2, low2, high2))  # Expected output: 23

    # Test case 3
    root3 = None
    low3, high3 = 1, 100
    print(solution.rangeSumBST(root3, low3, high3))  # Expected output: 0

    # Test case 4
    root4 = TreeNode(5)
    root4.left = TreeNode(3)
    root4.right = TreeNode(8)
    low4, high4 = 4, 7
    print(solution.rangeSumBST(root4, low4, high4))  # Expected output: 5

    # Test case 5
    root5 = TreeNode(1)
    low5, high5 = 0, 2
    print(solution.rangeSumBST(root5, low5, high5))  # Expected output: 1
    
test_range_sum_bst()