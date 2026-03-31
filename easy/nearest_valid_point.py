class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid = []
        for i, (x2, y2) in enumerate(points):
            if x2 == x or y2 == y:
                valid.append((abs(x - x2) + abs(y - y2), i))
        # print(valid)

        if valid:
            return min(valid)[1]
        return -1            

def test_nearest_valid_point():
    # Test case 1
    solution = Solution()
    x1, y1 = 3, 4
    points1 = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    print(solution.nearestValidPoint(x1, y1, points1))  # Expected output: 2

    # Test case 2
    x2, y2 = 3, 4
    points2 = [[3,4]]
    print(solution.nearestValidPoint(x2, y2, points2))  # Expected output: 0

    # Test case 3
    x3, y3 = 3, 4
    points3 = [[2,3]]
    print(solution.nearestValidPoint(x3, y3, points3))  # Expected output: -1

    # Test case 4
    x4, y4 = 3, 4
    points4 = [[1,4],[2,4],[3,4],[4,4],[5,4]]
    print(solution.nearestValidPoint(x4, y4, points4))  # Expected output: 2

    # Test case 5
    x5, y5 = 3, 4
    points5 = [[1,2],[3,1],[2,4],[2,3],[4,4],[3,4]]
    print(solution.nearestValidPoint(x5, y5, points5))  # Expected output: 2

test_nearest_valid_point()