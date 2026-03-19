class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_chars = set(allowed)
        consistent_count = 0

        for word in words:
            if all(char in allowed_chars for char in word):
                consistent_count += 1

        return consistent_count

def test_count_consistent_strings():
    solution = Solution()

    # Test case 1
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(solution.countConsistentStrings(allowed, words))  # Expected output: 2

    # Test case 2
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    print(solution.countConsistentStrings(allowed, words))  # Expected output: 7

    # Test case 3
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    print(solution.countConsistentStrings(allowed, words))  # Expected output: 4

    # Test case 4
    allowed = "xyz"
    words = ["x", "y", "z", "xy", "xz", "yz", "xyz"]
    print(solution.countConsistentStrings(allowed, words))  # Expected output: 7

    # Test case 5
    allowed = ""
    words = ["a", "b", "c"]
    print(solution.countConsistentStrings(allowed, words))  # Expected output: 0

test_count_consistent_strings()