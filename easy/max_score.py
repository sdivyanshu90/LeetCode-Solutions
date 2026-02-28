class Solution:
  def maxScore(self, s: str) -> int:
    ans = 0
    zeros = 0
    ones = s.count('1')

    for i in range(len(s) - 1):
      if s[i] == '0':
        zeros += 1
      else:
        ones -= 1
      ans = max(ans, zeros + ones)

    return ans

def test_max_score():
    solution = Solution()

    # Test case 1
    s1 = "011101"
    print(solution.maxScore(s1))  # Expected output: 5

    # Test case 2
    s2 = "00111"
    print(solution.maxScore(s2))  # Expected output: 5

    # Test case 3
    s3 = "1111"
    print(solution.maxScore(s3))  # Expected output: 3

    # Test case 4
    s4 = "0000"
    print(solution.maxScore(s4))  # Expected output: 3

    # Test case 5
    s5 = "101010"
    print(solution.maxScore(s5))  # Expected output: 5

test_max_score()