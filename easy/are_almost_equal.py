class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        s1_frequency_map = [0] * 26
        s2_frequency_map = [0] * 26
        num_diffs = 0

        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]

            if s1_char != s2_char:
                num_diffs += 1
                if num_diffs > 2:
                    return False

            s1_frequency_map[ord(s1_char) - ord("a")] += 1
            s2_frequency_map[ord(s2_char) - ord("a")] += 1

        return s1_frequency_map == s2_frequency_map

def test_are_almost_equal():
    solution = Solution()

    # Test case 1
    s1_1 = "bank"
    s2_1 = "kanb"
    print(solution.areAlmostEqual(s1_1, s2_1))  # Expected output: True

    # Test case 2
    s1_2 = "attack"
    s2_2 = "defend"
    print(solution.areAlmostEqual(s1_2, s2_2))  # Expected output: False

    # Test case 3
    s1_3 = "kelb"
    s2_3 = "kelb"
    print(solution.areAlmostEqual(s1_3, s2_3))  # Expected output: True

    # Test case 4
    s1_4 = "abcd"
    s2_4 = "dcba"
    print(solution.areAlmostEqual(s1_4, s2_4))  # Expected output: False

    # Test case 5
    s1_5 = "abcde"
    s2_5 = "abced"
    print(solution.areAlmostEqual(s1_5, s2_5))  # Expected output: True

test_are_almost_equal()