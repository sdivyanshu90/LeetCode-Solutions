from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        num_ct = {}
        nice_pairs = 0

        for num in nums:
            nice = int(str(num)[::-1]) - num

            if nice in num_ct:
                nice_pairs += num_ct[nice]

            if nice in num_ct:
                num_ct[nice] += 1
            else:
                num_ct[nice] = 1

        return nice_pairs % (10 ** 9 + 7)

def test_count_nice_pairs():
    solution = Solution()

    # Test Case 1
    nums1 = [42,11,1,97]
    print(solution.countNicePairs(nums1))  # Expected Output: 2

    # Test Case 2
    nums2 = [13,10,35,24,76]
    print(solution.countNicePairs(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1,2,3,4,5]
    print(solution.countNicePairs(nums3))  # Expected Output: 10

    # Test Case 4
    nums4 = [123,321,213,132]
    print(solution.countNicePairs(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [1000,1,10,100]
    print(solution.countNicePairs(nums5))  # Expected Output: 0

test_count_nice_pairs()