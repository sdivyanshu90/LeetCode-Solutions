from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])

        r_min_max = float('-inf')
        for i in range(N):
            r_min = min(matrix[i])  
            r_min_max = max(r_min_max, r_min)

        c_max_min = float('inf')
        for i in range(M):
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []

def test_lucky_numbers():
    solution = Solution()

    # Test case 1
    matrix1 = [[3, 7], [8, 5]]
    print(solution.luckyNumbers(matrix1))  # Expected output: []

    # Test case 2
    matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(solution.luckyNumbers(matrix2))  # Expected output: [12]

    # Test case 3
    matrix3 = [[7, 8], [1, 2]]
    print(solution.luckyNumbers(matrix3))  # Expected output: [7]

    # Test case 4
    matrix4 = [[5]]
    print(solution.luckyNumbers(matrix4))  # Expected output: [5]

    # Test case 5
    matrix5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.luckyNumbers(matrix5))  # Expected output: [7]

test_lucky_numbers()