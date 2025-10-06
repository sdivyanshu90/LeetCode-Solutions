from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res

def test_level_order():
    solution = Solution()

    # Test case 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(solution.levelOrder(root1))  # Expected output: [[3], [9, 20], [15, 7]]

    # Test case 2: Single node tree
    root2 = TreeNode(1)
    print(solution.levelOrder(root2))  # Expected output: [[1]]

    # Test case 3: Empty tree
    print(solution.levelOrder(None))  # Expected output: []

    # Test case 4: Left-skewed tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    print(solution.levelOrder(root4))  # Expected output: [[1], [2], [3]]

    # Test case 5: Right-skewed tree
    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)
    print(solution.levelOrder(root5))  # Expected output: [[1], [2], [3]]
    
test_level_order()