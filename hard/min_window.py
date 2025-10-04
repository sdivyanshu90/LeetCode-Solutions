from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1

        required = len(dictT)
        l, r = 0, 0
        formed = 0

        windowCounts = defaultdict(int)
        ans = [-1, 0, 0]

        while r < len(s):
            c = s[r]
            windowCounts[c] += 1

            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]

                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == -1 else s[ans[1]:ans[2] + 1]

def test_min_window():
    solution = Solution()

    # Test case 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    print(solution.minWindow(s1, t1))  # Expected output: "BANC"

    # Test case 2
    s2 = "a"
    t2 = "a"
    print(solution.minWindow(s2, t2))  # Expected output: "a"

    # Test case 3
    s3 = "a"
    t3 = "aa"
    print(solution.minWindow(s3, t3))  # Expected output: ""

    # Test case 4
    s4 = "ab"
    t4 = "A"
    print(solution.minWindow(s4, t4))  # Expected output: ""

    # Test case 5
    s5 = "aaflslflsldkalskaaa"
    t5 = "aaa"
    print(solution.minWindow(s5, t5))  # Expected output: "aaa"

    # Test case 6
    s6 = "aa"
    t6 = "aa"
    print(solution.minWindow(s6, t6))  # Expected output: "aa"

    # Test case 7
    s7 = "bba"
    t7 = "ab"
    print(solution.minWindow(s7, t7))  # Expected output: "ba"

    # Test case 8
    s8 = "cabwefgewcwaefgcf"
    t8 = "cae"
    print(solution.minWindow(s8, t8))  # Expected output: "cwaef"

    # Test case 9
    s9 = "ab"
    t9 = "b"
    print(solution.minWindow(s9, t9))  # Expected output: "b"

    # Test case 10
    s10 = "abcde"
    t10 = "e"
    print(solution.minWindow(s10, t10))  # Expected output: "e"

test_min_window()