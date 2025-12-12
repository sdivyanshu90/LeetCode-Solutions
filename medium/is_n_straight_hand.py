from typing import List
from collections import Counter

class Solution:
    def isNStraightHand(self, nums: List[int], size: int) -> bool:
        N = len(nums)
        if N % size:
            return False
        freq = Counter(nums)
        nums.sort()
        for num in nums:
            if freq[num]:
                for cur in range(num, num + size):
                    freq[cur] -= 1
                    if freq[cur] < 0:
                        return False
        return True

def test_isNStraightHand():
    solution = Solution()
    
    # Test Case 1
    print(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)) # Expected: True

    # Test Case 2
    print(solution.isNStraightHand([1,2,3,4,5], 4)) # Expected: False

    # Test Case 3
    print(solution.isNStraightHand([1,2,3,4,5,6], 2)) # Expected: True

    # Test Case 4
    print(solution.isNStraightHand([1,2,3,4,5,6], 3)) # Expected: True

    # Test Case 5
    print(solution.isNStraightHand([1,2,3,4,5], 5)) # Expected: True

test_isNStraightHand()