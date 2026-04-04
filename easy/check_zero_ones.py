class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_ones = 0
        longest_zeros = 0
        current_char = None
        current_length = 0
        
        for char in s:
            if char == current_char:
                current_length += 1
            else:
                if current_char == '1':
                    longest_ones = max(longest_ones, current_length)
                elif current_char == '0':
                    longest_zeros = max(longest_zeros, current_length)
                
                current_char = char
                current_length = 1
        
        if current_char == '1':
            longest_ones = max(longest_ones, current_length)
        elif current_char == '0':
            longest_zeros = max(longest_zeros, current_length)
        
        if longest_ones > longest_zeros:
            return True
        else:
            return False

def test_check_zero_ones():
    solution = Solution()

    # Test case 1
    s1 = "1101"
    print(solution.checkZeroOnes(s1))  # Expected output: True

    # Test case 2
    s2 = "111000"
    print(solution.checkZeroOnes(s2))  # Expected output: False

    # Test case 3
    s3 = "110100010"
    print(solution.checkZeroOnes(s3))  # Expected output: False

    # Test case 4
    s4 = "10101"
    print(solution.checkZeroOnes(s4))  # Expected output: False

    # Test case 5
    s5 = "000111000"
    print(solution.checkZeroOnes(s5))  # Expected output: False

test_check_zero_ones()