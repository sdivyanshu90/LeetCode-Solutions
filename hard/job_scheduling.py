from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda tup : tup[1])

        dp = [[0,0]] 
        for st, et, pf in jobs:
            j = len(dp) - 1
            while j > 0 and st < dp[j][0]:
                j -= 1
            
            newProfit = dp[j][1] + pf
            if newProfit > dp[-1][1]:
                dp.append([et, newProfit])
        return dp[-1][1]

def test_job_scheduling():
    solution = Solution()

    # Test case 1
    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    print(solution.jobScheduling(startTime, endTime, profit))  # Expected output: 120

    # Test case 2
    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    print(solution.jobScheduling(startTime, endTime, profit))  # Expected output: 150

    # Test case 3
    startTime = [1,1,1]
    endTime = [2,3,4]
    profit = [5,6,4]
    print(solution.jobScheduling(startTime, endTime, profit))  # Expected output: 6

    # Test case 4
    startTime = [4,2,4,8,2]
    endTime = [5,5,5,10,8]
    profit = [1,2,8,10,4]
    print(solution.jobScheduling(startTime, endTime, profit))  # Expected output: 18

    # Test case 5
    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]
    print(solution.jobScheduling(startTime, endTime, profit))  # Expected output: 150

test_job_scheduling()