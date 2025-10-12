from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        H = defaultdict(int)
        for i in range(n):
            H[nums[i]] += 1
            
            if H[nums[i]] > n / 2:
                return nums[i]

# Approach 2
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         n=len(nums)
#         return nums[n//2]

def test_majority_element():
    s = Solution()

    # Test Case 1: Simple case with an odd number of elements
    print(s.majorityElement([3, 2, 3])) # Expected Output: 3

    # Test Case 2: Simple case with an even number of elements
    print(s.majorityElement([2, 2, 1, 1, 1, 2, 2])) # Expected Output: 2

    # Test Case 3: List with a single element
    print(s.majorityElement([1])) # Expected Output: 1

    # Test Case 4: Bare majority in an even length list
    print(s.majorityElement([1, 2, 1, 3, 1, 1])) # Expected Output: 1

    # Test Case 5: Bare majority in an odd length list
    print(s.majorityElement([6, 6, 5, 5, 6])) # Expected Output: 6

    # Test Case 6: Majority element is negative
    print(s.majorityElement([-1, -1, 2, 3, -1])) # Expected Output: -1

    # Test Case 7: Majority element is zero
    print(s.majorityElement([0, 5, 5, 0, 0])) # Expected Output: 0

    # Test Case 8: Majority element appears late in the list
    print(s.majorityElement([1, 2, 1, 2, 3, 2, 2])) # Expected Output: 2

    # Test Case 9: List with two identical elements
    print(s.majorityElement([10, 10])) # Expected Output: 10
    
    # Test Case 10: List with large numbers
    print(s.majorityElement([1000000000, 5, 1000000000])) # Expected Output: 1000000000

test_majority_element()