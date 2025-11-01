from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = set()
        
        for num in nums:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        
        return sorted(list(duplicates))

def test_find_duplicates():
    s = Solution()

    # Test case 1
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDuplicates(nums))  # Expected output: [2, 3]

    # Test case 2
    nums = [1,1,2]
    print(s.findDuplicates(nums))  # Expected output: [1]

    # Test case 3
    nums = [1]
    print(s.findDuplicates(nums))  # Expected output: []

    # Test case 4
    nums = [2,2,2,2]
    print(s.findDuplicates(nums))  # Expected output: [2]

    # Test case 5
    nums = [3,3,3,3,3,3]
    print(s.findDuplicates(nums))  # Expected output: [3]

test_find_duplicates()