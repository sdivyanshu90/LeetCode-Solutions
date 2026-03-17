class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        for i in range(len(points)):
            ans = max(ans, points[i][0] - points[i - 1][0])
        return ans

def test_max_width_of_vertical_area():
    solution = Solution()

    # Test case 1
    points1 = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(solution.maxWidthOfVerticalArea(points1))  # Expected output: 1

    # Test case 2
    points2 = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    print(solution.maxWidthOfVerticalArea(points2))  # Expected output: 3

    # Test case 3
    points3 = [[1, 1], [3, 1], [5, 1], [7, 1], [9, 1]]
    print(solution.maxWidthOfVerticalArea(points3))  # Expected output: 2

    # Test case 4
    points4 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    print(solution.maxWidthOfVerticalArea(points4))  # Expected output: 1

    # Test case 5
    points5 = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]
    print(solution.maxWidthOfVerticalArea(points5))  # Expected output: 0

test_max_width_of_vertical_area()