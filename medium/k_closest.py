import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(p[0]**2 + p[1]**2, p) for p in points]
        
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]

def test_k_closest():
    solution = Solution()
    
    # Test case 1
    points = [[1,3],[-2,2]]
    k = 1
    print(solution.kClosest(points, k))  # Expected output: [[-2,2]]

    # Test case 2
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(solution.kClosest(points, k))  # Expected output: [[3,3],[-2,4]]

    # Test case 3
    points = [[0,1],[1,0]]
    k = 2
    print(solution.kClosest(points, k))  # Expected output: [[0,1],[1,0]]

    # Test case 4
    points = [[1,2],[2,3],[3,4],[0,0]]
    k = 3
    print(solution.kClosest(points, k))  # Expected output: [[0,0],[1,2],[2,3]]

    # Test case 5
    points = [[-1,-1],[2,2],[3,3],[0,0]]
    k = 2
    print(solution.kClosest(points, k))  # Expected output: [[0,0],[-1,-1]]

test_k_closest()