from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(0, [])
        return res

def test_subsets():
    solution = Solution()

    # Test case 1
    nums1 = [1,2,3]
    print(solution.subsets(nums1))  # Expected output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    # Test case 2
    nums2 = [0]
    print(solution.subsets(nums2))  # Expected output: [[],[0]]

    # Test case 3
    nums3 = [1,2]
    print(solution.subsets(nums3))  # Expected output: [[],[1],[2],[1,2]]

    # Test case 4
    nums4 = [4,5,6]
    print(solution.subsets(nums4))  # Expected output: [[],[4],[5],[4,5],[6],[4,6],[5,6],[4,5,6]]

    # Test case 5
    nums5 = []
    print(solution.subsets(nums5))  # Expected output: [[]]

    # Test case 6
    nums6 = [1]
    print(solution.subsets(nums6))  # Expected output: [[],[1]]

    # Test case 7
    nums7 = [1,2,3,4]
    print(solution.subsets(nums7))  # Expected output: All subsets of [1,2,3,4]

    # Test case 8
    nums8 = [7,8]
    print(solution.subsets(nums8))  # Expected output: [[],[7],[8],[7,8]]

    # Test case 9
    nums9 = [9]
    print(solution.subsets(nums9))  # Expected output: [[],[9]]

    # Test case 10
    nums10 = [1,3,5]
    print(solution.subsets(nums10))  # Expected output: [[],[1],[3],[1,3],[5],[1,5],[3,5],[1,3,5]]

test_subsets()