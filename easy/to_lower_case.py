class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

def test_to_lower_case():
    solution = Solution()

    # Test Case 1
    input_str = "Hello"
    print(solution.toLowerCase(input_str)) # Expected: "hello"

    # Test Case 2
    input_str = "here"
    print(solution.toLowerCase(input_str)) # Expected: "here"

    # Test Case 3
    input_str = "LOVELY"
    print(solution.toLowerCase(input_str)) # Expected: "lovely"

    # Test Case 4: Mixed case with special characters
    input_str = "TeSt123!@#"
    print(solution.toLowerCase(input_str)) # Expected: "test123!@#"

    # Test Case 5: Empty string
    input_str = ""
    print(solution.toLowerCase(input_str)) # Expected: ""

test_to_lower_case()