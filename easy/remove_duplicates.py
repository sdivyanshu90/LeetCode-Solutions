from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[i] = nums[n]
                i += 1
        return i

def test_remove_duplicates():
    sol = Solution()

    # Test case 1
    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 2, [1, 2]

    # Test case 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 5, [0, 1, 2, 3, 4]

    # Test case 3
    nums = []
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 0, []

    # Test case 4
    nums = [1]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 1, [1]

    # Test case 5
    nums = [1,2,3]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 3, [1, 2, 3]

    # Test case 6
    nums = [1,1,1,1,1]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 1, [1]

    # Test case 7
    nums = [1,2,2,3,3,4,4,5,5]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 5, [1, 2, 3, 4, 5]

    # Test case 8
    nums = [1,1,2,2,3,3,4,4,5,5,6,6]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 6, [1, 2, 3, 4, 5, 6]

    # Test case 9
    nums = [1,1,1,2,2,3,3,4,4,5,5]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 5, [1, 2, 3, 4, 5]

    # Test case 10
    nums = [1,2,3,4,5,6,7,8,9,10]
    k = sol.removeDuplicates(nums)
    print(k, nums[:k])  # Expected output: 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test_remove_duplicates()