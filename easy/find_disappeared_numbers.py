from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                res.append(i)

        return res


def test_find_disappeared_numbers():
    s = Solution()

    # Test case 1
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(nums))  # Expected output: [5, 6]

    # Test case 2
    nums = [1,1]
    print(s.findDisappearedNumbers(nums))  # Expected output: [2]

    # Test case 3
    nums = [2,2]
    print(s.findDisappearedNumbers(nums))  # Expected output: [1]

    # Test case 4
    nums = [1,2,3,4,5]
    print(s.findDisappearedNumbers(nums))  # Expected output: []

    # Test case 5
    nums = [5,4,3,2,1]
    print(s.findDisappearedNumbers(nums))  # Expected output: []

test_find_disappeared_numbers()