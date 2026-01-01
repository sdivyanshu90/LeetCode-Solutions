from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        suffix_sum = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        for i in range(length + 1):
            dp[i][length] = suffix_sum[i]

        for index in range(length - 1, -1, -1):
            for max_till_now in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till_now, length - index) + 1):
                    dp[index][max_till_now] = max(
                        dp[index][max_till_now],
                        suffix_sum[index] - dp[index + X][max(max_till_now, X)],
                    )
        return dp[0][1]

def test_stone_game_ii():
    solution = Solution()

    # Test case 1
    piles = [2,7,9,4,4]
    print(solution.stoneGameII(piles))  # Expected output: 10

    # Test case 2
    piles = [1,2,3,4,5,100]
    print(solution.stoneGameII(piles))  # Expected output: 104

    # Test case 3
    piles = [5,3,4,5]
    print(solution.stoneGameII(piles))  # Expected output: 10

    # Test case 4
    piles = [1,1,1,1,1,1]
    print(solution.stoneGameII(piles))  # Expected output: 4

    # Test case 5
    piles = [10,20,30,40,50]
    print(solution.stoneGameII(piles))  # Expected output: 90

test_stone_game_ii()