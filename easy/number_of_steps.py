class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                highest_power_of_2 = (num & -num).bit_length() - 1
                num >>= highest_power_of_2
                count += highest_power_of_2
            else:
                num -= 1
                count += 1
        return (count)

def test_number_Of_Steps():
    solution = Solution()

    # Test case 1
    num = 14
    expected = 6
    print(solution.numberOfSteps(num))  # Expected Output: 6

    # Test case 2
    num = 8
    expected = 4
    print(solution.numberOfSteps(num))  # Expected Output: 4

    # Test case 3
    num = 123
    expected = 12
    print(solution.numberOfSteps(num))  # Expected Output: 12

    # Test case 4
    num = 0
    expected = 0
    print(solution.numberOfSteps(num))  # Expected Output: 0

    # Test case 5
    num = 1
    expected = 1
    print(solution.numberOfSteps(num))  # Expected Output: 1

test_number_Of_Steps()