from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

def test_top_k_frequent():
    s = Solution()

    # Test Case 1: Example with multiple frequencies
    nums = [1,1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums, k))  # Expected: [1, 2]

    # Test Case 2: All elements are the same
    nums = [4,4,4,4]
    k = 1
    print(s.topKFrequent(nums, k))  # Expected: [4]

    # Test Case 3: Multiple elements with same frequency
    nums = [1,2,3,4,5,6]
    k = 3
    print(s.topKFrequent(nums, k))  # Expected: Any 3 elements from [1,2,3,4,5,6]

    # Test Case 4: Single element array
    nums = [10]
    k = 1
    print(s.topKFrequent(nums, k))  # Expected: [10]

    # Test Case 5: Large array with varying frequencies
    nums = [1]*1000 + [2]*500 + [3]*200 + [4]*100 + [5]*50
    k = 3
    print(s.topKFrequent(nums, k))  # Expected: [1, 2, 3]

    # Test Case 6: Edge case with k equal to number of unique elements
    nums = [7,8,9]
    k = 3
    print(s.topKFrequent(nums, k))  # Expected: [7, 8, 9] in any order

    # Test Case 7: Edge case with negative numbers
    nums = [-1,-1,-2,-2,-2,-3]
    k = 2
    print(s.topKFrequent(nums, k))  # Expected: [-2, -1]

    # Test Case 8: Large k value
    nums = [1,2,2,3,3,3]
    k = 3
    print(s.topKFrequent(nums, k))  # Expected: [3, 2, 1]

    # Test Case 9: Empty array (should handle gracefully)
    nums = []
    k = 0
    print(s.topKFrequent(nums, k))  # Expected: None

    # Test Case 10: All unique elements
    nums = [10,20,30,40,50]
    k = 5
    print(s.topKFrequent(nums, k))  # Expected: [10, 20, 30, 40, 50]

test_top_k_frequent()