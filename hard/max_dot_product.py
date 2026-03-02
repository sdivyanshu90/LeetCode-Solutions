from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        m = len(nums2) + 1
        prev_dp = [0] * m
        dp = [0] * m
        
        for i in range(len(nums1) - 1, -1, -1):
            dp = [0] * m
            for j in range(len(nums2) - 1, -1, -1):
                use = nums1[i] * nums2[j] + prev_dp[j + 1]
                dp[j] = max(use, prev_dp[j], dp[j + 1])
            
            prev_dp = dp
        
        return dp[0]

def test_max_dot_product():
    solution = Solution()

    # Test case 1
    nums1 = [2, 1, -2, 5]
    nums2 = [3, 0, -6]
    print(solution.maxDotProduct(nums1, nums2))  # Expected output: 18

    # Test case 2
    nums1 = [3, -2]
    nums2 = [2, -6, 7]
    print(solution.maxDotProduct(nums1, nums2))  # Expected output: 21

    # Test case 3
    nums1 = [-1, -1]
    nums2 = [1, 1]
    print(solution.maxDotProduct(nums1, nums2))  # Expected output: -1

    # Test case 4
    nums1 = [5, -4, -1]
    nums2 = [-3, -4, 1]
    print(solution.maxDotProduct(nums1, nums2))  # Expected output: 16

    # Test case 5
    nums1 = [1, -1]
    nums2 = [-1, 1]
    print(solution.maxDotProduct(nums1, nums2))  # Expected output: 1

test_max_dot_product()