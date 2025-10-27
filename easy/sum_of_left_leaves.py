from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total=0
        
        def dfs(node,left):
            if not node:
                return 
            
            dfs(node.left,True)
            dfs(node.right,False)
            
            if not node.left and not node.right and left:
                self.total+=node.val
                
        dfs(root,False)
        return self.total

def test_sum_of_left_leaves():
    s = Solution()

    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(s.sumOfLeftLeaves(root1))  # Expected output: 24

    # Test case 2
    root2 = TreeNode(1)
    print(s.sumOfLeftLeaves(root2))  # Expected output: 0

    # Test case 3
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    print(s.sumOfLeftLeaves(root3))  # Expected output: 2

    # Test case 4
    root4 = TreeNode(1)
    root4.right = TreeNode(3)
    print(s.sumOfLeftLeaves(root4))  # Expected output: 0

    # Test case 5
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(4)
    root5.left.right = TreeNode(5)
    print(s.sumOfLeftLeaves(root5))  # Expected output: 4

test_sum_of_left_leaves()