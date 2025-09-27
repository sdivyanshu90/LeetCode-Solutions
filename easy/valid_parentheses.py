class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

def test_is_valid():
    sol = Solution()

    # Test case 1
    s = "()"
    print(sol.isValid(s))  # Expected output: True

    # Test case 2
    s = "()[]{}"
    print(sol.isValid(s))  # Expected output: True

    # Test case 3
    s = "(]"
    print(sol.isValid(s))  # Expected output: False

    # Test case 4
    s = "([)]"
    print(sol.isValid(s))  # Expected output: False

    # Test case 5
    s = "{[]}"
    print(sol.isValid(s))  # Expected output: True

    # Test case 6
    s = ""
    print(sol.isValid(s))  # Expected output: True

    # Test case 7
    s = "((()))"
    print(sol.isValid(s))  # Expected output: True

    # Test case 8
    s = "((())"
    print(sol.isValid(s))  # Expected output: False

    # Test case 9
    s = "())"
    print(sol.isValid(s))  # Expected output: False

    # Test case 10
    s = "([{}])"
    print(sol.isValid(s))  # Expected output: True

test_is_valid()