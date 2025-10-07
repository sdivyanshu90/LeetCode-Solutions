from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

def test_minimum_total():
    solution = Solution()

    # Test case 1: Example triangle
    triangle1 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(solution.minimumTotal(triangle1))  # Expected output: 11

    # Test case 2: Single row triangle
    triangle2 = [
        [1]
    ]
    print(solution.minimumTotal(triangle2))  # Expected output: 1

    # Test case 3: Two rows triangle
    triangle3 = [
        [1],
        [2, 3]
    ]
    print(solution.minimumTotal(triangle3))  # Expected output: 3

    # Test case 4: Larger triangle
    triangle4 = [
        [5],
        [9, 6],
        [4, 6, 8],
        [0, 7, 1, 5]
    ]
    print(solution.minimumTotal(triangle4))  # Expected output: 18

    # Test case 5: Triangle with negative numbers
    triangle5 = [
        [-1],
        [2, 3],
        [1, -1, -3]
    ]
    print(solution.minimumTotal(triangle5))  # Expected output: -1

test_minimum_total()