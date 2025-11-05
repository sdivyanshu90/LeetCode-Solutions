from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat: return []
        m, n = len(mat), len(mat[0])
        diag = defaultdict(list)

        for i in range(m):
            for j in range(n):
                diag[i+j].append(mat[i][j])

        res = []
        for k in range(m+n-1):
            if k % 2 == 0:
                res.extend(diag[k][::-1])
            else:
                res.extend(diag[k])
        return res

def test_find_diagonal_order():
    s = Solution()

    # Test case 1
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.findDiagonalOrder(mat))  # Expected output: [1, 2, 4, 7, 5, 3, 6, 8, 9]

    # Test case 2
    mat = [[1, 2], [3, 4]]
    print(s.findDiagonalOrder(mat))  # Expected output: [1, 2, 3, 4]

    # Test case 3
    mat = [[1]]
    print(s.findDiagonalOrder(mat))  # Expected output: [1]

    # Test case 4
    mat = [[1, 2, 3, 4]]
    print(s.findDiagonalOrder(mat))  # Expected output: [1, 2, 3, 4]

    # Test case 5
    mat = [[1], [2], [3], [4]]
    print(s.findDiagonalOrder(mat))  # Expected output: [1, 2, 3, 4]

test_find_diagonal_order()