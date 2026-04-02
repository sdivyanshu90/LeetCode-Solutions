class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char, i = coordinates[0], int(coordinates[1])
        if i % 2 == 0:
            if char in ["b", "d", "f", "h"]:
                return False
            else:
                return True
        else:
            if char in ["a", "c", "e", "g"]:
                return False
            else:
                return True

def test_square_is_white():
    solution = Solution()

    # Test Case 1
    coordinates1 = "a1"
    print(solution.squareIsWhite(coordinates1))  # Expected Output: False

    # Test Case 2
    coordinates2 = "h3"
    print(solution.squareIsWhite(coordinates2))  # Expected Output: True

    # Test Case 3
    coordinates3 = "c7"
    print(solution.squareIsWhite(coordinates3))  # Expected Output: False

    # Test Case 4
    coordinates4 = "d4"
    print(solution.squareIsWhite(coordinates4))  # Expected Output: False

    # Test Case 5
    coordinates5 = "e5"
    print(solution.squareIsWhite(coordinates5))  # Expected Output: False

test_square_is_white()