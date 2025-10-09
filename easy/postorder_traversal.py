from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res

def test_postorder_traversal():
    sol = Solution()
    
    # Test case 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.postorderTraversal(root)) # Expected output: [3, 2, 1]
    
    # Test case 2
    root = None
    print(sol.postorderTraversal(root)) # Expected output: []
    
    # Test case 3
    root = TreeNode(1)
    print(sol.postorderTraversal(root)) # Expected output: [1]
    
    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.postorderTraversal(root)) # Expected output: [2, 3, 1]
    
    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print(sol.postorderTraversal(root)) # Expected output: [3, 2, 1]

test_postorder_traversal()