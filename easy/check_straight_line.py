from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
                return False
        
        return True

def test_check_straight_line():
    solution = Solution()

    # Test case 1
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(solution.checkStraightLine(coordinates))  # Expected output: True

    # Test case 2
    coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    print(solution.checkStraightLine(coordinates))  # Expected output: False

    # Test case 3
    coordinates = [[0,0],[0,1],[0,2],[0,3]]
    print(solution.checkStraightLine(coordinates))  # Expected output: True

    # Test case 4
    coordinates = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    print(solution.checkStraightLine(coordinates))  # Expected output: True

    # Test case 5
    coordinates = [[1,2],[2,4],[3,6],[4,8],[5,10]]
    print(solution.checkStraightLine(coordinates))  # Expected output: True

test_check_straight_line()