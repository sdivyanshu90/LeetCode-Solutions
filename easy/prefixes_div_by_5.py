from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = list()
        prefix = 0
        for num in nums:
            prefix = ((prefix << 1) + num) % 5
            answer.append(prefix == 0)
        return answer

def test_prefixes_div_by_5():
    solution = Solution()

    # Test case 1
    nums1 = [0,1,1]
    print(solution.prefixesDivBy5(nums1))  # Expected output: [True, False, False]

    # Test case 2
    nums2 = [1,1,1]
    print(solution.prefixesDivBy5(nums2))  # Expected output: [False, False, False]

    # Test case 3
    nums3 = [0,1,1,1,1,1]
    print(solution.prefixesDivBy5(nums3))  # Expected output: [True, False, False, False, True, False]

    # Test case 4
    nums4 = [1,0,1,0,1]
    print(solution.prefixesDivBy5(nums4))  # Expected output: [False, False, True, False, True]

    # Test case 5
    nums5 = [0,0,0,0]
    print(solution.prefixesDivBy5(nums5))  # Expected output: [True, True, True, True]

test_prefixes_div_by_5()