class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        alloc_ladders = []
        for i in range(len(heights)-1):
            steps = heights[i+1] - heights[i]
            if steps <= 0:
                continue
            heapq.heappush(alloc_ladders, steps)
            if len(alloc_ladders) > ladders:
                bricks -= heapq.heappop(alloc_ladders)
            if bricks < 0:
                return i
        return len(heights) - 1

def test_furthest_building():
    solution = Solution()

    # Test case 1
    heights1 = [4, 2, 7, 6, 9, 14, 12]
    bricks1 = 5
    ladders1 = 1
    print(solution.furthestBuilding(heights1, bricks1, ladders1))  # Expected output: 4

    # Test case 2
    heights2 = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks2 = 10
    ladders2 = 2
    print(solution.furthestBuilding(heights2, bricks2, ladders2))  # Expected output: 7

    # Test case 3
    heights3 = [14, 3, 19, 3]
    bricks3 = 17
    ladders3 = 0
    print(solution.furthestBuilding(heights3, bricks3, ladders3))  # Expected output: 3

    # Test case 4
    heights4 = [1, 5, 1, 2, 3, 4, 10000]
    bricks4 = 4
    ladders4 = 1
    print(solution.furthestBuilding(heights4, bricks4, ladders4))  # Expected output: 5

    # Test case 5
    heights5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    bricks5 = 0
    ladders5 = 2
    print(solution.furthestBuilding(heights5, bricks5, ladders5))  # Expected output: 2

test_furthest_building()