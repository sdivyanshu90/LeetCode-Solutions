# Approach 1
# class Solution:
#     def diffWaysToCompute(self, expression: str) -> List[int]:
#         n = len(expression)
#         dp = [[[] for _ in range(n)] for _ in range(n)]

#         self._initialize_base_cases(expression, dp)

#         for length in range(3, n + 1):
#             for start in range(n - length + 1):
#                 end = start + length - 1
#                 self._process_subexpression(expression, dp, start, end)

#         return dp[0][n - 1]

#     def _initialize_base_cases(
#         self, expression: str, dp: List[List[List[int]]]
#     ):
#         for i, char in enumerate(expression):
#             if char.isdigit():
#                 dig1 = ord(char) - ord("0")
#                 if i + 1 < len(expression) and expression[i + 1].isdigit():
#                     dig2 = ord(expression[i + 1]) - ord("0")
#                     number = dig1 * 10 + dig2
#                     dp[i][i + 1].append(number)
#                 dp[i][i].append(dig1)

#     def _process_subexpression(
#         self, expression: str, dp: List[List[List[int]]], start: int, end: int
#     ):
#         for split in range(start, end + 1):
#             if expression[split].isdigit():
#                 continue

#             left_results = dp[start][split - 1]
#             right_results = dp[split + 1][end]

#             self._compute_results(
#                 expression[split], left_results, right_results, dp[start][end]
#             )

#     def _compute_results(
#         self,
#         op: str,
#         left_results: List[int],
#         right_results: List[int],
#         results: List[int],
#     ):
#         for left_value in left_results:
#             for right_value in right_results:
#                 if op == "+":
#                     results.append(left_value + right_value)
#                 elif op == "-":
#                     results.append(left_value - right_value)
#                 elif op == "*":
#                     results.append(left_value * right_value)

# Approach 2
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}

        def compute(sub_expression: str) -> List[int]:
            if sub_expression in memo:
                return memo[sub_expression]
            
            if sub_expression.isdigit():
                return [int(sub_expression)]
            
            results = []
            for i, char in enumerate(sub_expression):
                if char in "+-*":
                    left_parts = compute(sub_expression[:i])
                    right_parts = compute(sub_expression[i+1:])
                    
                    for l in left_parts:
                        for r in right_parts:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)
            
            memo[sub_expression] = results
            return results

        return compute(expression)

def test_diff_ways_to_compute():
    s = Solution()

    # Test Case 1: Standard example from LeetCode
    expression = "2-1-1"
    # (2-1)-1 = 0
    # 2-(1-1) = 2
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [0, 2]

    # Test Case 2: More complex example
    expression = "2*3-4*5"
    # (2*3)-(4*5) = -14
    # 2*(3-(4*5)) = -34
    # ((2*3)-4)*5 = 10
    # 2*((3-4)*5) = -10
    # (2*(3-4))*5 = -10
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [-34, -14, -10, -10, 10]

    # Test Case 3: Expression with only one multi-digit number
    expression = "15"
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [15]

    # Test Case 4: Simple expression with multi-digit numbers
    expression = "10+5"
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [15]

    # Test Case 5: Mix of operators
    expression = "3*5+2"
    # (3*5)+2 = 17
    # 3*(5+2) = 21
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [17, 21]

    # Test Case 6: Expression with only one operator
    expression = "15-7*2"
    # (15-7)*2 = 16
    # 15-(7*2) = 1
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [1, 16]

    # Test Case 7: Expression is a single zero
    expression = "0"
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [0]

    # Test Case 8: Longer expression
    expression = "1+2*3-4"
    # ((1+2)*3)-4 = 5
    # (1+2)*(3-4) = -3
    # 1+((2*3)-4) = 3
    # 1+(2*(3-4)) = -1
    # (1+(2*3))-4 = 3
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [-3, -1, 3, 3, 5]

    # Test Case 9: Expression resulting in negative values
    expression = "1-10*2"
    # (1-10)*2 = -18
    # 1-(10*2) = -19
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [-19, -18]
    
    # Test Case 10: Expression where all groupings yield the same result
    expression = "5*2*3"
    # (5*2)*3 = 30
    # 5*(2*3) = 30
    print(f"\nInput: '{expression}'")
    print(f"Output: {sorted(s.diffWaysToCompute(expression))}") # Expected: [30, 30]

test_diff_ways_to_compute()