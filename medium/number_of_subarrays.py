from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum: 1}

        for i in range(len(nums)):
            curr_sum += nums[i] % 2
            if curr_sum - k in prefix_sum:
                subarrays = subarrays + prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
        return subarrays

def test_number_of_subarrays():
    solution = Solution()

    # Test case 1
    nums = [1,1,2,1,1]
    k = 3
    print(solution.numberOfSubarrays(nums, k))  # Expected output: 2

    # Test case 2
    nums = [2,4,6]
    k = 1
    print(solution.numberOfSubarrays(nums, k))  # Expected output: 0

    # Test case 3
    nums = [2,2,2,1,2,2,1,2,2,2]
    k = 2
    print(solution.numberOfSubarrays(nums, k))  # Expected output: 16

    # Test case 4
    nums = [1,2,3,4,5]
    k = 2
    print(solution.numberOfSubarrays(nums, k))  # Expected output: 4

    # Test case 5
    nums = [1,1,1,1,1]
    k = 5
    print(solution.numberOfSubarrays(nums, k))  # Expected output: 1

test_number_of_subarrays()