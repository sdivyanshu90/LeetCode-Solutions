from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        res = 0
        for value, count in freq.items():
            if count == 1:
                res += value
        return res

def test_sum_of_unique():
    solution = Solution()

    # Test Case 1
    nums1 = [1,2,3,2]
    print(solution.sumOfUnique(nums1)) # Expected Output: 4

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(solution.sumOfUnique(nums2)) # Expected Output: 15

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(solution.sumOfUnique(nums3)) # Expected Output: 0

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(solution.sumOfUnique(nums4)) # Expected Output: 0

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    print(solution.sumOfUnique(nums5)) # Expected Output: 150

test_sum_of_unique()