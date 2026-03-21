class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            s = s[::-1]
            x, y = y, x

        a_count, b_count, total_points = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "a":
                a_count += 1
            elif s[i] == "b":
                if a_count > 0:
                    a_count -= 1
                    total_points += x
                else:
                    b_count += 1
            else:
                total_points += min(b_count, a_count) * y
                a_count = b_count = 0

        total_points += min(b_count, a_count) * y
        return total_points

def test_maximum_gain():
    s = Solution()

    # Test Case 1
    str1 = "cdbcbbaaabab"
    x1 = 4
    y1 = 5
    print(s.maximumGain(str1, x1, y1)) # Expected Output: 19

    # Test Case 2
    str2 = "aabbaaxybbaabb"
    x2 = 5
    y2 = 4
    print(s.maximumGain(str2, x2, y2)) # Expected Output: 20

    # Test Case 3
    str3 = "ababa"
    x3 = 10
    y3 = 20
    print(s.maximumGain(str3, x3, y3)) # Expected Output: 30

    # Test Case 4
    str4 = "abcde"
    x4 = 1
    y4 = 1
    print(s.maximumGain(str4, x4, y4)) # Expected Output: 0

    # Test Case 5
    str5 = "aaabbb"
    x5 = 10
    y5 = 20
    print(s.maximumGain(str5, x5, y5)) # Expected Output: 50

test_maximum_gain()