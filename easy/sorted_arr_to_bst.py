from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct_bst(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = construct_bst(left, mid - 1)
            root.right = construct_bst(mid + 1, right)

            return root
        return construct_bst(0, len(nums) - 1)

def test_sorted_array_to_bst():
    solution = Solution()

    # Test case 1: Balanced BST
    nums1 = [-10, -3, 0, 5, 9]
    bst1 = solution.sortedArrayToBST(nums1)
    print(bst1.val)  # Expected output: 0 (root value)

    # Test case 2: Single element
    nums2 = [1]
    bst2 = solution.sortedArrayToBST(nums2)
    print(bst2.val)  # Expected output: 1 (root value)

    # Test case 3: Two elements
    nums3 = [1, 2]
    bst3 = solution.sortedArrayToBST(nums3)
    print(bst3.val)        # Expected output: 2

    # Test case 4: Empty array
    nums4 = []
    bst4 = solution.sortedArrayToBST(nums4)
    print(bst4)  # Expected output: None (empty tree)

    # Test case 5: Larger array
    nums5 = [i for i in range(1, 16)]  # [1, 2, ..., 15]
    bst5 = solution.sortedArrayToBST(nums5)
    print(bst5.val)  # Expected output: 8 (root value)

test_sorted_array_to_bst()