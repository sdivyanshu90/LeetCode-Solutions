from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False

        no_swap = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(
            root1.right, root2.right
        )

        swap = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(
            root1.right, root2.left
        )

        return no_swap or swap

def test_flip_equiv():
    solution = Solution()

    # Test case 1
    root1_1 = TreeNode(1)
    root1_1.left = TreeNode(2)
    root1_1.right = TreeNode(3)
    root1_1.left.left = TreeNode(4)
    root1_1.left.right = TreeNode(5)
    root1_1.right.left = TreeNode(6)
    root1_1.left.right.left = TreeNode(7)
    root1_1.left.right.right = TreeNode(8)

    root2_1 = TreeNode(1)
    root2_1.left = TreeNode(3)
    root2_1.right = TreeNode(2)
    root2_1.right.left = TreeNode(4)
    root2_1.right.right = TreeNode(5)
    root2_1.left.right = TreeNode(6)
    root2_1.right.right.left = TreeNode(8)
    root2_1.right.right.right = TreeNode(7)

    print(solution.flipEquiv(root1_1, root2_1))  # Expected output: True

    # Test case 2
    root1_2 = TreeNode(1)
    root1_2.left = TreeNode(2)

    root2_2 = TreeNode(1)
    root2_2.right = TreeNode(2)

    print(solution.flipEquiv(root1_2, root2_2))  # Expected output: True

    # Test case 3
    root1_3 = TreeNode(1)
    root1_3.left = TreeNode(2)
    root1_3.right = TreeNode(3)

    root2_3 = TreeNode(1)
    root2_3.left = TreeNode(2)
    root2_3.right = TreeNode(4)

    print(solution.flipEquiv(root1_3, root2_3))  # Expected output: False

    # Test case 4
    root1_4 = None
    root2_4 = None

    print(solution.flipEquiv(root1_4, root2_4))  # Expected output: True

    # Test case 5
    root1_5 = TreeNode(1)
    root2_5 = None

    print(solution.flipEquiv(root1_5, root2_5))  # Expected output: False

test_flip_equiv()