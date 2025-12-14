from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = {0}
        for x in arr:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)

def test_subarray_bitwise_ors():
    solution = Solution()

    # Test case 1
    arr1 = [0]
    print(solution.subarrayBitwiseORs(arr1))  # Expected output: 1

    # Test case 2
    arr2 = [1, 1, 2]
    print(solution.subarrayBitwiseORs(arr2))  # Expected output: 3

    # Test case 3
    arr3 = [1, 2, 4]
    print(solution.subarrayBitwiseORs(arr3))  # Expected output: 6

    # Test case 4
    arr4 = [3, 5, 7, 9]
    print(solution.subarrayBitwiseORs(arr4))  # Expected output: 8

    # Test case 5
    arr5 = [1, 2, 3, 4, 5]
    print(solution.subarrayBitwiseORs(arr5))  # Expected output: 10

test_subarray_bitwise_ors()