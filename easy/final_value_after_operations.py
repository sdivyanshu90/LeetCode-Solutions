class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if "+" in op else -1 for op in operations)

def test_final_value_after_operations():
    solution = Solution()

    # Test case 1
    operations1 = ["--X", "X++", "X++"]
    print(solution.finalValueAfterOperations(operations1))  # Expected output: 1

    # Test case 2
    operations2 = ["++X", "++X", "X++"]
    print(solution.finalValueAfterOperations(operations2))  # Expected output: 3

    # Test case 3
    operations3 = ["X++", "++X", "--X", "X--"]
    print(solution.finalValueAfterOperations(operations3))  # Expected output: 0

    # Test case 4
    operations4 = ["X++", "X++", "X++", "X--", "X--", "X--"]
    print(solution.finalValueAfterOperations(operations4))  # Expected Output: 1

    # Test case 5
    operations5 = ["++X", "++X", "++X", "--X", "--X", "--X", "++X"]
    print(solution.finalValueAfterOperations(operations5))  # Expected Output: 2

test_final_value_after_operations()