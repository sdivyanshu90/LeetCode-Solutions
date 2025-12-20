from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        smallest_string = ""
        node_queue = deque()
        node_queue.append([root, chr(root.val + ord('a'))])
        
        while node_queue:
            node, current_string = node_queue.popleft()
            
            if not node.left and not node.right:
                smallest_string = min(smallest_string, current_string) if smallest_string else current_string
            if node.left:
                node_queue.append([node.left, chr(node.left.val + ord('a')) + current_string])
            if node.right:
                node_queue.append([node.right, chr(node.right.val + ord('a')) + current_string])

        return smallest_string

def test_smallest_from_leaf():
    solution = Solution()
    
    # Test case 1
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    print(solution.smallestFromLeaf(root))  # Expected output: "ba"

    # Test case 2
    root = TreeNode(25)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    print(solution.smallestFromLeaf(root))  # Expected output: "adz"

    # Test case 3
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(solution.smallestFromLeaf(root))  # Expected output: "abc"

    # Test case 4
    root = TreeNode(0)
    print(solution.smallestFromLeaf(root))  # Expected output: "a"

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(25)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    print(solution.smallestFromLeaf(root))  # Expected output: "cab"

test_smallest_from_leaf()