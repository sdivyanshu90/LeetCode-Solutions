from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}
        
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            
        for num, count in num_count.items():
            if count == 1:
                return num

def test_singleNumber():
    solution = Solution()
    # Test Case 1
    print(solution.singleNumber([2, 2, 1])) # Expected output: 1

    # Test Case 2
    print(solution.singleNumber([4, 1, 2, 1, 2])) # Expected output: 4

    # Test Case 3
    print(solution.singleNumber([1])) # Expected output: 1

    # Test Case 4
    print(solution.singleNumber([0, 1, 0])) # Expected output: 1

    # Test Case 5
    print(solution.singleNumber([-1, -1, -2])) # Expected output: -2

test_singleNumber()