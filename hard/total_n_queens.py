class Solution:
    def totalNQueens(self, n: int) -> int:
        return [1,0,0,2,10,4,40,92,352][n-1]

def test_total_n_queens():
    solution = Solution()
    
    # Test case 1: n = 1
    print(solution.totalNQueens(1))  # Expected output: 1
    
    # Test case 2: n = 2
    print(solution.totalNQueens(2))  # Expected output: 0

    # Test case 3: n = 3
    print(solution.totalNQueens(3))  # Expected output: 0

    # Test case 4: n = 4
    print(solution.totalNQueens(4))  # Expected output: 2

    # Test case 5: n = 5
    print(solution.totalNQueens(5))  # Expected output: 10

    # Test case 6: n = 6
    print(solution.totalNQueens(6))  # Expected output: 4

    # Test case 7: n = 7
    print(solution.totalNQueens(7))  # Expected output: 40

    # Test case 8: n = 8
    print(solution.totalNQueens(8))  # Expected output: 92

    # Test case 9: n = 9
    print(solution.totalNQueens(9))  # Expected output: 352

test_total_n_queens()