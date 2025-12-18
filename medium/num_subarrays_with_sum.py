from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        freq = {}

        for num in nums:
            current_sum += num
            if current_sum == goal:
                total_count += 1
            if current_sum - goal in freq:
                total_count += freq[current_sum - goal]
            freq[current_sum] = freq.get(current_sum, 0) + 1
        return total_count

def test_num_subarrays_with_sum():
    solution = Solution()

    # Test case 1
    nums1 = [1,0,1,0,1]
    goal1 = 2
    print(solution.numSubarraysWithSum(nums1, goal1))  # Expected output: 4

    # Test case 2
    nums2 = [0,0,0,0,0]
    goal2 = 0
    print(solution.numSubarraysWithSum(nums2, goal2))  # Expected output: 15

    # Test case 3
    nums3 = [1,1,1,1,1]
    goal3 = 3
    print(solution.numSubarraysWithSum(nums3, goal3))  # Expected output: 3

    # Test case 4
    nums4 = [1,0,1,0,1]
    goal4 = 3
    print(solution.numSubarraysWithSum(nums4, goal4))  # Expected output: 1

    # Test case 5
    nums5 = [0,1,0,1,0]
    goal5 = 1
    print(solution.numSubarraysWithSum(nums5, goal5))  # Expected output: 6

test_num_subarrays_with_sum()