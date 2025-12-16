from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums

# Approach: without using any built-in sort functions - TLE
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def quicksort(arr):
#             if len(arr) <= 1:
#                 return arr
#             pivot = arr[len(arr) // 2]
#             left = [x for x in arr if x < pivot]
#             middle = [x for x in arr if x == pivot]
#             right = [x for x in arr if x > pivot]
#             return quicksort(left) + middle + quicksort(right)
#         return quicksort(nums)
#      return nums

def test_sort_array():
    solution = Solution()

    # Test Case 1
    print(solution.sortArray([5, 2, 3, 1])) # Expected: [1, 2, 3, 5]

    # Test Case 2
    print(solution.sortArray([5, 1, 1, 2, 0, 0])) # Expected: [0, 0, 1, 1, 2, 5]

    # Test Case 3
    print(solution.sortArray([3, 3, 2, 1, 4])) # Expected: [1, 2, 3, 3, 4]

    # Test Case 4
    print(solution.sortArray([10, -1, 2, -10, 5])) # Expected: [-10, -1, 2, 5, 10]

    # Test Case 5
    print(solution.sortArray([0])) # Expected: [0]

test_sort_array()