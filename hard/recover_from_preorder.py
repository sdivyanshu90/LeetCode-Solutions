from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal):
        stack = []
        index = 0
        root = None

        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == "-":
                depth += 1
                index += 1
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            node = TreeNode(value)
            if depth == 0:
                root = node
            else:
                while len(stack) > depth:
                    stack.pop()

                if stack[-1][0].left == None:
                    stack[-1][0].left = node
                else:
                    stack[-1][0].right = node
            stack.append((node, depth))

        return root

def test_recover_from_preorder():
    solution = Solution()

    # Test case 1
    traversal1 = "1-2--3--4-5--6--7"
    root1 = solution.recoverFromPreorder(traversal1)
    print(root1.val)  # Expected output: 1

    # Test case 2
    traversal2 = "1-2--3---4-5--6---7"
    root2 = solution.recoverFromPreorder(traversal2)
    print(root2.val)  # Expected output: 1

    # Test case 3
    traversal3 = "1-401--349---90--88"
    root3 = solution.recoverFromPreorder(traversal3)
    print(root3.val)  # Expected output: 1

    # Test case 4
    traversal4 = "1"
    root4 = solution.recoverFromPreorder(traversal4)
    print(root4.val)  # Expected output: 1

    # Test case 5
    traversal5 = "10-20--30--40-50--60--70"
    root5 = solution.recoverFromPreorder(traversal5)
    print(root5.val)  # Expected output: 10

test_recover_from_preorder()