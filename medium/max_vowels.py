class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_counts = {}
        vowels = 'aeiou'

        curr_count = sum(1 for char in s[:k] if char in vowels)
        max_vowel_count = curr_count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                curr_count -= 1
            if s[i] in vowels:
                curr_count += 1

            if curr_count > max_vowel_count:
                max_vowel_count = curr_count
        return max_vowel_count

def test_max_vowels():
    solution = Solution()

    # Test case 1
    s = "abciiidef"
    k = 3
    print(solution.maxVowels(s, k))  # Expected output: 3

    # Test case 2
    s = "aeiou"
    k = 2
    print(solution.maxVowels(s, k))  # Expected output: 2

    # Test case 3
    s = "leetcode"
    k = 3
    print(solution.maxVowels(s, k))  # Expected output: 2

    # Test case 4
    s = "rhythms"
    k = 4
    print(solution.maxVowels(s, k))  # Expected output: 0

    # Test case 5
    s = "tryhard"
    k = 4
    print(solution.maxVowels(s, k))  # Expected output: 1

test_max_vowels()