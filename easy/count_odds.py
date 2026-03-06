class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

def test_count_odds():
    solution = Solution()

    # Test case 1
    low1 = 3
    high1 = 7
    print(solution.countOdds(low1, high1))  # Expected output: 3

    # Test case 2
    low2 = 8
    high2 = 10
    print(solution.countOdds(low2, high2))  # Expected output: 1

    # Test case 3
    low3 = 1
    high3 = 10
    print(solution.countOdds(low3, high3))  # Expected output: 5

    # Test case 4
    low4 = 0
    high4 = 0
    print(solution.countOdds(low4, high4))  # Expected output: 0

    # Test case 5
    low5 = 0
    high5 = 1
    print(solution.countOdds(low5, high5))  # Expected output: 1

test_count_odds()