class Solution:
    def findRotateSteps(self, s: str, t: str) -> int:
        s = [ord(c) - ord('a') for c in s]
        t = [ord(c) - ord('a') for c in t]
        n, m = len(s), len(t)

        pos = [0] * 26
        for i, c in enumerate(s):
            pos[c] = i

        left = [None] * n
        for i, c in enumerate(s):
            left[i] = pos[:]
            pos[c] = i

        pos = [0] * 26
        for i in range(n - 1, -1, -1):
            pos[s[i]] = i

        right = [None] * n
        for i in range(n - 1, -1, -1):
            right[i] = pos[:]
            pos[s[i]] = i

        pos = [[] for _ in range(26)]
        for i, b in enumerate(s):
            pos[b].append(i)

        f = [0] * n
        for j in range(m - 1, 0, -1):
            c = t[j]
            if c == t[j - 1]:
                continue
            nf = [0] * n
            for i in pos[t[j - 1]]:
                l, r = left[i][c], right[i][c]
                res1 = f[l] + (n - l + i if l > i else i - l)
                res2 = f[r] + (n - i + r if r < i else r - i)
                if res2 < res1 : res1 = res2
                nf[i] = res1          
            f = nf
        if s[0] == t[0]:
            return f[0] + m
        c = t[0]
        l, r = left[0][c], right[0][c]
        return min(f[l] + n - l, f[r] + r) + m

def test_find_rotate_steps():
    solution = Solution()

    # Test Case 1
    s1 = "godding"
    t1 = "gd"
    print(solution.findRotateSteps(s1, t1))  # Expected: 4

    # Test Case 2
    s2 = "abc"
    t2 = "abcbc"
    print(solution.findRotateSteps(s2, t2))  # Expected: 9

    # Test Case 3
    s3 = "a"
    t3 = "aaaa"
    print(solution.findRotateSteps(s3, t3))  # Expected: 4

    # Test Case 4
    s4 = "pqrstuvwxyzabcdefghijklmno"
    t4 = "leetcode"
    print(solution.findRotateSteps(s4, t4))  # Expected: 63

    # Test Case 5
    s5 = "zjpc"
    t5 = "zjpc"
    print(solution.findRotateSteps(s5, t5))  # Expected: 7

test_find_rotate_steps()