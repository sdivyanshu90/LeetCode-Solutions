from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        ans = 0
        curr = 0
        
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)

        return ans

def test_max_frequency():
    solution = Solution()

    # Test Case 1
    nums1 = [1,2,4]
    k1 = 5
    print(solution.maxFrequency(nums1, k1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1,4,8,13]
    k2 = 5
    print(solution.maxFrequency(nums2, k2))  # Expected Output: 2

    # Test Case 3
    nums3 = [3,9,6]
    k3 = 2
    print(solution.maxFrequency(nums3, k3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1,2,4]
    k4 = 1
    print(solution.maxFrequency(nums4, k4))  # Expected Output: 2

    # Test Case 5
    nums5 = [1,2,4]
    k5 = 0
    print(solution.maxFrequency(nums5, k5))  # Expected Output: 1

test_max_frequency()