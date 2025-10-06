from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

def test_has_path_sum():
    solution = Solution()

    # Test case 1: Tree with a valid path sum
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.right = TreeNode(1)
    print(solution.hasPathSum(root1, 22))  # Expected output: True

    # Test case 2: Tree without a valid path sum
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    print(solution.hasPathSum(root2, 1))  # Expected output: False

    # Test case 3: Empty tree
    print(solution.hasPathSum(None, 0))  # Expected output: False

    # Test case 4: Single node tree with matching target sum
    root4 = TreeNode(7)
    print(solution.hasPathSum(root4, 7))  # Expected output: True

    # Test case 5: Single node tree without matching target sum
    root5 = TreeNode(7)
    print(solution.hasPathSum(root5, 10))  # Expected output: False

test_has_path_sum()