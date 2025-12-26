from collections import defaultdict
from typing import List

class Solution:
    def numSubmatrixSumTarget(self, M: List[List[int]], T: int) -> int:
        xlen, ylen, ans, res = len(M[0]), len(M), 0, defaultdict(int)
        for r in M:
            for j in range(1, xlen):
                r[j] += r[j-1]
        for j in range(xlen):
            for k in range(j, xlen):
                res.clear()
                res[0], csum = 1, 0
                for i in range(ylen):
                    csum += M[i][k] - (M[i][j-1] if j else 0)
                    ans += res[csum - T]
                    res[csum] += 1
        return ans

def test_num_submatrix_sum_target():
    solution = Solution()

    # Test case 1
    M1 = [[0,1,0],[1,1,1],[0,1,0]]
    T1 = 0
    print(solution.numSubmatrixSumTarget(M1, T1))  # Expected output: 4

    # Test case 2
    M2 = [[1,-1],[-1,1]]
    T2 = 0
    print(solution.numSubmatrixSumTarget(M2, T2))  # Expected output: 5

    # Test case 3
    M3 = [[904]]
    T3 = 0
    print(solution.numSubmatrixSumTarget(M3, T3))  # Expected output: 0

    # Test case 4
    M4 = [[1,2,3],[4,5,6],[7,8,9]]
    T4 = 12
    print(solution.numSubmatrixSumTarget(M4, T4))  # Expected output: 4

    # Test case 5
    M5 = [[-1,-1],[-1,1]]
    T5 = 0
    print(solution.numSubmatrixSumTarget(M5, T5))  # Expected output: 1

test_num_submatrix_sum_target()