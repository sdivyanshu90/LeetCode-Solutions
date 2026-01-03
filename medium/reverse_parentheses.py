class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction

        return "".join(result)

def test_reverse_parentheses():
    solution = Solution()

    # Test Case 1
    s = "(abcd)"
    print(solution.reverseParentheses(s)) # Expected Output: "dcba"

    # Test Case 2
    s = "(u(love)i)"
    print(solution.reverseParentheses(s)) # Expected Output: "iloveu"

    # Test Case 3
    s = "(ed(et(oc))el)"
    print(solution.reverseParentheses(s)) # Expected Output: "leetcode"

    # Test Case 4
    s = "a(bcdefghijkl(mno)p)q"
    print(solution.reverseParentheses(s)) # Expected Output: "apmnolkjihgfedcbq"

    # Test Case 5
    s = "((a(bc)d)e)"
    print(solution.reverseParentheses(s)) # Expected Output: "edcb a"

test_reverse_parentheses()