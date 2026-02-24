from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        max_day = max(event[1] for event in events)
        events.sort()
        pq = []
        ans, j = 0, 0
        for i in range(1, max_day + 1):
            while j < n and events[j][0] <= i:
                heapq.heappush(pq, events[j][1])
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans += 1

        return ans

def test_maxEvents():
    solution = Solution()

    # Test case 1
    events1 = [[1, 2], [2, 3], [3, 4]]
    print(solution.maxEvents(events1)) # Expected output: 3

    # Test case 2
    events2 = [[1, 2], [2, 3], [3, 4], [1, 2]]
    print(solution.maxEvents(events2)) # Expected output: 4

    # Test case 3
    events3 = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
    print(solution.maxEvents(events3)) # Expected output: 4

    # Test case 4
    events4 = [[1, 100000]]
    print(solution.maxEvents(events4)) # Expected output: 1

    # Test case 5
    events5 = [[1, 2], [1, 2], [1, 6], [1, 6], [1, 6]]
    print(solution.maxEvents(events5)) # Expected output: 5

test_maxEvents()