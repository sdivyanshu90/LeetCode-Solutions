from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        res = []
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

def test_inorder_traversal():
    solution = Solution()

    # Helper function to create a binary tree from a list
    def create_tree(lst):
        if not lst:
            return None
        nodes = [TreeNode(x) if x is not None else None for x in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Test Case 1
    root = create_tree([1,None,2,3])
    print(solution.inorderTraversal(root)) # Output: [1,3,2]

    # Test Case 2
    root = create_tree([])
    print(solution.inorderTraversal(root)) # Output: []

    # Test Case 3
    root = create_tree([1])
    print(solution.inorderTraversal(root)) # Output: [1]

    # Test Case 4
    root = create_tree([1,2])
    print(solution.inorderTraversal(root)) # Output: [2,1]

    # Test Case 5
    root = create_tree([1,None,2])
    print(solution.inorderTraversal(root)) # Output: [1,2]

test_inorder_traversal()