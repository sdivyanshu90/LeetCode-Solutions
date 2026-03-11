class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        trailing = []
        for row in grid:
            count = 0
            for x in reversed(row):
                if x == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        for i in range(n):
            needed = n - i - 1
            j = i
            
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps

def test_min_swaps():
    solution = Solution()

    # Test case 1
    grid1 = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    print(solution.minSwaps(grid1))  # Expected output: 3

    # Test case 2
    grid2 = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    print(solution.minSwaps(grid2))  # Expected output: -1

    # Test case 3
    grid3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(solution.minSwaps(grid3))  # Expected output: 0

    # Test case 4
    grid4 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(solution.minSwaps(grid4))  # Expected output: -1

    # Test case 5
    grid5 = [[0]]
    print(solution.minSwaps(grid5))  # Expected output: 0

test_min_swaps()