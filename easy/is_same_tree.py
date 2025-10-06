from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        
        if (p is None and q) or (p and q is None):
            return False
        
        if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        
        return False

def test_is_same_tree():
    solution = Solution()

    # Test case 1: Identical trees
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    print(solution.isSameTree(root1, root2))  # Expected output: True

    # Test case 2: Different structure
    root3 = TreeNode(1)
    root3.left = TreeNode(2)

    root4 = TreeNode(1)
    root4.right = TreeNode(2)

    print(solution.isSameTree(root3, root4))  # Expected output: False

    # Test case 3: Different values
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(1)

    root6 = TreeNode(1)
    root6.left = TreeNode(1)
    root6.right = TreeNode(2)

    print(solution.isSameTree(root5, root6))  # Expected output: False

    # Test case 4: Both trees are empty
    print(solution.isSameTree(None, None))  # Expected output: True

    # Test case 5: One tree is empty, the other is not
    root7 = TreeNode(1)
    print(solution.isSameTree(root7, None))  # Expected output: False
    print(solution.isSameTree(None, root7))  # Expected output: False

test_is_same_tree()