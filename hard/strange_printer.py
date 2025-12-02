class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        a = [s[0]]
        for i in range(1, n):
            if s[i] != s[i - 1]:
                a.append(s[i])
        n = len(a)
        h = {}
        t = [n] * n
        for i in reversed(range(n)):
            if a[i] in h:
                t[i] = h[a[i]]
            h[a[i]] = i
        d = [[0] * n for _ in range(n + 1)]
        for i in range(n):
            d[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                d[i][j] = 1 + d[i + 1][j]
                k = t[i]
                while k <= j:
                    d[i][j] = min(d[i][j], d[i][k - 1] + d[k + 1][j])
                    k = t[k]
        return d[0][n - 1]

def test_strange_printer():
    solution = Solution()

    # Test Case 1
    s1 = "aaabbb"
    print(solution.strangePrinter(s1)) # Expected: 2

    # Test Case 2
    s2 = "aba"
    print(solution.strangePrinter(s2)) # Expected: 2

    # Test Case 3
    s3 = "abcabc"
    print(solution.strangePrinter(s3)) # Expected: 5

    # Test Case 4
    s4 = "a"
    print(solution.strangePrinter(s4)) # Expected: 1

    # Test Case 5
    s5 = "abababab"
    print(solution.strangePrinter(s5)) # Expected: 4

test_strange_printer()