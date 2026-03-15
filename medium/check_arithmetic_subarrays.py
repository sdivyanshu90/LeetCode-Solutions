from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        def checkArithmetic(arr):
            if len(arr) < 2: return False

            arr.sort()

            diff = arr[1] - arr[0]

            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff: return False
            
            return True

        for start, end in zip(l, r):
            answer.append(checkArithmetic(nums[start:end + 1]))

        return answer

def test_check_arithmetic_subarrays():
    solution = Solution()

    # Test case 1
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    print(solution.checkArithmeticSubarrays(nums, l, r))  # Expected output: [True, False, True]

    # Test case 2
    nums = [-12, -9, -3, -6, -15, -21, -18]
    l = [0, 1, 6]
    r = [1, 4, 6]
    print(solution.checkArithmeticSubarrays(nums, l, r))  # Expected output: [True, False, False]

    # Test case 3
    nums = [1]
    l = [0]
    r = [0]
    print(solution.checkArithmeticSubarrays(nums, l, r))  # Expected output: [False]

    # Test case 4
    nums = [1, 2, 3, 4, 5]
    l = [0, 1, 2]
    r = [4, 3, 2]
    print(solution.checkArithmeticSubarrays(nums, l, r))  # Expected output: [True, True, False]

    # Test case 5
    nums = [1, 3, 5, 7, 9]
    l = [0, 1, 2]
    r = [4, 3, 2]
    print(solution.checkArithmeticSubarrays(nums, l, r))  # Expected output: [True, True, False]

test_check_arithmetic_subarrays()