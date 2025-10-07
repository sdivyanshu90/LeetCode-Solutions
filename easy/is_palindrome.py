# Approach 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(filter(str.isalnum, s)).lower()
        if new_s == new_s[::-1]:
            return True
        return False

# Approach 2
# import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
#         left, right = 0, len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 return False    
#             left += 1
#             right -= 1
#         return True

def test_is_palindrome():
    solution = Solution()
    
    # Test case 1
    s = "A man, a plan, a canal: Panama"
    print(solution.isPalindrome(s))  # Expected output: True

    # Test case 2
    s = "race a car"
    print(solution.isPalindrome(s))  # Expected output: False

    # Test case 3
    s = " "
    print(solution.isPalindrome(s))  # Expected output: True

    # Test case 4
    s = "A Toyota's a Toyota"
    print(solution.isPalindrome(s))  # Expected output: True

    # Test case 5
    s = "No 'x' in Nixon"
    print(solution.isPalindrome(s))  # Expected output: True

test_is_palindrome()