from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        height = [0] * (m + 1)
        ans = 0
        for r in matrix:
            for i in range(m):
                height[i] = height[i] + 1 if r[i] == '1' else 0
            stack = [-1]
            for i in range(m + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
        return ans

def test_maximal_rectangle():
    solution = Solution()

    # Test case 1
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalRectangle(matrix))  # Output: 6

    # Test case 2
    matrix = []
    print(solution.maximalRectangle(matrix))  # Output: 0

    # Test case 3
    matrix = [["0"]]
    print(solution.maximalRectangle(matrix))  # Output: 0

    # Test case 4
    matrix = [["1"]]
    print(solution.maximalRectangle(matrix))  # Output: 1

    # Test case 5
    matrix = [["0", "0"]]
    print(solution.maximalRectangle(matrix))  # Output: 0

    # Test case 6
    matrix = [["1", "1"]]
    print(solution.maximalRectangle(matrix))  # Output: 2

    # Test case 7
    matrix = [["1", "0"], ["1", "1"]]
    print(solution.maximalRectangle(matrix))  # Output: 3

    # Test case 8
    matrix = [["0", "1"], ["1", "1"]]
    print(solution.maximalRectangle(matrix))  # Output: 3

    # Test case 9
    matrix = [["0", "0"], ["0", "0"]]
    print(solution.maximalRectangle(matrix))  # Output: 0

    # Test case 10
    matrix = [["1", "1"], ["1", "1"]]
    print(solution.maximalRectangle(matrix))  # Output: 4

test_maximal_rectangle()