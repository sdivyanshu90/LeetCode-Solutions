from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        result = []
        for c in s:
            if c == '(':
                stack.append(len(result))
                result.append(c)
            elif c == ')':
                if stack:
                    stack.pop()
                    result.append(c)
            else:
                result.append(c)
        
        for i in stack:
            result[i] = ''
        
        return ''.join(result)

def test_min_remove_to_make_valid():
    solution = Solution()

    # Test case 1
    s = "lee(t(c)o)de)"
    print(solution.minRemoveToMakeValid(s))  # Expected output: "lee(t(c)o)de"

    # Test case 2
    s = "a)b(c)d"
    print(solution.minRemoveToMakeValid(s))  # Expected output: "ab(c)d"

    # Test case 3
    s = "))(("
    print(solution.minRemoveToMakeValid(s))  # Expected output: ""

    # Test case 4
    s = "(a(b(c)d)"
    print(solution.minRemoveToMakeValid(s))  # Expected output: "a(b(c)d)"

    # Test case 5
    s = "abcde"
    print(solution.minRemoveToMakeValid(s))  # Expected output: "abcde"

test_min_remove_to_make_valid()