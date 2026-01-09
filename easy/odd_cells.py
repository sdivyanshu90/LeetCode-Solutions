from typing import List

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rowCount = [0] * m
        colCount = [0] * n
        
        for r, c in indices:
            rowCount[r] += 1
            colCount[c] += 1
        
        oddRows = sum(1 for x in rowCount if x % 2 == 1)
        oddCols = sum(1 for x in colCount if x % 2 == 1)
        evenRows = m - oddRows
        evenCols = n - oddCols
        
        return oddRows * evenCols + evenRows * oddCols

def test_odd_cells():
    solution = Solution()

    # Test case 1
    m = 2
    n = 3
    indices = [[0,1],[1,1]]
    print(solution.oddCells(m, n, indices))  # Expected output: 6

    # Test case 2
    m = 2
    n = 2
    indices = [[1,1],[0,0]]
    print(solution.oddCells(m, n, indices))  # Expected output: 0

    # Test case 3
    m = 3
    n = 3
    indices = [[0,0],[1,1],[2,2]]
    print(solution.oddCells(m, n, indices))  # Expected output: 9

    # Test case 4
    m = 1
    n = 4
    indices = [[0,0],[0,1],[0,2],[0,3]]
    print(solution.oddCells(m, n, indices))  # Expected output: 4

    # Test case 5
    m = 4
    n = 1
    indices = [[0,0],[1,0],[2,0],[3,0]]
    print(solution.oddCells(m, n, indices))  # Expected output: 4

test_odd_cells()