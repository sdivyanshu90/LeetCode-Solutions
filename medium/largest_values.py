from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        while queue:
            current_length = len(queue)
            curr_max = float("-inf")
            
            for _ in range(current_length):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(curr_max)
        return ans

def test_largest_values():
    solution = Solution()

    # Test Case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(9)
    print(solution.largestValues(root1))  # Expected: [1, 3, 9]

    # Test Case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(solution.largestValues(root2))  # Expected: [1, 3]

    # Test Case 3
    root3 = None
    print(solution.largestValues(root3))  # Expected: []

    # Test Case 4
    root4 = TreeNode(-10)
    root4.left = TreeNode(-20)
    root4.right = TreeNode(-30)
    root4.left.left = TreeNode(-5)
    root4.left.right = TreeNode(-15)
    print(solution.largestValues(root4))  # Expected: [-10, -20, -5]

    # Test Case 5
    root5 = TreeNode(0)
    print(solution.largestValues(root5))  # Expected: [0]

test_largest_values()