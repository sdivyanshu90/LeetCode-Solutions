from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.seen = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.seen

    def dfs(self, current_node, current_value):
        if current_node is None:
            return
        # visit current node by adding its value to seen
        self.seen.add(current_value)
        self.dfs(current_node.left, current_value * 2 + 1)
        self.dfs(current_node.right, current_value * 2 + 2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

def test_find_elements():
    # Test case 1
    root = TreeNode(-1, TreeNode(-1), TreeNode(-1))
    obj = FindElements(root)
    print(obj.find(1))  # Expected output: True
    print(obj.find(2))  # Expected output: True
    print(obj.find(3))  # Expected output: False
    print(obj.find(4))  # Expected output: False

    # Test case 2
    root = TreeNode(-1, TreeNode(-1, TreeNode(-1)), None)
    obj = FindElements(root)
    print(obj.find(1))  # Expected output: True
    print(obj.find(2))  # Expected output: True
    print(obj.find(3))  # Expected output: False
    print(obj.find(4))  # Expected output: False

    # Test case 3
    root = TreeNode(-1)
    obj = FindElements(root)
    print(obj.find(0))  # Expected output: True
    print(obj.find(1))  # Expected output: False
    print(obj.find(2))  # Expected output: False

    # Test case 4
    root = TreeNode(-1, None, TreeNode(-1))
    obj = FindElements(root)
    print(obj.find(1))  # Expected output: False
    print(obj.find(2))  # Expected output: True
    print(obj.find(3))  # Expected output: False
    print(obj.find(4))  # Expected output: False

    # Test case 5
    root = TreeNode(-1, TreeNode(-1, None, TreeNode(-1)), TreeNode(-1))
    obj = FindElements(root)
    print(obj.find(1))  # Expected output: True
    print(obj.find(2))  # Expected output: True
    print(obj.find(3))  # Expected output: False
    print(obj.find(4))  # Expected output: True
    print(obj.find(5))  # Expected output: False
    print(obj.find(6))  # Expected output: False

test_find_elements()