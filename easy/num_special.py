class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    row_count[row] += 1
                    col_count[col] += 1
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    if row_count[row] == 1 and col_count[col] == 1:
                        ans += 1

        return ans

def test_num_special():
    solution = Solution()

    # Test case 1
    mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    print(solution.numSpecial(mat))  # Expected output: 1

    # Test case 2
    mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print(solution.numSpecial(mat))  # Expected output: 3

    # Test case 3
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(solution.numSpecial(mat))  # Expected output: 0

    # Test case 4
    mat = [[1]]
    print(solution.numSpecial(mat))  # Expected output: 1

    # Test case 5
    mat = [[1, 1], [1, 1]]
    print(solution.numSpecial(mat))  # Expected output: 0

test_num_special()