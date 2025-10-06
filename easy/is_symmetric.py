from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        if root is None:
            return True

        return isMirror(root.left, root.right)

def test_is_symmetric():
    solution = Solution()

    # Test case 1: Symmetric tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    print(solution.isSymmetric(root1))  # Expected output: True

    # Test case 2: Non-symmetric tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    print(solution.isSymmetric(root2))  # Expected output: False

    # Test case 3: Empty tree
    print(solution.isSymmetric(None))  # Expected output: True

    # Test case 4: Single node tree
    root4 = TreeNode(1)
    print(solution.isSymmetric(root4))  # Expected output: True

    # Test case 5: Larger symmetric tree
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(2)
    root5.left.left = TreeNode(3)
    root5.left.right = TreeNode(4)
    root5.right.left = TreeNode(4)
    root5.right.right = TreeNode(3)
    root5.left.left.left = TreeNode(5)
    root5.right.right.right = TreeNode(5)
    print(solution.isSymmetric(root5))  # Expected output: True

test_is_symmetric()