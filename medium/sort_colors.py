class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        left, current, right = 0, 0, len(nums) - 1
        
        while current <= right:
            if nums[current] == 0:
                swap(nums, left, current)
                left += 1
                current += 1
            elif nums[current] == 2:
                swap(nums, current, right)
                right -= 1
            else:
                current += 1


def test_sort_colors():
    solution = Solution()

    # Test case 1
    nums1 = [2,0,2,1,1,0]
    solution.sortColors(nums1)
    print(nums1)  # Expected output: [0,0,1,1,2,2]

    # Test case 2
    nums2 = [2,0,1]
    solution.sortColors(nums2)
    print(nums2)  # Expected output: [0,1,2]

    # Test case 3
    nums3 = [0]
    solution.sortColors(nums3)
    print(nums3)  # Expected output: [0]

    # Test case 4
    nums4 = [1]
    solution.sortColors(nums4)
    print(nums4)  # Expected output: [1]

    # Test case 5
    nums5 = [1,2,0]
    solution.sortColors(nums5)
    print(nums5)  # Expected output: [0,1,2]

    # Test case 6
    nums6 = [0,0,0]
    solution.sortColors(nums6)
    print(nums6)  # Expected output: [0,0,0]

    # Test case 7
    nums7 = [2,2,2]
    solution.sortColors(nums7)
    print(nums7)  # Expected output: [2,2,2]

    # Test case 8
    nums8 = [1,1,1]
    solution.sortColors(nums8)
    print(nums8)  # Expected output: [1,1,1]

    # Test case 9
    nums9 = [2,1,0,2,1,0,2,1,0]
    solution.sortColors(nums9)
    print(nums9)  # Expected output: [0,0,0,1,1,1,2,2,2]
    
    # Test case 10
    nums10 = [0,2,1,0,2,1,0,2,1]
    solution.sortColors(nums10)
    print(nums10)  # Expected output: [0,0,0,1,1,1,2,2,2]

test_sort_colors()