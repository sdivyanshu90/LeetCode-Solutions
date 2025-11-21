from typing import List
from collections import defaultdict

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []

        for i in range(len(nums)):
            for num in nums[i]:
                merged.append((num, i))

        merged.sort()
        freq = defaultdict(int)
        left, count = 0, 0
        range_start, range_end = 0, float("inf")

        for right in range(len(merged)):
            freq[merged[right][1]] += 1
            if freq[merged[right][1]] == 1:
                count += 1

            while count == len(nums):
                cur_range = merged[right][0] - merged[left][0]
                if cur_range < range_end - range_start:
                    range_start = merged[left][0]
                    range_end = merged[right][0]

                freq[merged[left][1]] -= 1
                if freq[merged[left][1]] == 0:
                    count -= 1
                left += 1

        return [range_start, range_end]

def test_smallest_range():
    s = Solution()

    # Test case 1
    nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
    print(s.smallestRange(nums))  # Expected output: [20,24]

    # Test case 2
    nums = [[1,2,3],[1,2,3],[1,2,3]]
    print(s.smallestRange(nums))  # Expected output: [1,1]

    # Test case 3
    nums = [[10,10],[11,11]]
    print(s.smallestRange(nums))  # Expected output: [10,11]

    # Test case 4
    nums = [[1],[2],[3],[4],[5],[6],[7]]
    print(s.smallestRange(nums))  # Expected output: [1,7]

    # Test case 5
    nums = [[-5,-4,-3,-2,-1],[0],[1,2,3,4,5]]
    print(s.smallestRange(nums))  # Expected output: [-1,0]

test_smallest_range()