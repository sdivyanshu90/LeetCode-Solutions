from typing import List

class Solution:
    def bucket_sort(self, arr, place_value):
        buckets = [[] for _ in range(10)]

        for val in arr:
            digit = abs(val) // place_value
            digit = digit % 10
            buckets[digit].append(val)

        index = 0
        for digit in range(10):
            for val in buckets[digit]:
                arr[index] = val
                index += 1

    def radix_sort(self, arr):
        max_element, max_digits = max(abs(val) for val in arr), 0
        while max_element > 0:
            max_digits += 1
            max_element //= 10

        place_value = 1
        for _ in range(max_digits):
            self.bucket_sort(arr, place_value)
            place_value *= 10

    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights[:]
        self.radix_sort(sorted_heights)

        count = 0
        for i in range(len(sorted_heights)):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count

def test_height_checker():
    solution = Solution()

    # Test case 1
    heights1 = [1, 1, 4, 2, 1, 3]
    print(solution.heightChecker(heights1))  # Expected output: 3

    # Test case 2
    heights2 = [5, 1, 2, 3, 4]
    print(solution.heightChecker(heights2))  # Expected output: 5

    # Test case 3
    heights3 = [1, 2, 3, 4, 5]
    print(solution.heightChecker(heights3))  # Expected output: 0

    # Test case 4
    heights4 = [3, 2, 1]
    print(solution.heightChecker(heights4))  # Expected output: 2

    # Test case 5
    heights5 = [2, 2, 2, 1, 1, 1]
    print(solution.heightChecker(heights5))  # Expected output: 4

test_height_checker()