from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        def dfs(node):
            if not node:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

def test_preorder_traversal():
    sol = Solution()
    
    # Test case 1
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(sol.preorderTraversal(root)) # Expected output: [1, 2, 3]
    
    # Test case 2
    root = None
    print(sol.preorderTraversal(root)) # Expected output: []
    
    # Test case 3
    root = TreeNode(1)
    print(sol.preorderTraversal(root)) # Expected output: [1]
    
    # Test case 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(sol.preorderTraversal(root)) # Expected output: [1, 2, 3]
    
    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    print(sol.preorderTraversal(root)) # Expected output: [1, 2, 3]

test_preorder_traversal()