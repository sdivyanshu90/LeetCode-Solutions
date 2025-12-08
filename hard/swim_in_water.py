import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0

        while heap:
            t, r, c = heapq.heappop(heap)
            res = max(res, t)
            if (r, c) == (n-1, n-1):
                return res
            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
        return res

def test_swim_in_water():
    solution = Solution()
    
    # Test case 1
    grid = [[0,2],[1,3]]
    print(solution.swimInWater(grid)) # Expected: 3
    
    # Test case 2
    grid = [[0,1,2,3,4],
            [24,23,22,21,5],
            [12,13,14,15,16],
            [11,17,18,19,20],
            [10,9,8,7,6]]
    print(solution.swimInWater(grid)) # Expected: 16
    
    # Test case 3
    grid = [[7,34,6,1,9,4],
            [14,2,8,15,10,3],
            [23,20,5,19,12,11],
            [16,28,25,24,27,13],
            [29,17,30,21,22,18],
            [35,32,31,33,0,26]]
    print(solution.swimInWater(grid)) # Expected: 26

    # Test case 4
    grid = [[0]]
    print(solution.swimInWater(grid)) # Expected: 0

    # Test case 5
    grid = [[10,12,15],
            [9,11,13],
            [8,7,6]]
    print(solution.swimInWater(grid)) # Expected: 10

test_swim_in_water()