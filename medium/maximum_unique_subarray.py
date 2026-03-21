from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        left = curr_sum = max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum,curr_sum)
        return max_sum

def test_maximum_unique_subarray():
    s = Solution()

    # Test Case 1
    nums1 = [4,2,4,5,6]
    print(s.maximumUniqueSubarray(nums1)) # Expected Output: 17

    # Test Case 2
    nums2 = [5,2,1,2,5,2,1,2,5]
    print(s.maximumUniqueSubarray(nums2)) # Expected Output: 8

    # Test Case 3
    nums3 = [10000]
    print(s.maximumUniqueSubarray(nums3)) # Expected Output: 10000

    # Test Case 4
    nums4 = [1,2,3,4,5]
    print(s.maximumUniqueSubarray(nums4)) # Expected Output: 15

    # Test Case 5
    nums5 = [1,1,1,1]
    print(s.maximumUniqueSubarray(nums5)) # Expected Output: 1

test_maximum_unique_subarray()