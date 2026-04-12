class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
                
        if len(set(freq.values())) == 1:
            return True
        else:
            return False

def test_are_occurences_equal():
    solution = Solution()

    # Test Case 1
    s1 = "abacbc"
    print(solution.areOccurrencesEqual(s1))  # Expected output: True

    # Test Case 2
    s2 = "aaabb"
    print(solution.areOccurrencesEqual(s2))  # Expected output: False

    # Test Case 3
    s3 = "abseda"
    print(solution.areOccurrencesEqual(s3))  # Expected output: False

    # Test Case 4
    s4 = "aabbcc"
    print(solution.areOccurrencesEqual(s4))  # Expected output: True

    # Test Case 5
    s5 = "aabbccc"
    print(solution.areOccurrencesEqual(s5))  # Expected output: False

test_are_occurences_equal()