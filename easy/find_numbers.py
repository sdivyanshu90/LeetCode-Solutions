from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1

        return res

def test_find_numbers():
    solution = Solution()

    # Test case 1
    nums = [12,345,2,6,7896]
    print(solution.findNumbers(nums))  # Expected output: 2

    # Test case 2
    nums = [555,901,482,1771]
    print(solution.findNumbers(nums))  # Expected output: 1

    # Test case 3
    nums = [1,22,333,4444]
    print(solution.findNumbers(nums))  # Expected output: 2

    # Test case 4
    nums = [1234,56789,10]
    print(solution.findNumbers(nums))  # Expected output: 2

    # Test case 5
    nums = [0,11,222,3333]
    print(solution.findNumbers(nums))  # Expected output: 2

test_find_numbers()