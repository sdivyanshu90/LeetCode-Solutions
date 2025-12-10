from typing import List

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0
                    max_area = max(max_area, area)
        return max_area

def test_largest_triangle_area():
    solution = Solution()

    # Test Case 1
    points1 = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(solution.largestTriangleArea(points1)) # Expected: 2.0

    # Test Case 2
    points2 = [[1,0],[0,0],[0,1]]
    print(solution.largestTriangleArea(points2)) # Expected: 0.5

    # Test Case 3
    points3 = [[-1,-1],[1,0],[0,1]]
    print(solution.largestTriangleArea(points3)) # Expected: 1.5

    # Test Case 4
    points4 = [[0,0],[3,0],[0,4]]
    print(solution.largestTriangleArea(points4)) # Expected: 6.0

    # Test Case 5
    points5 = [[-2,-3],[4,5],[1,1],[2,2]]
    print(solution.largestTriangleArea(points5)) # Expected: 1.0

test_largest_triangle_area()