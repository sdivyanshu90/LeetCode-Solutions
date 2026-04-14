from typing import List

class Solution:
    MOD = 1_000_000_007
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for src in range(n):
            for dest in range(n):
                if src != dest:
                    dp[src][dest][0] = int(1e12)
                    dp[src][dest][1] = 0
                else:
                    dp[src][dest][0] = 0
                    dp[src][dest][1] = 1

        for start_node, end_node, travel_time in roads:
            dp[start_node][end_node][0] = travel_time
            dp[end_node][start_node][0] = travel_time
            dp[start_node][end_node][1] = 1
            dp[end_node][start_node][1] = 1

        for mid in range(n):
            for src in range(n):
                for dest in range(n):
                    if src != mid and dest != mid:
                        new_time = dp[src][mid][0] + dp[mid][dest][0]

                        if new_time < dp[src][dest][0]:
                            dp[src][dest][0] = new_time
                            dp[src][dest][1] = (
                                dp[src][mid][1] * dp[mid][dest][1]
                            ) % self.MOD
                        elif new_time == dp[src][dest][0]:

                            dp[src][dest][1] = (
                                dp[src][dest][1]
                                + dp[src][mid][1] * dp[mid][dest][1]
                            ) % self.MOD

        return dp[n - 1][0][1]

def test_count_paths():
    solution = Solution()

    # Test case 1
    n1 = 7
    roads1 = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    print(solution.countPaths(n1, roads1))  # Expected output: 4

    # Test case 2
    n2 = 2
    roads2 = [[1, 0, 10]]
    print(solution.countPaths(n2, roads2))  # Expected output: 1

    # Test case 3
    n3 = 3
    roads3 = [[0, 1, 1], [0, 2, 1], [1, 2, 1]]
    print(solution.countPaths(n3, roads3))  # Expected output: 1

    # Test case 4
    n4 = 4
    roads4 = [[0, 1, 1], [0, 2, 1], [1, 2, 1], [1, 3, 1], [2, 3, 1]]
    print(solution.countPaths(n4, roads4))  # Expected output: 2

    # Test case 5
    n5 = 5
    roads5 = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1], [3, 4, 2]]
    print(solution.countPaths(n5, roads5))  # Expected output: 2

test_count_paths()