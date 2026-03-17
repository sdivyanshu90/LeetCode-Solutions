class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
      return False

    count1 = collections.Counter(word1)
    count2 = collections.Counter(word2)
    if count1.keys() != count2.keys():
      return False

    return sorted(count1.values()) == sorted(count2.values())

def test_close_strings():
    solution = Solution()

    # Test case 1
    word1_1 = "abc"
    word2_1 = "bca"
    print(solution.closeStrings(word1_1, word2_1))  # Expected output: True

    # Test case 2
    word1_2 = "a"
    word2_2 = "aa"
    print(solution.closeStrings(word1_2, word2_2))  # Expected output: False

    # Test case 3
    word1_3 = "cabbba"
    word2_3 = "abbccc"
    print(solution.closeStrings(word1_3, word2_3))  # Expected output: True

    # Test case 4
    word1_4 = "cabbba"
    word2_4 = "aabbss"
    print(solution.closeStrings(word1_4, word2_4))  # Expected output: False

    # Test case 5
    word1_5 = "uau"
    word2_5 = "ssx"
    print(solution.closeStrings(word1_5, word2_5))  # Expected output: False

test_close_strings()