from typing import List
from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0,0)])
        n = len(nums)
        res = []

        while queue:
            i, j = queue.popleft()
            res.append(nums[i][j])

            if j == 0 and i + 1 < n:
                queue.append([i+1, j])
            
            if j + 1 < len(nums[i]):
                queue.append([i, j + 1])
        
        return res

def test_find_diagonal_order():
    solution = Solution()

    # Test case 1
    nums1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.findDiagonalOrder(nums1))  # Expected output: [1,4,2,7,5,3,8,6,9]

    # Test case 2
    nums2 = [[1,2],[3],[4,5,6]]
    print(solution.findDiagonalOrder(nums2))  # Expected output: [1,3,2,4,5,6]

    # Test case 3
    nums3 = [[1,2,3,4,5]]
    print(solution.findDiagonalOrder(nums3))  # Expected output: [1,2,3,4,5]

    # Test case 4
    nums4 = [[1],[2],[3],[4],[5]]
    print(solution.findDiagonalOrder(nums4))  # Expected output: [1,2,3,4,5]

    # Test case 5
    nums5 = [[1]]
    print(solution.findDiagonalOrder(nums5))  # Expected output: [1]

test_find_diagonal_order()