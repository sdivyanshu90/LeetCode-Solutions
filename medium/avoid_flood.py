from collections import defaultdict
import heapq
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        nextRain = defaultdict(list)
        for i, lake in enumerate(rains):
            if lake > 0:
                nextRain[lake].append(i)

        heap = []
        full = set()
        ans = [-1] * n

        for i, lake in enumerate(rains):
            if lake > 0:
                if lake in full:
                    return []
                full.add(lake)
                nextRain[lake].pop(0)
                if nextRain[lake]:
                    heapq.heappush(heap, (nextRain[lake][0], lake))
                ans[i] = -1
            else:
                if heap:
                    _, lakeToDry = heapq.heappop(heap)
                    full.remove(lakeToDry)
                    ans[i] = lakeToDry
                else:
                    ans[i] = 1
        return ans

def test_avoid_flood():
    solution = Solution()

    # Test Case 1
    rains1 = [1, 2, 0, 0, 2, 1]
    print(solution.avoidFlood(rains1))  # Expected output: [-1, -1, 2, 1, -1, -1]

    # Test Case 2
    rains2 = [1, 2, 0, 1, 2]
    print(solution.avoidFlood(rains2))  # Expected output: []

    # Test Case 3
    rains3 = [0, 1, 1]
    print(solution.avoidFlood(rains3))  # Expected output: []

    # Test Case 4
    rains4 = [0, 0, 0]
    print(solution.avoidFlood(rains4))  # Expected output: [1, 1, 1]

    # Test Case 5
    rains5 = [69]
    print(solution.avoidFlood(rains5))  # Expected output: [-1]

test_avoid_flood()