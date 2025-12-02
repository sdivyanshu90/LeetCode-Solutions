class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1
        
        for i in range(length + 1):
            if s[i] == '(' or s[i] == '*':
                open_count += 1
            else:
                open_count -= 1
            
            if s[length - i] == ')' or s[length - i] == '*':
                close_count += 1
            else:
                close_count -= 1
            
            if open_count < 0 or close_count < 0:
                return False
        
        return True

def test_check_valid_string():
    solution = Solution()

    # Test Case 1
    s1 = "(*))"
    print(solution.checkValidString(s1))  # Expected: True

    # Test Case 2
    s2 = "(*()"
    print(solution.checkValidString(s2))  # Expected: True

    # Test Case 3
    s3 = ")*("
    print(solution.checkValidString(s3))  # Expected: False

    # Test Case 4
    s4 = "((*)"
    print(solution.checkValidString(s4))  # Expected: True

    # Test Case 5
    s5 = "(((******))"
    print(solution.checkValidString(s5))  # Expected: True

test_check_valid_string()