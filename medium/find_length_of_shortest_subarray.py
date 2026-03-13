from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        right = len(arr) - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ans = right
        left = 0
        while left < right and (left == 0 or arr[left - 1] <= arr[left]):
            while right < len(arr) and arr[left] > arr[right]:
                right += 1
            ans = min(ans, right - left - 1)
            left += 1
        return ans

def test_find_length_of_shortest_subarray():
    solution = Solution()

    # Test case 1
    arr = [1, 2, 3, 10, 4, 2, 3, 5]
    print(solution.findLengthOfShortestSubarray(arr))  # Expected output: 3

    # Test case 2
    arr = [5, 4, 3, 2, 1]
    print(solution.findLengthOfShortestSubarray(arr))  # Expected output: 4

    # Test case 3
    arr = [1, 2, 3]
    print(solution.findLengthOfShortestSubarray(arr))  # Expected output: 0

    # Test case 4
    arr = [1]
    print(solution.findLengthOfShortestSubarray(arr))  # Expected output: 0

    # Test case 5
    arr = [1, 2, 3, 4, 5]
    print(solution.findLengthOfShortestSubarray(arr))  # Expected output: 0

test_find_length_of_shortest_subarray()