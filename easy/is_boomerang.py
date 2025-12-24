from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        (x1, y1), (x2, y2), (x3, y3) = points
        
        if (x1, y1) == (x2, y2) or (x2, y2) == (x3, y3) or (x1, y1) == (x3, y3):
            return False
        
        return (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1)

def test_is_boomerang():
    solution = Solution()

    # Test case 1
    points = [[1, 1], [2, 3], [3, 2]]
    print(solution.isBoomerang(points))  # Expected output: True

    # Test case 2
    points = [[1, 1], [2, 2], [3, 3]]
    print(solution.isBoomerang(points))  # Expected output: False

    # Test case 3
    points = [[0, 0], [1, 1], [1, 0]]
    print(solution.isBoomerang(points))  # Expected output: True

    # Test case 4
    points = [[0, 0], [0, 0], [1, 1]]
    print(solution.isBoomerang(points))  # Expected output: False

    # Test case 5
    points = [[-1, -1], [0, 0], [1, 1]]
    print(solution.isBoomerang(points))  # Expected output: False

test_is_boomerang()