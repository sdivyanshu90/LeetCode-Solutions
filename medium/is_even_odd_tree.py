# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        current = root
        queue.append(current)

        even = True

        while queue:
            size = len(queue)
            prev = maxsize
            if even:
                prev = -maxsize

            while size > 0:
                current = queue.popleft()
                if (even and (current.val % 2 == 0 or current.val <= prev)) or \
                        (not even and (current.val % 2 == 1 or current.val >= prev)):
                    return False

                prev = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1

            even = not even

        return True

def test_is_even_odd_tree():
    solution = Solution()

    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(10)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(9)
    print(solution.isEvenOddTree(root))  # Expected output: True

    # Test case 2
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    print(solution.isEvenOddTree(root))  # Expected output: False

    # Test case 3
    root = TreeNode(1)
    print(solution.isEvenOddTree(root))  # Expected output: True

    # Test case 4
    root = TreeNode(11)
    root.left = TreeNode(8)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(9)
    print(solution.isEvenOddTree(root))  # Expected output: False

    # Test case 5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(solution.isEvenOddTree(root))  # Expected output: False

test_is_even_odd_tree()