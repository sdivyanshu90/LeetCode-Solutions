from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(int(stack[-1])*2)
            elif i == '+':
                stack.append(stack[-2]+stack[-1])
            else:
                stack.append(int(i))
        return sum(stack)

def test_cal_points():
    solution = Solution()

    # Test Case 1
    ops1 = ["5","2","C","D","+"]
    print(solution.calPoints(ops1))  # Expected: 30

    # Test Case 2
    ops2 = ["5","-2","4","C","D","9","+","+"]
    print(solution.calPoints(ops2))  # Expected: 27

    # Test Case 3
    ops3 = ["1"]
    print(solution.calPoints(ops3))  # Expected: 1

    # Test Case 4
    ops4 = ["10","20","30","D","+"]
    print(solution.calPoints(ops4))  # Expected: 210

    # Test Case 5
    ops5 = ["-5","-10","D","+","C"]
    print(solution.calPoints(ops5))  # Expected: -15

test_cal_points()