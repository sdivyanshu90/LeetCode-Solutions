# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))

def test_leaf_similar():
    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    solution = Solution()
    print(solution.leafSimilar(root1, root2)) # Expected output: True

    # Test case 2
    root3 = TreeNode(1)
    root3.left = TreeNode(2)

    root4 = TreeNode(2)
    root4.left = TreeNode(2)

    print(solution.leafSimilar(root3, root4)) # Expected output: True

    # Test case 3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)

    root6 = TreeNode(1)
    root6.left = TreeNode(3)
    root6.right = TreeNode(2)

    print(solution.leafSimilar(root5, root6)) # Expected output: False


    # Test case 4
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    root7.right = TreeNode(3)
    root7.left.left = TreeNode(4)
    root7.left.right = TreeNode(5)
    root7.right.left = TreeNode(6)
    root7.right.right = TreeNode(7)
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(3)
    root8.left.left = TreeNode(4)
    root8.left.right = TreeNode(5)
    root8.right.left = TreeNode(6)
    root8.right.right = TreeNode(8)
    print(solution.leafSimilar(root7, root8)) # Expected output: False

    # Test case 5
    root9 = TreeNode(1)
    root10 = TreeNode(1)
    print(solution.leafSimilar(root9, root10)) # Expected output: True

test_leaf_similar()