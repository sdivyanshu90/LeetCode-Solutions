# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)        
        root.right = self.removeLeafNodes(root.right, target)
        
        if root.left is None and root.right is None and root.val == target:
            return None
        return root

def test_removeLeafNodes():
    solution = Solution()

    # Test case 1
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target = 2
    expected = TreeNode(1, None, TreeNode(3))
    print(solution.removeLeafNodes(root, target))  # Expected Output: TreeNode(1, None, TreeNode(3))

    # Test case 2
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target = 3
    expected = TreeNode(1, TreeNode(2), None)
    print(solution.removeLeafNodes(root, target))  # Expected Output: TreeNode(1, TreeNode(2), None)

    # Test case 3
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target = 1
    expected = None
    print(solution.removeLeafNodes(root, target))  # Expected Output: None

    # Test case 4
    root = TreeNode(1, TreeNode(2), None)
    target = 2
    expected = TreeNode(1)
    print(solution.removeLeafNodes(root, target))  # Expected Output: TreeNode(1)

    # Test case 5
    root = TreeNode(1, None, TreeNode(2))
    target = 2
    expected = TreeNode(1)
    print(solution.removeLeafNodes(root, target))  # Expected Output: TreeNode(1)

test_removeLeafNodes()