class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        candidate = sorted(
            [c for c, w in Counter(s).items() if w >= k], reverse=True
        )
        q = deque(candidate)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr

            for ch in candidate:
                nxt = curr + ch
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return ans

def test_longest_subsequence_repeated_k():
    solution = Solution()

    # Test case 1
    s1 = "letsleetcode"
    k1 = 2
    print(solution.longestSubsequenceRepeatedK(s1, k1))  # Expected output: "let"

    # Test case 2
    s2 = "bb"
    k2 = 2
    print(solution.longestSubsequenceRepeatedK(s2, k2))  # Expected output: "b"

    # Test case 3
    s3 = "ababc"
    k3 = 2
    print(solution.longestSubsequenceRepeatedK(s3, k3))  # Expected output: "ab"

    # Test case 4
    s4 = "aaaaa"
    k4 = 3
    print(solution.longestSubsequenceRepeatedK(s4, k4))  # Expected output: "aaa"

    # Test case 5
    s5 = "abcde"
    k5 = 2
    print(solution.longestSubsequenceRepeatedK(s5, k5))  # Expected output: "" (empty string)

test_longest_subsequence_repeated_k()