from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ones = 0
        i = len(bits) - 2
        while i >= 0 and bits[i] == 1:
            ones += 1
            i -= 1
        return ones % 2 == 0

def test_is_one_bit_character():
    solution = Solution()

    # Test Case 1
    bits = [1, 0, 0]
    print(solution.isOneBitCharacter(bits))  # Expected: True

    # Test Case 2
    bits = [1, 1, 1, 0]
    print(solution.isOneBitCharacter(bits))  # Expected: False

    # Test Case 3: Single bit character
    bits = [0]
    print(solution.isOneBitCharacter(bits))  # Expected: True

    # Test Case 4: Two bit character followed by one bit
    bits = [1, 0, 1, 0]
    print(solution.isOneBitCharacter(bits))  # Expected: False

    # Test Case 5: Two bit character followed by two bits
    bits = [1, 1, 0, 0]
    print(solution.isOneBitCharacter(bits))  # Expected: True

    # Test Case 6: Multiple two bit characters ending with one bit
    bits = [1, 0, 1, 1, 0]
    print(solution.isOneBitCharacter(bits))  # Expected: True

    # Test Case 7: Long sequence with alternating bits
    bits = [1, 0] * 500 + [0]
    print(solution.isOneBitCharacter(bits))  # Expected: True

    # Test Case 8: Long sequence with multiple two bit characters
    bits = [1, 1, 0] * 333 + [1, 0]
    print(solution.isOneBitCharacter(bits))  # Expected: False

    # Test Case 9: Edge case with all ones
    bits = [1] * 1000 + [0]
    print(solution.isOneBitCharacter(bits))  # Expected: True

    # Test Case 10: Edge case with all zeros
    bits = [0] * 1001
    print(solution.isOneBitCharacter(bits))  # Expected: True

test_is_one_bit_character()