class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for i in nums:
            mul *= i
        if mul > 0:
            return 1
        elif mul == 0:
            return 0
        else:
            return -1

def test_array_sign():
    solution = Solution()

    # Test Case 1
    nums1 = [-1,-2,-3]
    print(solution.arraySign(nums1))  # Expected Output: -1

    # Test Case 2
    nums2 = [1,5,0,2,-3]
    print(solution.arraySign(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [-1,1,-1,1,-1]
    print(solution.arraySign(nums3))  # Expected Output: -1

    # Test Case 4
    nums4 = [1,2,3,4,5]
    print(solution.arraySign(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [-1,-2,-3,-4,-5]
    print(solution.arraySign(nums5))  # Expected Output: -1

test_array_sign()