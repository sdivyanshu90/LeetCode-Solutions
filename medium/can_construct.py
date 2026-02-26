class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        bitmask = 0
        
        for char in s:
            bit_index = ord(char) - ord('a')
            bitmask ^= (1 << bit_index)
            
        return bitmask.bit_count() <= k

def test_can_construct():
    solution = Solution()

    # Test case 1
    s1 = "annabelle"
    k1 = 2
    print(solution.canConstruct(s1, k1))  # Expected output: True

    # Test case 2
    s2 = "leetcode"
    k2 = 3
    print(solution.canConstruct(s2, k2))  # Expected output: False

    # Test case 3
    s3 = "true"
    k3 = 4
    print(solution.canConstruct(s3, k3))  # Expected output: True

    # Test case 4
    s4 = "yzyzyzyzyzyzyzy"
    k4 = 2
    print(solution.canConstruct(s4, k4))  # Expected output: True

    # Test case 5
    s5 = "cr"
    k5 = 7
    print(solution.canConstruct(s5, k5))  # Expected output: False

test_can_construct()