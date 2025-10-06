from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            if not node:
                return 0

            left_height = check_balance_and_height(node.left)
            if left_height == -1:
                return -1

            right_height = check_balance_and_height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return check_balance_and_height(root) != -1

def test_is_balanced():
    solution = Solution()

    # Test case 1: Balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(solution.isBalanced(root1))  # Expected output: True

    # Test case 2: Unbalanced tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(solution.isBalanced(root2))  # Expected output: False

    # Test case 3: Single node tree
    root3 = TreeNode(1)
    print(solution.isBalanced(root3))  # Expected output: True

    # Test case 4: Empty tree
    print(solution.isBalanced(None))  # Expected output: True

    # Test case 5: Larger balanced tree
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    root5.left.left = TreeNode(4)
    root5.left.right = TreeNode(5)
    root5.right.left = TreeNode(6)
    root5.right.right = TreeNode(7)
    print(solution.isBalanced(root5))  # Expected output: True

test_is_balanced()