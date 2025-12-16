class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        
        return i == len(name)

def test_is_long_pressed_name():
    solution = Solution()

    # Test Case 1
    print(solution.isLongPressedName("alex", "aaleex")) # Expected: True

    # Test Case 2
    print(solution.isLongPressedName("saeed", "ssaaedd")) # Expected: False

    # Test Case 3
    print(solution.isLongPressedName("leelee", "lleeelee")) # Expected: True

    # Test Case 4
    print(solution.isLongPressedName("laiden", "laiden")) # Expected: True

    # Test Case 5
    print(solution.isLongPressedName("pyplrz", "ppyypllr")) # Expected: False

test_is_long_pressed_name()