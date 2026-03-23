from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = []
        for i in range(len(rectangles)):
            res.append(min(rectangles[i]))

        return res.count(max(res))

def test_count_good_rectangles():
    solution = Solution()

    # Test case 1
    rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
    print(solution.countGoodRectangles(rectangles))  # Expected output: 3

    # Test case 2
    rectangles = [[2, 3], [3, 7], [4, 3], [3, 7]]
    print(solution.countGoodRectangles(rectangles))  # Expected output: 3

    # Test case 3
    rectangles = [[1, 1], [2, 2], [3, 3], [4, 4]]
    print(solution.countGoodRectangles(rectangles))  # Expected output: 1

    # Test case 4
    rectangles = [[5, 5], [5, 5], [5, 5], [5, 5]]
    print(solution.countGoodRectangles(rectangles))  # Expected output: 4

    # Test case 5
    rectangles = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(solution.countGoodRectangles(rectangles))  # Expected output: 1

test_count_good_rectangles()