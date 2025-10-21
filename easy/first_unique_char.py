class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}

        for char in s:
            hash[char] = hash.get(char, 0) + 1

        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i
        return -1

def test_first_unique_char():
    solution = Solution()
    
    # Test case 1
    print(solution.firstUniqChar("leetcode")) # Expected output: 0
    
    # Test case 2
    print(solution.firstUniqChar("loveleetcode")) # Expected output: 2

    # Test case 3: Edge case - all characters repeating
    print(solution.firstUniqChar("aabbcc")) # Expected output: -1

    # Test case 4: Single character string
    print(solution.firstUniqChar("z")) # Expected output: 0
    
    # Test case 5: First unique character at the end
    print(solution.firstUniqChar("aabbc")) # Expected output: 4

    # Test case 6: Empty string
    print(solution.firstUniqChar("")) # Expected output: -1

    # Test case 7: Unique character in the middle
    print(solution.firstUniqChar("swiss")) # Expected output: 1

    # Test case 8: All unique characters
    print(solution.firstUniqChar("abcdef")) # Expected output: 0

    # Test case 9: Large input with unique character at the start
    large_input = "a" + "b" * 10000 + "c" * 10000
    print(solution.firstUniqChar(large_input)) # Expected output: 0

    # Test case 10: Large input with unique character at the end
    large_input_end = "b" * 10000 + "c" * 10000 + "d"
    print(solution.firstUniqChar(large_input_end)) # Expected output: 20000

test_first_unique_char()