class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


def test_remove_duplicates():
    solution = Solution()

    # Test case 1
    s = "abbaca"
    print(solution.removeDuplicates(s))  # Expected output: "ca"

    # Test case 2
    s = "azxxzy"
    print(solution.removeDuplicates(s))  # Expected output: "ay"

    # Test case 3
    s = "a"
    print(solution.removeDuplicates(s))  # Expected output: "a"

    # Test case 4
    s = "aa"
    print(solution.removeDuplicates(s))  # Expected output: ""

    # Test case 5
    s = "abccba"
    print(solution.removeDuplicates(s))  # Expected output: ""

test_remove_duplicates()