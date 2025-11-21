from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(2, n):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count

def test_triangle_number():
    s = Solution()

    # Test case 1
    nums = [2, 2, 3, 4]
    print(s.triangleNumber(nums))  # Expected output: 3

    # Test case 2
    nums = [4, 2, 3, 4]
    print(s.triangleNumber(nums))  # Expected output: 4

    # Test case 3
    nums = [1, 1, 1, 1]
    print(s.triangleNumber(nums))  # Expected output: 4

    # Test case 4
    nums = [0, 1, 1, 1]
    print(s.triangleNumber(nums))  # Expected output: 1

    # Test case 5
    nums = [3, 6, 2, 7]
    print(s.triangleNumber(nums))  # Expected output: 2

test_triangle_number()