from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(current):
            if current == None: 
                return 0

            left_coins = dfs(current.left)
            right_coins = dfs(current.right)
            self.moves += abs(left_coins) + abs(right_coins)
            return (current.val - 1) + left_coins + right_coins
        dfs(root)
        return self.moves

def test_distribute_coins():
    solution = Solution()
    
    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    print(solution.distributeCoins(root))  # Expected output: 2

    # Test case 2
    root = TreeNode(0)
    root.left = TreeNode(3)
    root.right = TreeNode(0)
    print(solution.distributeCoins(root))  # Expected output: 3

    # Test case 3
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(2)
    print(solution.distributeCoins(root))  # Expected output: 2

    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    print(solution.distributeCoins(root))  # Expected output: 2

    # Test case 5
    root = TreeNode(4)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    root.right.right = TreeNode(0)
    print(solution.distributeCoins(root))  # Expected output: 4

test_distribute_coins()