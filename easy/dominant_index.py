from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = 0
        second_largest = None

        for i in range(1, len(nums)):
            if nums[i] > nums[largest]:
                second_largest = largest
                largest = i
            elif second_largest is None or nums[i] > nums[second_largest]:
                second_largest = i

        if nums[largest] >= 2 * nums[second_largest]:
            return largest
        else:
            return -1

def test_dominant_index():
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 6, 1, 0]
    print(solution.dominantIndex(nums1)) # Expected: 1
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(solution.dominantIndex(nums2)) # Expected: -1
    
    # Test case 3
    nums3 = [1]
    print(solution.dominantIndex(nums3)) # Expected: 0
    
    # Test case 4
    nums4 = [0, 0, 3, 2]
    print(solution.dominantIndex(nums4)) # Expected: -1
    
    # Test case 5
    nums5 = [0, 0, 0, 1]
    print(solution.dominantIndex(nums5)) # Expected: 3

    # Test case 6
    nums6 = [10, 5, 2]
    print(solution.dominantIndex(nums6)) # Expected: 0

    # Test case 7
    nums7 = [2, 4, 8, 16]
    print(solution.dominantIndex(nums7)) # Expected: -1

    # Test case 8
    nums8 = [20, 10, 5]
    print(solution.dominantIndex(nums8)) # Expected: 0

    # Test case 9
    nums9 = [1, 0, 0, 0]
    print(solution.dominantIndex(nums9)) # Expected: 0

    # Test case 10
    nums10 = [5, 25, 10]
    print(solution.dominantIndex(nums10)) # Expected: -1

test_dominant_index()