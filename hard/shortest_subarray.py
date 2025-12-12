from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        candidate_indices = deque()
        shortest_subarray_length = float("inf")

        for i in range(n + 1):
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]]
                >= target_sum
            ):
                shortest_subarray_length = min(
                    shortest_subarray_length, i - candidate_indices.popleft()
                )

            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()

            candidate_indices.append(i)

        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )

def test_shortestSubarray():
    solution = Solution()
    
    # Test Case 1
    print(solution.shortestSubarray([1,2], 4)) # Expected: -1

    # Test Case 2
    print(solution.shortestSubarray([2,-1,2], 3)) # Expected: 3

    # Test Case 3
    print(solution.shortestSubarray([1], 1)) # Expected: 1

    # Test Case 4
    print(solution.shortestSubarray([1,2,3,4,5], 11)) # Expected: 3

    # Test Case 5
    print(solution.shortestSubarray([84,-37,32,40,95], 167)) # Expected: 3

test_shortestSubarray()