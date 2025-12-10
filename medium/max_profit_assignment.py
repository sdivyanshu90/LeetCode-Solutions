from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)
        jobs = [0] * (maxAbility + 1)

        for i in range(len(difficulty)):
            if difficulty[i] <= maxAbility:
                jobs[difficulty[i]] = max(jobs[difficulty[i]], profit[i])

        for i in range(1, maxAbility + 1):
            jobs[i] = max(jobs[i], jobs[i - 1])
        netProfit = 0
        for ability in worker:
            netProfit += jobs[ability]
        return netProfit

def test_max_profit_assignment():
    solution = Solution()

    # Test Case 1
    difficulty1 = [2,4,6,8,10]
    profit1 = [10,20,30,40,50]
    worker1 = [4,5,6,7]
    print(solution.maxProfitAssignment(difficulty1, profit1, worker1)) # Expected: 100

    # Test Case 2
    difficulty2 = [85,47,57]
    profit2 = [24,66,99]
    worker2 = [40,25,25]
    print(solution.maxProfitAssignment(difficulty2, profit2, worker2)) # Expected: 0

    # Test Case 3
    difficulty3 = [2,4,6,8,10]
    profit3 = [10,20,30,40,50]
    worker3 = [5,5,5,5]
    print(solution.maxProfitAssignment(difficulty3, profit3, worker3)) # Expected: 80

    # Test Case 4
    difficulty4 = [1,2,3]
    profit4 = [10,20,30]
    worker4 = [3,2,1,4]
    print(solution.maxProfitAssignment(difficulty4, profit4, worker4)) # Expected: 100

    # Test Case 5
    difficulty5 = [5,10,15]
    profit5 = [10,20,30]
    worker5 = [10,10,10]
    print(solution.maxProfitAssignment(difficulty5, profit5, worker5)) # Expected: 60

test_max_profit_assignment()