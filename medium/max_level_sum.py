from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float('-inf'), 0, 0

        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            sum_at_current_level = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum_at_current_level += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if max_sum < sum_at_current_level:
                max_sum, ans = sum_at_current_level, level
           
        return ans

def test_max_level_sum():
    solution = Solution()

    # Test Case 1
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(-8)
    print(solution.maxLevelSum(root)) # Expected Output: 2

    # Test Case 2
    root = TreeNode(989)
    root.right = TreeNode(10250)
    root.right.left = TreeNode(98693)
    root.right.right = TreeNode(-89388)
    root.right.right.right = TreeNode(-32127)
    print(solution.maxLevelSum(root)) # Expected Output: 2

    # Test Case 3
    root = TreeNode(-100)
    root.left = TreeNode(-200)
    root.right = TreeNode(-300)
    root.left.left = TreeNode(-20)
    root.left.right = TreeNode(-5)
    root.right.right = TreeNode(-10)
    print(solution.maxLevelSum(root)) # Expected Output: 3

    # Test Case 4
    root = TreeNode(1)
    print(solution.maxLevelSum(root)) # Expected Output: 1

    # Test Case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(solution.maxLevelSum(root)) # Expected Output: 3

test_max_level_sum()