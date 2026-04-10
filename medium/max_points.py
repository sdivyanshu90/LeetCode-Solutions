class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cols = len(points[0])
        current_row = [0] * cols
        previous_row = [0] * cols

        for row in points:
            running_max = 0
            for col in range(cols):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = running_max

            running_max = 0
            for col in range(cols - 1, -1, -1):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = max(current_row[col], running_max) + row[col]
            previous_row = current_row.copy()
        return max(previous_row)

def test_max_points():
    solution = Solution()

    # Test case 1
    points1 = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    print(solution.maxPoints(points1))  # Expected output: 9

    # Test case 2
    points2 = [[1, 5], [2, 3], [4, 2]]
    print(solution.maxPoints(points2))  # Expected output: 11

    # Test case 3
    points3 = [[10]]
    print(solution.maxPoints(points3))  # Expected output: 10

    # Test case 4
    points4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.maxPoints(points4))  # Expected output: 29

    # Test case 5
    points5 = [[1, 1000], [1000, 1]]
    print(solution.maxPoints(points5))  # Expected output: 1000

test_max_points()