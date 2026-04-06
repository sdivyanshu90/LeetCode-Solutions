from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        R = len(grid)
        C = len(grid[0])
        
        d1 = [[0] * C for _ in range(R)]
        d2 = [[0] * C for _ in range(R)]
        
        for r in range(R):
            for c in range(C):
                d1[r][c] = grid[r][c] + (d1[r-1][c-1] if r > 0 and c > 0 else 0)
                d2[r][c] = grid[r][c] + (d2[r-1][c+1] if r > 0 and c + 1 < C else 0)
                
        ans_set = set()
        
        for i in range(R):
            for j in range(C):
                ans_set.add(grid[i][j])
                
                l = 1
                while i - l >= 0 and i + l < R and j - l >= 0 and j + l < C:
                    sum1 = d1[i][j+l] - (d1[i-l-1][j-1] if i-l > 0 and j > 0 else 0)
                    sum2 = d2[i+l][j] - (d2[i-1][j+l+1] if i > 0 and j+l+1 < C else 0)
                    sum3 = d1[i+l][j] - (d1[i-1][j-l-1] if i > 0 and j-l > 0 else 0)
                    sum4 = d2[i][j-l] - (d2[i-l-1][j+1] if i-l > 0 and j+1 < C else 0)
                    
                    total = sum1 + sum2 + sum3 + sum4
                    total -= (grid[i-l][j] + grid[i][j+l] + grid[i+l][j] + grid[i][j-l])
                    
                    ans_set.add(total)
                    l += 1
                    
        return sorted(list(ans_set), reverse=True)[:3]

def test_get_biggest_three():
    solution = Solution()

    # Test case 1
    grid1 = [[7, 7, 7]]
    print(solution.getBiggestThree(grid1))  # Expected output: [7]

    # Test case 2
    grid2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solution.getBiggestThree(grid2))  # Expected output: [20, 9, 8]

    # Test case 3
    grid3 = [[3, 4, 5, 1], [3, 3, 4, 2], [20, 30, 200, 10], [1, 1, 1, 1]]
    print(solution.getBiggestThree(grid3))  # Expected output: [224, 210, 200]

    # Test case 4
    grid4 = [[1]]
    print(solution.getBiggestThree(grid4))  # Expected output: [1]

    # Test case 5
    grid5 = [[9,9],[9,9]]
    print(solution.getBiggestThree(grid5))  # Expected output: [9]

test_get_biggest_three()