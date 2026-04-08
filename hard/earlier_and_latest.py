class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @cache
        def dp(n: int, f: int, s: int) -> (int, int):
            if f + s == n + 1:
                return (1, 1)

            if f + s > n + 1:
                return dp(n, n + 1 - s, n + 1 - f)

            earliest, latest = float("inf"), float("-inf")
            n_half = (n + 1) // 2

            if s <= n_half:
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(n_half, i + 1, i + j + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)
            else:
                s_prime = n + 1 - s
                mid = (n - 2 * s_prime + 1) // 2
                for i in range(f):
                    for j in range(s_prime - f):
                        x, y = dp(n_half, i + 1, i + j + mid + 2)
                        earliest = min(earliest, x)
                        latest = max(latest, y)

            return (earliest + 1, latest + 1)

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [earliest, latest]

def test_earliest_and_latest():
    solution = Solution()

    # Test case 1
    n = 11
    firstPlayer = 2
    secondPlayer = 4
    print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))  # Expected output: [3, 4]

    # Test case 2
    n = 5
    firstPlayer = 1
    secondPlayer = 5
    print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))  # Expected output: [1, 1]

    # Test case 3
    n = 6
    firstPlayer = 1
    secondPlayer = 6
    print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))  # Expected output: [1, 1]

    # Test case 4
    n = 12
    firstPlayer = 2
    secondPlayer = 11
    print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))  # Expected output: [2, 2]

    # Test case 5
    n = 10
    firstPlayer = 3
    secondPlayer = 7
    print(solution.earliestAndLatest(n, firstPlayer, secondPlayer))  # Expected output: [3, 4]

test_earliest_and_latest()