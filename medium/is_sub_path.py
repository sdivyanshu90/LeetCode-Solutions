from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(
        self, head: Optional[ListNode], root: Optional[TreeNode]
    ) -> bool:
        if not root:
            return False
        return (
            self._dfs(root, head)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )

    def _dfs(self, node: Optional[TreeNode], head: Optional[ListNode]) -> bool:
        if not head:
            return True  # All nodes in the list matched
        if not node:
            return False  # Reached end of tree without matching all nodes
        if node.val != head.val:
            return False  # Value mismatch
        # Check both left and right children
        return self._dfs(node.left, head.next) or self._dfs(
            node.right, head.next
        )

def test_isSubPath():
    solution = Solution()

    # Test case 1
    head1 = ListNode(4, ListNode(2, ListNode(8)))
    root1 = TreeNode(
        1,
        TreeNode(4, TreeNode(2), TreeNode(1)),
        TreeNode(4, None, TreeNode(2, None, TreeNode(6))),
    )
    print(solution.isSubPath(head1, root1)) # Expected output: False

    # Test case 2
    head2 = ListNode(1, ListNode(4, ListNode(2)))
    root2 = TreeNode(
        1,
        TreeNode(4, TreeNode(2), TreeNode(1)),
        TreeNode(4, None, TreeNode(2, None, TreeNode(6))),
    )
    print(solution.isSubPath(head2, root2)) # Expected output: True

    # Test case 3
    head3 = ListNode(1, ListNode(4, ListNode(2)))
    root3 = TreeNode(
        1,
        TreeNode(4, TreeNode(2), TreeNode(1)),
        TreeNode(4, None, TreeNode(2, None, TreeNode(6))),
    )
    print(solution.isSubPath(head3, root3)) # Expected output: True

    # Test case 4
    head4 = ListNode(1)
    root4 = None
    print(solution.isSubPath(head4, root4)) # Expected output: False

    # Test case 5
    head5 = ListNode(1)
    root5 = TreeNode(1)
    print(solution.isSubPath(head5, root5)) # Expected output: True

test_isSubPath()