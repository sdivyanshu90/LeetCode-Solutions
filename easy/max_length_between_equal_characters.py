class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        length = -1
        hash = {}
        
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = i
            else:
                length = max(length , i- hash.get(s[i]) -1)
                
        return length

def test_max_length_between_equal_characters():
    solution = Solution()

    # Test case 1
    s = "aa"
    print(solution.maxLengthBetweenEqualCharacters(s))  # Expected output: 0

    # Test case 2
    s = "abca"
    print(solution.maxLengthBetweenEqualCharacters(s))  # Expected output: 2

    # Test case 3
    s = "cbzxy"
    print(solution.maxLengthBetweenEqualCharacters(s))  # Expected output: -1

    # Test case 4
    s = "cabbac"
    print(solution.maxLengthBetweenEqualCharacters(s))  # Expected output: 4

    # Test case 5
    s = "abcde"
    print(solution.maxLengthBetweenEqualCharacters(s))  # Expected output: -1

test_max_length_between_equal_characters()