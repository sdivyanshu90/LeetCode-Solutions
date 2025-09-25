from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            res = max(res, min(height[left], height[right]) * width)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res

        # Time complexity: O(n)
        # Space complexity: O(1)

def test_max_area():
    solution = Solution()

    # Test case 1
    height = [1,8,6,2,5,4,8,3,7]
    print(solution.maxArea(height))  # Expected output: 49

    # Test case 2
    height = [1,1]
    print(solution.maxArea(height))  # Expected output: 1

    # Test case 3
    height = [4,3,2,1,4]
    print(solution.maxArea(height))  # Expected output: 16

    # Test case 4
    height = [1,2,1]
    print(solution.maxArea(height))  # Expected output: 2

    # Test case 5
    height = [1,3,2,5,25,24,5]
    print(solution.maxArea(height))  # Expected output: 24

    # Test case 6
    height = [2,3,4,5,18,17,6]
    print(solution.maxArea(height))  # Expected output: 17

    # Test case 7
    height = [1,2,4,3]
    print(solution.maxArea(height))  # Expected output: 4

    # Test case 8
    height = [1,3,2]
    print(solution.maxArea(height))  # Expected output: 2

    # Test case 9
    height = [1,2,1,3,1,4,1,5]
    print(solution.maxArea(height))  # Expected output: 6

    # Test case 10
    height = [5,4,3,2,1,2,3,4,5]
    print(solution.maxArea(height))  # Expected output: 40

test_max_area()