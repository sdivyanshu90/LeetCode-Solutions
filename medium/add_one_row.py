from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left = root)

        def recurse(rt = root, d = 1):
            if rt is None: 
                return None 

            if d == depth - 1:
                left_subtree = rt.left 
                right_subtree = rt.right 
                rt.left = TreeNode(val, left = left_subtree)
                rt.right = TreeNode(val, right = right_subtree)

            if d < depth - 1:
                recurse(rt.left, d + 1)
                recurse(rt.right, d + 1)

        recurse()
        return root

def test_add_one_row():
    s = Solution()

    # Test case 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)
    val = 1
    depth = 2
    new_root = s.addOneRow(root, val, depth)
    print(new_root.val)  # Expected output: 4
    print(new_root.left.val)  # Expected output: 1
    print(new_root.right.val)  # Expected output: 1

    # Test case 2
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)
    val = 1
    depth = 3
    new_root = s.addOneRow(root, val, depth)
    print(new_root.left.left.val)  # Expected output: 1
    print(new_root.left.right.val)  # Expected output: 1
    print(new_root.right.left.val)  # Expected output: 1
    print(new_root.right.right.val)  # Expected output: 1

    # Test case 3
    root = None
    val = 1
    depth = 1
    new_root = s.addOneRow(root, val, depth)
    print(new_root.val)  # Expected output: 1

    # Test case 4
    root = TreeNode(1)
    val = 2
    depth = 1
    new_root = s.addOneRow(root, val, depth)
    print(new_root.val)  # Expected output: 2
    print(new_root.left.val)  # Expected output: 1

    # Test case 5
    root = TreeNode(1)
    val = 3
    depth = 2
    new_root = s.addOneRow(root, val, depth)
    print(new_root.left.val)  # Expected output: 3
    print(new_root.right.val)  # Expected output: 3

test_add_one_row()