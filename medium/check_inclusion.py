from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ln = len(s1)
        mp1 = Counter(s1)
        for i in range(len(s2) - ln + 1):
            sb = s2[i:i+ln]
            if mp1 == Counter(sb):
                return True
        return False

def test_check_inclusion():
    s = Solution()

    # Test case 1
    s1_1 = "ab"
    s2_1 = "eidbaooo"
    print(s.checkInclusion(s1_1, s2_1)) # Expected output: True

    # Test case 2
    s1_2 = "ab"
    s2_2 = "eidboaoo"
    print(s.checkInclusion(s1_2, s2_2)) # Expected output: False

    # Test case 3
    s1_3 = "adc"
    s2_3 = "dcda"
    print(s.checkInclusion(s1_3, s2_3)) # Expected output: True

    # Test case 4
    s1_4 = "hello"
    s2_4 = "ooolleoooleh"
    print(s.checkInclusion(s1_4, s2_4)) # Expected output: False

    # Test case 5
    s1_5 = "a"
    s2_5 = "a"
    print(s.checkInclusion(s1_5, s2_5)) # Expected output: True

test_check_inclusion()