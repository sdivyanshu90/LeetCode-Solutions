from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = second_max = third_max = float('-inf')
        distinct_count = 0

        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
                distinct_count += 1
            elif num < first_max and num > second_max:
                third_max = second_max
                second_max = num
                distinct_count += 1
            elif num < second_max and num > third_max:
                third_max = num
                distinct_count += 1

        if distinct_count >= 3:
            return third_max
        else:
            return first_max

def test_third_max():
    s = Solution()

    # Test case 1
    print(s.thirdMax([3, 2, 1]))  # Expected output: 1

    # Test case 2
    print(s.thirdMax([1, 2]))     # Expected output: 2

    # Test case 3
    print(s.thirdMax([2, 2, 3, 1])) # Expected output: 1

    # Test case 4
    print(s.thirdMax([1, 2, -2147483648])) # Expected output: -2147483648

    # Test case 5
    print(s.thirdMax([1,1,2]))    # Expected output: 2

    # Test case 6
    print(s.thirdMax([5,2,2]))    # Expected output: 5

    # Test case 7
    print(s.thirdMax([1,2,-2147483648])) # Expected output: -2147483648

    # Test case 8
    print(s.thirdMax([1,2,3,4,5])) # Expected output: 3

    # Test case 9
    print(s.thirdMax([2,2,3,3,1,1])) # Expected output: 1

    # Test case 10
    print(s.thirdMax([1,2,2,5,3,5])) # Expected output: 2

test_third_max()