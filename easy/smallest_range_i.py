from typing import List

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2*k)

def test_smallest_range_i():
    solution = Solution()

    # Test Case 1
    print(solution.smallestRangeI([1], 0)) # Expected: 0

    # Test Case 2
    print(solution.smallestRangeI([0,10], 2)) # Expected: 6

    # Test Case 3
    print(solution.smallestRangeI([1,3,6], 3)) # Expected: 0

    # Test Case 4
    print(solution.smallestRangeI([5,8,10], 1)) # Expected: 3

    # Test Case 5
    print(solution.smallestRangeI([2,7,4,1], 3)) # Expected: 0

test_smallest_range_i()