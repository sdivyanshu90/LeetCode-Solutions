class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, opened = [], 0
        for para in s:
            if para == "(" and opened > 0:
                res.append(para)
            if para == ")" and opened > 1:
                res.append(para)
            opened += 1 if para == "(" else -1 

        return "".join(res)

def test_remove_outer_parentheses():
    solution = Solution()

    # Test case 1
    s1 = "(()())(())"
    print(solution.removeOuterParentheses(s1))  # Expected output: "()()()"

    # Test case 2
    s2 = "(()())(())(()(()))"
    print(solution.removeOuterParentheses(s2))  # Expected output: "()()()()(())"

    # Test case 3
    s3 = "()()"
    print(solution.removeOuterParentheses(s3))  # Expected output: ""

    # Test case 4
    s4 = "((()))"
    print(solution.removeOuterParentheses(s4))  # Expected output: "(())"

    # Test case 5
    s5 = "((())())(()(()))"
    print(solution.removeOuterParentheses(s5))  # Expected output: "(())()()(())"

test_remove_outer_parentheses()