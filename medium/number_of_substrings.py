class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            last_pos[ord(s[pos]) - ord("a")] = pos
            total += 1 + min(last_pos)

        return total

def test_numberOfSubstrings():
    solution = Solution()

    # Test case 1
    s1 = "abcabc"
    print(solution.numberOfSubstrings(s1)) # Expected output: 10

    # Test case 2
    s2 = "aaacb"
    print(solution.numberOfSubstrings(s2)) # Expected output: 3

    # Test case 3
    s3 = "abc"
    print(solution.numberOfSubstrings(s3)) # Expected output: 1

    # Test case 4
    s4 = "aaaaa"
    print(solution.numberOfSubstrings(s4)) # Expected output: 0

    # Test case 5
    s5 = "abccba"
    print(solution.numberOfSubstrings(s5)) # Expected output: 7

test_numberOfSubstrings()