# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(root, result):
            if not root:
                return
            inorder_traversal(root.left, result)
            result.append(root.val)
            inorder_traversal(root.right, result)
        
        result1, result2 = [], []
        inorder_traversal(root1, result1)
        inorder_traversal(root2, result2)
        
        combined = result1 + result2
        combined.sort()
        
        return combined

def test_get_all_elements():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(2, TreeNode(1), TreeNode(4))
    root2 = TreeNode(1, None, TreeNode(3))
    expected = [1, 1, 2, 3, 4]
    print(solution.getAllElements(root1, root2))  # Expected Output: [1, 1, 2, 3, 4]

    # Test case 2
    root1 = TreeNode(0)
    root2 = TreeNode(-10, None, TreeNode(10))
    expected = [-10, 0, 10]
    print(solution.getAllElements(root1, root2))  # Expected Output: [-10, 0, 10]

    # Test case 3
    root1 = None
    root2 = TreeNode(5)
    expected = [5]
    print(solution.getAllElements(root1, root2))  # Expected Output: [5]

    # Test case 4
    root1 = TreeNode(3)
    root2 = None
    expected = [3]
    print(solution.getAllElements(root1, root2))  # Expected Output: [3]

    # Test case 5
    root1 = TreeNode(1, None, TreeNode(8))
    root2 = TreeNode(8, TreeNode(1), None)
    expected = [1, 1, 8, 8]
    print(solution.getAllElements(root1, root2))  # Expected Output: [1, 1, 8, 8]

test_get_all_elements()