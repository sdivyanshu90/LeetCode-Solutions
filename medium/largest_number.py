from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ""
            
        str_nums = [str(num) for num in nums]
        str_nums.sort(key = lambda a: a * 10, reverse = True)

        if str_nums[0] == "0":
            return "0"
            
        return "".join(str_nums)

def test_largest_number():
    s = Solution()

    # Test Case 1: Standard case
    print(s.largestNumber([10, 2])) # Expected Output: 210

    # Test Case 2: Complex case with prefix-like numbers
    print(s.largestNumber([3, 30, 34, 5, 9])) # Expected Output: 9534330

    # Test Case 3: All zeros
    print(s.largestNumber([0, 0, 0])) # Expected Output: 0

    # Test Case 4: Numbers with different lengths
    print(s.largestNumber([89, 9, 45, 7])) # Expected Output: 989745

    # Test Case 5: Single element list
    print(s.largestNumber([1])) # Expected Output: 1

    # Test Case 6: Tricky prefix comparison
    print(s.largestNumber([12, 121])) # Expected Output: 12121

    # Test Case 7: Another tricky prefix comparison
    print(s.largestNumber([80, 8, 0, 81])) # Expected Output: 881800

    # Test Case 8: All single-digit numbers
    print(s.largestNumber([9, 5, 3, 1, 7])) # Expected Output: 97531

    # Test Case 9: Large numbers
    print(s.largestNumber([478, 47, 471])) # Expected Output: 47847471
    
    # Test Case 10: Critical Failure Case - Empty List
    print(s.largestNumber([])) # Expected Output: ""

test_largest_number()