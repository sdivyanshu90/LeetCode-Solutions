class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        s_list = list(s)
        j = 2

        for i in range(2, len(s)):
            if s_list[i] != s_list[j - 1] or s_list[i] != s_list[j - 2]:
                s_list[j] = s_list[i]
                j += 1

        return "".join(s_list[:j])

def test_make_fancy_string():
    solution = Solution()

    # Test Case 1
    s1 = "leeetcode"
    print(solution.makeFancyString(s1))  # Expected output: "leetcode"

    # Test Case 2
    s2 = "aaabaaaa"
    print(solution.makeFancyString(s2))  # Expected output: "aba"

    # Test Case 3
    s3 = "aab"
    print(solution.makeFancyString(s3))  # Expected output: "aab"

    # Test Case 4
    s4 = "aaaaa"
    print(solution.makeFancyString(s4))  # Expected output: "a"

    # Test Case 5
    s5 = "abc"
    print(solution.makeFancyString(s5))  # Expected output: "abc"

test_make_fancy_string()