import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first != second:
                heapq.heappush(stones, first - second)
        
        return -stones[0] if stones else 0

def test_last_stone_weight():
    solution = Solution()

    # Test case 1
    stones = [2,7,4,1,8,1]
    print(solution.lastStoneWeight(stones))  # Expected output: 1

    # Test case 2
    stones = [1]
    print(solution.lastStoneWeight(stones))  # Expected output: 1

    # Test case 3
    stones = [3,3,3,3]
    print(solution.lastStoneWeight(stones))  # Expected output: 0

    # Test case 4
    stones = [10,4,2,10]
    print(solution.lastStoneWeight(stones))  # Expected output: 2

    # Test case 5
    stones = [5,5,5,5,5]
    print(solution.lastStoneWeight(stones))  # Expected output: 5

test_last_stone_weight()