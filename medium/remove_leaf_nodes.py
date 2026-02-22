from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_list(root: Optional[TreeNode]):
    if root is None:
        return []

    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)

    while result and result[-1] is None:
        result.pop()
    return result
        
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
    output = solution.removeLeafNodes(root, target)
    print(tree_to_list(output))  # Expected Output: [1, None, 3]

    # Test case 2
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target = 3
    expected = TreeNode(1, TreeNode(2), None)
    output = solution.removeLeafNodes(root, target)
    print(tree_to_list(output))  # Expected Output: [1, 2]

    # Test case 3
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target = 1
    expected = None
    output = solution.removeLeafNodes(root, target)
    print(tree_to_list(output))  # Expected Output: [1, 2, 3]

    # Test case 4
    root = TreeNode(1, TreeNode(2), None)
    target = 2
    expected = TreeNode(1)
    output = solution.removeLeafNodes(root, target)
    print(tree_to_list(output))  # Expected Output: [1]

    # Test case 5
    root = TreeNode(1, None, TreeNode(2))
    target = 2
    expected = TreeNode(1)
    output = solution.removeLeafNodes(root, target)
    print(tree_to_list(output))  # Expected Output: [1]

test_removeLeafNodes()