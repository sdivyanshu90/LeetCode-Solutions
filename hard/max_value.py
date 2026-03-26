class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda ans: ans[1])
        
        dp = [[0, 0]]
        dp2 = [[0, 0]]
        
        for x in range(k):
            for s, e, v in events:
                i = bisect.bisect_left(dp, [s]) - 1
                
                if dp[i][1] + v > dp2[-1][1]:
                    dp2.append([e, dp[i][1] + v])
            
            dp = dp2
            dp2 = [[0, 0]]
        
        return dp[-1][-1]

def test_max_value():
    solution = Solution()

    # Test Case 1
    events1 = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    k1 = 2
    print(solution.maxValue(events1, k1)) # Expected Output: 7

    # Test Case 2
    events2 = [[1, 2, 4], [3, 4, 3], [2, 3, 10]]
    k2 = 2
    print(solution.maxValue(events2, k2)) # Expected Output: 10

    # Test Case 3
    events3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]
    k3 = 3
    print(solution.maxValue(events3, k3)) # Expected Output: 9

    # Test Case 4
    events4 = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    k4 = 1
    print(solution.maxValue(events4, k4)) # Expected Output: 4

    # Test Case 5
    events5 = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    k5 = 3
    print(solution.maxValue(events5, k5)) # Expected Output: 7

test_max_value()