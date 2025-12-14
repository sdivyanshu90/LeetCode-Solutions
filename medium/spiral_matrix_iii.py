from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        visited = rows * cols - 1
        output = [[rStart, cStart]]
        delta = 1
        count = 2
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        curr_dir = 0

        while visited > 0:
            if count <= 0:
                count = 2
                delta += 1

            if count > 0:
                dx,dy = directions[curr_dir]
                for i in range(delta):
                    rStart += dx
                    cStart += dy
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        visited -= 1
                        output.append((rStart, cStart))
                count -= 1
                curr_dir = (curr_dir + 1) % 4
        return output

def test_spiral_matrix_iii():
    solution = Solution()

    # Test case 1
    rows1, cols1, rStart1, cStart1 = 1, 4, 0, 0
    print(solution.spiralMatrixIII(rows1, cols1, rStart1, cStart1))  # Expected output: [[0,0],[0,1],[0,2],[0,3]]

    # Test case 2
    rows2, cols2, rStart2, cStart2 = 5, 6, 1, 4
    print(solution.spiralMatrixIII(rows2, cols2, rStart2, cStart2))
    # Expected output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

    # Test case 3
    rows3, cols3, rStart3, cStart3 = 3, 3, 0, 0
    print(solution.spiralMatrixIII(rows3, cols3, rStart3, cStart3))
    # Expected output: [[0,0],[0,1],[1,1],[1,0],[2,0],[2,1],[2,2],[1,2],[0,2]]

    # Test case 4
    rows4, cols4, rStart4, cStart4 = 2, 2, 0, 1
    print(solution.spiralMatrixIII(rows4, cols4, rStart4, cStart4))
    # Expected output: [[0,1],[0,0],[1,0],[1,1]]

    # Test case 5
    rows5, cols5, rStart5, cStart5 = 4, 4, 2, 2
    print(solution.spiralMatrixIII(rows5, cols5, rStart5, cStart5))
    # Expected output: [[2,2],[2,3],[3,3],[3,2],[3,1],[2,1],[1,1],[1,2],[1,3],[0,3],[0,2],[0,1],[0,0],[1,0],[2,0],[3,0]]

test_spiral_matrix_iii()