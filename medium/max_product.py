from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def dfs(node):
            if not node: return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            curr_sum = node.val + left_sum + right_sum
            all_sums.append(curr_sum)
            return curr_sum

        total_sum = dfs(root)
        max_p = 0
        for s in all_sums:
            max_p = max(max_p, s * (total_sum - s))
        return max_p % (10**9 + 7)

def test_maxProduct():
    solution = Solution()

    # Test case 1
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    expected = 6
    print(solution.maxProduct(root))  # Expected Output: 9

    # Test case 2
    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    expected = 110
    print(solution.maxProduct(root))  # Expected Output: 50

    # Test case 3
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    expected = 12
    print(solution.maxProduct(root))  # Expected Output: 24

    # Test case 4
    root = TreeNode(1)
    expected = 0
    print(solution.maxProduct(root))  # Expected Output: 0

    # Test case 5
    root = TreeNode(1, TreeNode(2), None)
    expected = 2
    print(solution.maxProduct(root))  # Expected Output: 2

test_maxProduct()