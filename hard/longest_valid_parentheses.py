# Approach 1: Two Pass Scan

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right >= left:
                left, right = 0, 0
        
        left, right = 0, 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left >= right:
                left, right = 0, 0
        
        return max_length

# Approach 2: Stack
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         stack = [-1]
#         ans = 0
#         for i, ch in enumerate(s):
#             if ch == '(':
#                 stack.append(i)
#             else:
#                 stack.pop()
#                 if not stack:
#                     stack.append(i)
#                 else:
#                     ans = max(ans, i - stack[-1])
#         return ans

def test_longest_valid_parentheses():
    solution = Solution()

    # Test case 1: Basic case
    s1 = "(()"
    result1 = solution.longestValidParentheses(s1)
    print(result1)  # Expected output: 2

    # Test case 2: Nested parentheses
    s2 = ")()())"
    result2 = solution.longestValidParentheses(s2)
    print(result2)  # Expected output: 4

    # Test case 3: All valid parentheses
    s3 = "()()"
    result3 = solution.longestValidParentheses(s3)
    print(result3)  # Expected output: 4

    # Test case 4: No valid parentheses
    s4 = "(((("
    result4 = solution.longestValidParentheses(s4)
    print(result4)  # Expected output: 0

    # Test case 5: Mixed valid and invalid parentheses
    s5 = "(()())"
    result5 = solution.longestValidParentheses(s5)
    print(result5)  # Expected output: 6

    # Test case 6: Empty string
    s6 = ""
    result6 = solution.longestValidParentheses(s6)
    print(result6)  # Expected output: 0

    # Test case 7: Single character (invalid)
    s7 = "("
    result7 = solution.longestValidParentheses(s7)
    print(result7)  # Expected output: 0

    # Test case 8: Single character (invalid)
    s8 = ")"
    result8 = solution.longestValidParentheses(s8)
    print(result8)  # Expected output: 0

    # Test case 9: Long string with multiple valid segments
    s9 = "(()))())("
    result9 = solution.longestValidParentheses(s9)
    print(result9)  # Expected output: 4

    # Test case 10: Long string with all valid parentheses
    s10 = "((()))()()"
    result10 = solution.longestValidParentheses(s10)
    print(result10)  # Expected output: 10

test_longest_valid_parentheses()