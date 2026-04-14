class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Method 1
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            if left == right:
                return i
        return -1

        # Method 2
        # n = len(nums)
        # prefix = [0]*(n+1)

        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]
        
        # total = prefix[n]

        # for i in range(n):
        #     left = prefix[i]
        #     right = total - prefix[i+1]
        #     if left == right:
        #         return i
        # return -1


        # Method 3
        # total = sum(nums)
        # left = 0

        # for i, num in enumerate(nums):
        #     right = total - left - num
        #     if left == right:
        #         return i
        #     left += num
        # return -1

def test_find_middle_index():
    solution = Solution()

    # Test case 1
    nums1 = [2, 3, -1, 8, 4]
    print(solution.findMiddleIndex(nums1))  # Expected output: 3

    # Test case 2
    nums2 = [1, -1, 4]
    print(solution.findMiddleIndex(nums2))  # Expected output: 2

    # Test case 3
    nums3 = [2, 5]
    print(solution.findMiddleIndex(nums3))  # Expected output: -1

    # Test case 4
    nums4 = [10]
    print(solution.findMiddleIndex(nums4))  # Expected output: 0

    # Test case 5
    nums5 = [-1, -1, -1, -1, -1, -1]
    print(solution.findMiddleIndex(nums5))  # Expected output: -1

test_find_middle_index()