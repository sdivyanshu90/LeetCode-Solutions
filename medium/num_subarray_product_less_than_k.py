import bisect
import math
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return 0
        logK = math.log(k)

        logs_prefix_sum = [0]
        for num in nums:
            logs_prefix_sum.append(logs_prefix_sum[-1] + math.log(num))

        total_count = 0
        for i, log_num in enumerate(logs_prefix_sum):
            j = bisect.bisect(logs_prefix_sum, log_num + logK - 1e-9, i+1)
            total_count += j - i - 1
        return total_count

def test_num_subarray_product_less_than_k():
    solution = Solution()

    # Test Case 1
    nums = [10, 5, 2, 6]
    k = 100
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 8

    # Test Case 2
    nums = [1, 2, 3]
    k = 0
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 0

    # Test Case 3: Single element less than k
    nums = [5]
    k = 10
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 1

    # Test Case 4: Single element equal to k
    nums = [10]
    k = 10
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 0

    # Test Case 5: All elements greater than or equal to k
    nums = [10, 20, 30]
    k = 5
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 0

    # Test Case 6: Large array with small k
    nums = [1] * 1000
    k = 2
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 500500

    # Test Case 7: Large array with large k
    nums = [100] * 1000
    k = 10**10
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 499500

    # Test Case 8: Mixed elements
    nums = [3, 5, 2, 7, 1]
    k = 20
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 10

    # Test Case 9: Increasing sequence
    nums = [1, 2, 3, 4, 5]
    k = 15
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 9

    # Test Case 10: Decreasing sequence
    nums = [5, 4, 3, 2, 1]
    k = 10
    print(solution.numSubarrayProductLessThanK(nums, k))  # Expected: 8

test_num_subarray_product_less_than_k()