class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        return count

def test_countNegatives():
    solution = Solution()

    # Test case 1
    grid1 = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    print(solution.countNegatives(grid1)) # Expected output: 8

    # Test case 2
    grid2 = [[3, 2], [1, 0]]
    print(solution.countNegatives(grid2)) # Expected output: 0

    # Test case 3
    grid3 = [[1, -1], [-1, -1]]
    print(solution.countNegatives(grid3)) # Expected output: 3

    # Test case 4
    grid4 = [[-1]]
    print(solution.countNegatives(grid4)) # Expected output: 1

    # Test case 5
    grid5 = [[0, -1, -2], [-3, -4, -5], [-6, -7, -8]]
    print(solution.countNegatives(grid5)) # Expected output: 8

test_countNegatives()