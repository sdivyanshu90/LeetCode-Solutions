from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [num for num in nums if num % 2 == 0] + [num for num in nums if num % 2 != 0]

def test_sort_array_by_parity():
    solution = Solution()

    # Test Case 1
    print(solution.sortArrayByParity([3, 1, 2, 4])) # Expected: [2, 4, 3, 1]

    # Test Case 2
    print(solution.sortArrayByParity([0])) # Expected: [0]

    # Test Case 3
    print(solution.sortArrayByParity([1, 3, 5])) # Expected: [1, 3, 5]

    # Test Case 4
    print(solution.sortArrayByParity([2, 4, 6])) # Expected: [2, 4, 6]

    # Test Case 5
    print(solution.sortArrayByParity([1, 2, 3, 4, 5, 6])) # Expected: [2, 4, 6, 1, 3, 5]

test_sort_array_by_parity()