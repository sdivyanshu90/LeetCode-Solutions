from functools import reduce
import math
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return reduce(
            lambda st, p: (st[0] + 1, p[1]) if p[0] > st[1] else st,
            sorted(points, key=lambda p: p[1]),
            (0, -math.inf),
        )[0]

def test_find_min_arrow_shots():
    s = Solution()

    # Test case 1
    points = [[10,16],[2,8],[1,6],[7,12]]
    print(s.findMinArrowShots(points))  # Expected output: 2

    # Test case 2
    points = [[1,2],[3,4],[5,6],[7,8]]
    print(s.findMinArrowShots(points))  # Expected output: 4

    # Test case 3
    points = [[1,2],[2,3],[3,4],[4,5]]
    print(s.findMinArrowShots(points))  # Expected output: 2

    # Test case 4
    points = [[1,10],[2,3],[4,5],[6,7],[8,9]]
    print(s.findMinArrowShots(points))  # Expected output: 4

    # Test case 5
    points = [[1,5],[2,6],[3,7],[4,8]]
    print(s.findMinArrowShots(points))  # Expected output: 1

test_find_min_arrow_shots()