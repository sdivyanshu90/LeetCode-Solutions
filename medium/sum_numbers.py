from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur,num):
            if not cur:
                return 0
            num = num * 10 + cur.val
            if not cur.left and not cur.right:
                return num
            return dfs(cur.left, num) + dfs(cur.right, num)
        return dfs(root,0)

def test_sum_numbers():
    solution = Solution()
    
    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.sumNumbers(root))  # Expected output: 25

    # Test case 2
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    print(solution.sumNumbers(root))  # Expected output: 1026

    # Test case 3
    root = None
    print(solution.sumNumbers(root))  # Expected output: 0

    # Test case 4
    root = TreeNode(0)
    print(solution.sumNumbers(root))  # Expected output: 0

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(solution.sumNumbers(root))  # Expected output: 422

test_sum_numbers()