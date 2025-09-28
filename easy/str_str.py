class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return  -1

def test_str_str():
    solution = Solution()

    # Test case 1: Basic case
    haystack1 = "hello"
    needle1 = "ll"
    result1 = solution.strStr(haystack1, needle1)
    print(result1)  # Expected output: 2

    # Test case 2: Needle not in haystack
    haystack2 = "aaaaa"
    needle2 = "bba"
    result2 = solution.strStr(haystack2, needle2)
    print(result2)  # Expected output: -1

    # Test case 3: Needle is empty string
    haystack3 = "abc"
    needle3 = ""
    result3 = solution.strStr(haystack3, needle3)
    print(result3)  # Expected output: 0

    # Test case 4: Haystack and needle are the same
    haystack4 = "test"
    needle4 = "test"
    result4 = solution.strStr(haystack4, needle4)
    print(result4)  # Expected output: 0

    # Test case 5: Needle at the end of haystack
    haystack5 = "abcdef"
    needle5 = "def"
    result5 = solution.strStr(haystack5, needle5)
    print(result5)  # Expected output: 3

    # Test case 6: Needle at the beginning of haystack
    haystack6 = "abcdef"
    needle6 = "abc"
    result6 = solution.strStr(haystack6, needle6)
    print(result6)  # Expected output: 0

    # Test case 7: Needle longer than haystack
    haystack7 = "short"
    needle7 = "longerneedle"
    result7 = solution.strStr(haystack7, needle7)
    print(result7)  # Expected output: -1

    # Test case 8: Multiple occurrences of needle in haystack
    haystack8 = "ababcabc"
    needle8 = "abc"
    result8 = solution.strStr(haystack8, needle8)
    print(result8)  # Expected output: 2

    # Test case 9: Special characters in haystack and needle
    haystack9 = "a!b@c#d$e%"
    needle9 = "@c#d"
    result9 = solution.strStr(haystack9, needle9)
    print(result9)  # Expected output: 3

    # Test case 10: Case sensitivity
    haystack10 = "CaseSensitive"
    needle10 = "casesensitive"
    result10 = solution.strStr(haystack10, needle10)
    print(result10)  # Expected output: -1

test_str_str()