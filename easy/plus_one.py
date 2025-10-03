from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] <= 8:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits

def test_plus_one():
    solution = Solution()
    # Test Case 1
    print(solution.plusOne([1,2,3]))  # Expected output: [1,2,4]
    # Test Case 2
    print(solution.plusOne([4,3,2,1]))  # Expected output: [4,3,2,2]
    # Test Case 3
    print(solution.plusOne([0]))  # Expected output: [1]
    # Test Case 4
    print(solution.plusOne([9]))  # Expected output: [1,0]
    # Test Case 5
    print(solution.plusOne([9,9,9]))  # Expected output: [1,0,0,0]
    # Test Case 6
    print(solution.plusOne([1,9,9]))  # Expected output: [2,0,0]
    # Test Case 7
    print(solution.plusOne([2,9,9]))  # Expected output: [3,0,0]
    # Test Case 8
    print(solution.plusOne([1,2,9]))  # Expected output: [1,3,0]
    # Test Case 9
    print(solution.plusOne([1,2,8]))  # Expected output: [1,2,9]
    # Test Case 10
    print(solution.plusOne([9,8,7,6,5,4,3,2,1,0]))  # Expected output: [9,8,7,6,5,4,3,2,1,1]

test_plus_one()