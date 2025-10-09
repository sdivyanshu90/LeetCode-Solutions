from typing import List
from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+": 
                    stack.append(a + b)
                elif t == "-": 
                    stack.append(a - b)
                elif t == "*": 
                    stack.append(a * b)
                else: 
                    stack.append(trunc(a / b))
        return stack[0]

def test_eval_rpn():
    sol = Solution()

    # Test Case 1
    print(sol.evalRPN(["2", "1", "+", "3", "*"])) # Expected output: 9

    # Test Case 2
    print(sol.evalRPN(["4", "13", "5", "/", "+"])) # Expected output: 6

    # Test Case 3
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])) # Expected output: 22

    # Test Case 4
    print(sol.evalRPN(["3", "-4", "+"])) # Expected output: -1

    # Test Case 5
    print(sol.evalRPN(["4", "3", "-"])) # Expected output: 1

    # Test Case 6
    print(sol.evalRPN(["4", "-2", "/"])) # Expected output: -2

    # Test Case 7
    print(sol.evalRPN(["-1", "1", "-", "2", "*", "3", "+", "4", "-", "5", "*", "6", "/"])) # Expected output: -4

    # Test Case 8
    print(sol.evalRPN(["-4", "-2", "/"])) # Expected output: 2

    # Test Case 9
    print(sol.evalRPN(["0", "3", "/"])) # Expected output: 0

    # Test Case 10
    print(sol.evalRPN(["3", "100", "/"])) # Expected output: 0

test_eval_rpn()