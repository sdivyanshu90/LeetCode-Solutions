class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # a = s.split(" ")
        return " ".join(s.split(" ")[:k])

def test_truncate_sentence():
    solution = Solution()

    # Test Case 1
    s1 = "Hello how are you Contestant"
    k1 = 4
    print(solution.truncateSentence(s1, k1))  # Expected Output: "Hello how are you"

    # Test Case 2
    s2 = "What is the solution to this problem"
    k2 = 4
    print(solution.truncateSentence(s2, k2))  # Expected Output: "What is the solution"

    # Test Case 3
    s3 = "chopper is not a tanuki"
    k3 = 5
    print(solution.truncateSentence(s3, k3))  # Expected Output: "chopper is not a tanuki"

    # Test Case 4
    s4 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    k4 = 10
    print(solution.truncateSentence(s4, k4))  # Expected Output: "a b c d e f g h i j"

    # Test Case 5
    s5 = "The quick brown fox jumps over the lazy dog"
    k5 = 9
    print(solution.truncateSentence(s5, k5))  # Expected Output: "The quick brown fox jumps over the lazy"

test_truncate_sentence()