class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = {}
        freq[0] = 1
        mask = 0
        res = 0
        for c in word:
            bit = ord(c) - 97
            mask ^= (1 << bit)
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1
            for odd_c in range(0, 10):
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]

        return res

def test_wonderful_substrings():
    solution = Solution()

    # Test case 1
    word = "aba"
    print(solution.wonderfulSubstrings(word))  # Expected output: 4

    # Test case 2
    word = "aabb"
    print(solution.wonderfulSubstrings(word))  # Expected output: 9

    # Test case 3
    word = "he"
    print(solution.wonderfulSubstrings(word))  # Expected output: 2

    # Test case 4
    word = "ihhih"
    print(solution.wonderfulSubstrings(word))  # Expected output: 6

    # Test case 5
    word = "jj"
    print(solution.wonderfulSubstrings(word))  # Expected output: 3

test_wonderful_substrings()