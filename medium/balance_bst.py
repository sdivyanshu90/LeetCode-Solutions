# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                inorder(node.left)
                sorted_array.append(node.val)
                inorder(node.right)
        def build(l, r):
            if l <= r:
                mid = (l + r) // 2
                return TreeNode(sorted_array[mid], build(l, mid - 1), build(mid + 1, r))
        sorted_array = []
        inorder(root)
        return build(0, len(sorted_array) - 1)

def test_balance_bst():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    balanced_root1 = solution.balanceBST(root1)
    print(balanced_root1.val)  # Expected output: 2

    # Test case 2
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    balanced_root2 = solution.balanceBST(root2)
    print(balanced_root2.val)  # Expected output: 3

    # Test case 3
    root3 = TreeNode(1)
    balanced_root3 = solution.balanceBST(root3)
    print(balanced_root3.val)  # Expected output: 1

    # Test case 4
    root4 = TreeNode(1, TreeNode(0), TreeNode(2))
    balanced_root4 = solution.balanceBST(root4)
    print(balanced_root4.val)  # Expected output: 1

    # Test case 5
    root5 = TreeNode(10, TreeNode(5), TreeNode(15))
    balanced_root5 = solution.balanceBST(root5)
    print(balanced_root5.val)  # Expected output: 10

test_balance_bst()