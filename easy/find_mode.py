from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, counter):
            if not node:
                return
            
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
            
        counter = defaultdict(int)
        dfs(root, counter)
        max_freq = max(counter.values())
        
        ans = []
        for key in counter:
            if counter[key] == max_freq:
                ans.append(key)
        
        return ans

def test_find_mode():
    solution = Solution()

    # Test case 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    print(solution.findMode(root))  # Expected output: [2]

    # Test case 2
    root = TreeNode(1)
    print(solution.findMode(root))  # Expected output: [1]

    # Test case 3
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(2)
    print(solution.findMode(root))  # Expected output: [1, 2]

    # Test case 4
    root = TreeNode(9)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(3)
    print(solution.findMode(root))  # Expected output: [9, 7, 5, 6, 8, 3, 4]

    # Test case 5
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right.right = TreeNode(4)
    print(solution.findMode(root))  # Expected output: [2, 4]

test_find_mode()