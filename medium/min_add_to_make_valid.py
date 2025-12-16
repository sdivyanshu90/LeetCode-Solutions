class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened = 0
        closed = 0

        for i in range(len(s)):
            if s[i] == "(":
                opened += 1
            else:
                if opened > 0:
                    opened -= 1
                else:
                    closed += 1

        return opened + closed

def test_min_add_to_make_valid():
    solution = Solution()

    # Test Case 1
    print(solution.minAddToMakeValid("())")) # Expected: 1

    # Test Case 2
    print(solution.minAddToMakeValid("(((")) # Expected: 3

    # Test Case 3
    print(solution.minAddToMakeValid("()")) # Expected: 0

    # Test Case 4
    print(solution.minAddToMakeValid("()))((")) # Expected: 4

    # Test Case 5
    print(solution.minAddToMakeValid(")(")) # Expected: 2

test_min_add_to_make_valid()