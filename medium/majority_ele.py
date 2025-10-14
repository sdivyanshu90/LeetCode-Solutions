from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = []
        
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1 = count2 = 0
        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
        
        threshold = len(nums) // 3
        if count1 > threshold:
            result.append(candidate1)
        if candidate1 != candidate2 and count2 > threshold:
            result.append(candidate2)
        
        return result

def test_majority_element():
    s = Solution()

    # Test Case 1: Two majority elements
    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [1, 2]

    # Test Case 2: One majority element
    nums = [3, 2, 3]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [3]
    
    # Test Case 3: No majority elements
    nums = [1, 2, 3, 4]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: []

    # Test Case 4: Empty list (edge case)
    nums = []
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: []

    # Test Case 5: Small list where all elements are majority elements
    nums = [1, 2]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [1, 2]

    # Test Case 6: All elements are the same
    nums = [5, 5, 5, 5]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [5]

    # Test Case 7: Elements at the exact n/3 threshold
    nums = [2, 2, 1, 1, 3, 3]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: []

    # Test Case 8: List with negative numbers and zero
    nums = [0, 0, 0, -1, -1]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [-1, 0]

    # Test Case 9: Decoy candidates that get eliminated
    nums = [10, 20, 10, 30, 10, 40, 10]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [10]

    # Test Case 10: Complex case where only one candidate is valid after verification
    nums = [2, 1, 1, 3, 1, 4, 5, 6]
    print(f"\nInput: nums = {nums}")
    print(f"Output: {sorted(s.majorityElement(nums))}") # Expected: [1]

test_majority_element()