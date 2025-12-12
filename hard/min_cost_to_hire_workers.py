from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        total_cost = float("inf")
        current_total_quality = 0
        wage_to_quality_ratio = []

        for i in range(n):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        wage_to_quality_ratio.sort(key=lambda x: x[0])
        highest_quality_workers = []

        for i in range(n):
            heapq.heappush(highest_quality_workers, -wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)

            if len(highest_quality_workers) == k:
                total_cost = min(
                    total_cost, current_total_quality * wage_to_quality_ratio[i][0]
                )
        return total_cost

def test_mincostToHireWorkers():
    solution = Solution()
    
    # Test Case 1
    print(abs(solution.mincostToHireWorkers([10,20,5], [70,50,30], 2) - 105.0)) # Expected: 0.0

    # Test Case 2
    print(abs(solution.mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3) - 30.66667)) # Expected: 3.3333333355756167e-06

    # Test Case 3
    print(abs(solution.mincostToHireWorkers([5,10,15], [70,20,30], 3) - 105.0)) # Expected: 315.0

    # Test Case 4
    print(abs(solution.mincostToHireWorkers([4,2,1], [8,4,2], 2) - 12.0)) # Expected: 6.0

    # Test Case 5
    print(abs(solution.mincostToHireWorkers([1,2,3,4,5], [10,20,30,40,50], 3) - 60.0)) # Expected: 0.0

test_mincostToHireWorkers()