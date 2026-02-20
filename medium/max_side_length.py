from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])        
        P = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                P[r+1][c+1] = P[r][c+1] + P[r+1][c] - P[r][c] + mat[r][c]
        
        current_len = 0
        for r in range(rows):
            for c in range(cols):
                next_len = current_len + 1                
                if r - next_len + 1 >= 0 and c - next_len + 1 >= 0:
                    r1 = r - next_len + 1
                    c1 = c - next_len + 1                    
                    total = (P[r+1][c+1] 
                           - P[r1][c+1] 
                           - P[r+1][c1] 
                           + P[r1][c1])
                    if total <= threshold:
                        current_len += 1
        return current_len

def test_max_side_length():
    solution = Solution()

    # Test case 1
    mat = [[1,1,3],[2,2,4],[1,1,5]]
    threshold = 4
    print(solution.maxSideLength(mat, threshold))  # Expected output: 2

    # Test case 2
    mat = [[2,2,2],[2,2,2],[2,2,2]]
    threshold = 1
    print(solution.maxSideLength(mat, threshold))  # Expected output: 0

    # Test case 3
    mat = [[1,1,1],[1,0,1],[1,1,1]]
    threshold = 6
    print(solution.maxSideLength(mat, threshold))  # Expected output: 3

    # Test case 4
    mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
    threshold = 40184
    print(solution.maxSideLength(mat, threshold))  # Expected output: 2

    # Test case 5
    mat = [[34,28],[53,56],[86,19],[92,22],[49,21],[62,27],[93,86]]
    threshold = 40184
    print(solution.maxSideLength(mat, threshold))  # Expected output: 2

test_max_side_length()