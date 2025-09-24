class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

def test_palindrome_number():
    solution = Solution()

    # Test Case 1: Normal case with a palindrome number
    x = 121
    print(solution.isPalindrome(x))  # Expected output: True

    # Test Case 2: Normal case with a non-palindrome number
    x = -121
    print(solution.isPalindrome(x))  # Expected output: False

    # Test Case 3: Single digit number (always a palindrome)
    x = 7
    print(solution.isPalindrome(x))  # Expected output: True

    # Test Case 4: Number with trailing zeros (not a palindrome)
    x = 10
    print(solution.isPalindrome(x))  # Expected output: False

    # Test Case 5: Large palindrome number
    x = 1234321
    print(solution.isPalindrome(x))  # Expected output: True

    # Test Case 6: Large non-palindrome number
    x = 1234567
    print(solution.isPalindrome(x))  # Expected output: False

    # Test Case 7: Zero (edge case)
    x = 0
    print(solution.isPalindrome(x))  # Expected output: True

    # Test Case 8: Very large number
    x = 1234567890987654321
    print(solution.isPalindrome(x))  # Expected output: True

    # Test Case 9: Negative number with palindrome digits
    x = -12321
    print(solution.isPalindrome(x))  # Expected output: False

    # Test Case 10: Number with all identical digits
    x = 555
    print(solution.isPalindrome(x))  # Expected output: True

test_palindrome_number()