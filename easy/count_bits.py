from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits_count = [0] * (n + 1)
        
        for i in range(1, n + 1):
            bits_count[i] = bits_count[i // 2] + (i % 2)
        
        return bits_count

def test_count_bits():
    s = Solution()

    # Test Case 1: Example with n = 2
    n = 2
    print(s.countBits(n))  # Expected: [0, 1, 1]

    # Test Case 2: Example with n = 5
    n = 5
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2]

    # Test Case 3: Edge case with n = 0
    n = 0
    print(s.countBits(n))  # Expected: [0]

    # Test Case 4: Larger n
    n = 10
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]

    # Test Case 5: n = 15
    n = 15
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

    # Test Case 6: n = 20
    n = 20
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2]

    # Test Case 7: n = 1
    n = 1
    print(s.countBits(n))  # Expected: [0, 1]

    # Test Case 8: n = 8
    n = 8
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1]

    # Test Case 9: n = 16
    n = 16
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1]

    # Test Case 10: n = 25
    n = 25
    print(s.countBits(n))  # Expected: [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3]

test_count_bits()