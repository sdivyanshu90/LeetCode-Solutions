from collections import deque

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = deque()

        for curr_char in expression:
            if curr_char == "," or curr_char == "(":
                curr_char

            if curr_char in ["t", "f", "!", "&", "|"]:
                st.append(curr_char)

            elif curr_char == ")":
                has_true = False
                has_false = False

                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True

                op = st.pop()
                if op == "!":
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    st.append("f" if has_false else "t")
                else:
                    st.append("t" if has_true else "f")

        return st[-1] == "t"

def test_parse_bool_expr():
    solution = Solution()

    # Test case 1
    expression = "!(f)"
    print(solution.parseBoolExpr(expression))  # Expected output: True

    # Test case 2
    expression = "|(f,t)"
    print(solution.parseBoolExpr(expression))  # Expected output: True

    # Test case 3
    expression = "&(t,f)"
    print(solution.parseBoolExpr(expression))  # Expected output: False

    # Test case 4
    expression = "|(&(t,f,t),!(t))"
    print(solution.parseBoolExpr(expression))  # Expected output: False

    # Test case 5
    expression = "&(|(f,t),!(f),&(t,t,f))"
    print(solution.parseBoolExpr(expression))  # Expected output: False

test_parse_bool_expr()