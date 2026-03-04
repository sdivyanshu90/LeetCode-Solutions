class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_array = sorted(arr)
        
        common_diff = sorted_array[1] - sorted_array[0]
        
        for i in range(1, len(sorted_array)):
            if sorted_array[i] - sorted_array[i - 1] != common_diff:
                return False
        
        return True

def test_can_make_arithmetic_progression():
    solution = Solution()

    # Test Case 1
    arr1 = [3, 5, 1]
    print(solution.canMakeArithmeticProgression(arr1))  # Expected output: True

    # Test Case 2
    arr2 = [1, 2, 4]
    print(solution.canMakeArithmeticProgression(arr2))  # Expected output: False

    # Test Case 3
    arr3 = [7, 3, 5]
    print(solution.canMakeArithmeticProgression(arr3))  # Expected output: True

    # Test Case 4
    arr4 = [1, 3, 5, 7]
    print(solution.canMakeArithmeticProgression(arr4))  # Expected output: True

    # Test Case 5
    arr5 = [1, 2, 3, 5]
    print(solution.canMakeArithmeticProgression(arr5))  # Expected output: False

test_can_make_arithmetic_progression()