from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def bfs(node):
            q = deque()
            q.append(node)
            levels = []
            while q:
                n = len(q)
                level = []
                for i in range(n):
                    popped = q.popleft()
                    if popped:
                        level.append(popped.val)
                        q.append(popped.left)
                        q.append(popped.right)
                if level:
                    levels.append(level)
            return levels[-1][0]      
        return bfs(root)

def test_find_bottom_left_value():
    solution = Solution()

    # Test Case 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    print(solution.findBottomLeftValue(root1))  # Expected: 1

    # Test Case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(6)
    root2.right.left.left = TreeNode(7)
    print(solution.findBottomLeftValue(root2))  # Expected: 7

    # Test Case 3
    root3 = TreeNode(0)
    print(solution.findBottomLeftValue(root3))  # Expected: 0

    # Test Case 4
    root4 = TreeNode(-1)
    root4.left = TreeNode(-2)
    root4.right = TreeNode(-3)
    root4.left.left = TreeNode(-4)
    print(solution.findBottomLeftValue(root4))  # Expected: -4

    # Test Case 5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.left.right = TreeNode(4)
    root5.left.right.left = TreeNode(5)
    print(solution.findBottomLeftValue(root5))  # Expected: 5

test_find_bottom_left_value()