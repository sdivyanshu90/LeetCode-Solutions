# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstToGst(self, root):
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = get_successor(node)
                if succ.left is None:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root

def test_bst_to_gst():
    solution = Solution()

    # Test case 1
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)

    new_root = solution.bstToGst(root)
    print(new_root.val)  # 30
    print(new_root.left.val)  # 36
    print(new_root.right.val)  # 21
    print(new_root.left.left.val)  # 36
    print(new_root.left.right.val)  # 35
    print(new_root.right.left.val)  # 15
    print(new_root.right.right.val)  # 8
    print(new_root.right.right.right.val)  # 8

test_bst_to_gst()