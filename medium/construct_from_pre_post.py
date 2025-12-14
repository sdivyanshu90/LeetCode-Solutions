from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        num_of_nodes = len(preorder)

        index_in_post_order = [0] * (num_of_nodes + 1)
        for index in range(num_of_nodes):
            index_in_post_order[postorder[index]] = index

        return self._construct_tree(
            0, num_of_nodes - 1, 0, preorder, index_in_post_order
        )

    def _construct_tree(
        self,
        pre_start: int,
        pre_end: int,
        post_start: int,
        preorder: List[int],
        index_in_post_order: List[int],
    ) -> Optional[TreeNode]:
        if pre_start > pre_end:
            return None

        if pre_start == pre_end:
            return TreeNode(preorder[pre_start])

        left_root = preorder[pre_start + 1]

        num_of_nodes_in_left = index_in_post_order[left_root] - post_start + 1

        root = TreeNode(preorder[pre_start])

        root.left = self._construct_tree(
            pre_start + 1,
            pre_start + num_of_nodes_in_left,
            post_start,
            preorder,
            index_in_post_order,
        )

        root.right = self._construct_tree(
            pre_start + num_of_nodes_in_left + 1,
            pre_end,
            post_start + num_of_nodes_in_left,
            preorder,
            index_in_post_order,
        )

        return root

def test_construct_from_pre_post():
    solution = Solution()

    # Test case 1
    preorder1 = [1, 2, 4, 5, 3, 6, 7]
    postorder1 = [4, 5, 2, 6, 7, 3, 1]
    root1 = solution.constructFromPrePost(preorder1, postorder1)
    print(root1.val)  # Expected output: 1

    # Test case 2
    preorder2 = [1, 2, 3]
    postorder2 = [3, 2, 1]
    root2 = solution.constructFromPrePost(preorder2, postorder2)
    print(root2.val)  # Expected output: 1

    # Test case 3
    preorder3 = [1]
    postorder3 = [1]
    root3 = solution.constructFromPrePost(preorder3, postorder3)
    print(root3.val)  # Expected output: 1

    # Test case 4
    preorder4 = [1, 2]
    postorder4 = [2, 1]
    root4 = solution.constructFromPrePost(preorder4, postorder4)
    print(root4.val)  # Expected output: 1

    # Test case 5
    preorder5 = [1, 2, 3, 4]
    postorder5 = [4, 3, 2, 1]
    root5 = solution.constructFromPrePost(preorder5, postorder5)
    print(root5.val)  # Expected output: 1

test_construct_from_pre_post()