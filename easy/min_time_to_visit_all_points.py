from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            res += max(abs(y2-y1), abs(x2-x1))
        return res

def test_min_time_to_visit_all_points():
    solution = Solution()

    # Test case 1
    points = [[1,1],[3,4],[-1,0]]
    print(solution.minTimeToVisitAllPoints(points))  # Expected output: 7

    # Test case 2
    points = [[3,2],[-2,2]]
    print(solution.minTimeToVisitAllPoints(points))  # Expected output: 5

    # Test case 3
    points = [[0,0],[1,1],[1,0]]
    print(solution.minTimeToVisitAllPoints(points))  # Expected output: 2

    # Test case 4
    points = [[0,0],[2,2],[3,3]]
    print(solution.minTimeToVisitAllPoints(points))  # Expected output: 3

    # Test case 5
    points = [[0,0],[1,1],[2,2],[3,3]]
    print(solution.minTimeToVisitAllPoints(points))  # Expected output: 3

test_min_time_to_visit_all_points()