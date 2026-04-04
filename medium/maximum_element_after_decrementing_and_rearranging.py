class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] >= ans + 1:
                ans += 1

        return ans

def test_maximum_element_after_decrementing_and_rearranging():
    solution = Solution()

    # Test case 1
    arr1 = [2, 2, 1, 2, 1]
    print(solution.maximumElementAfterDecrementingAndRearranging(arr1))  # Expected output: 2

    # Test case 2
    arr2 = [100, 1, 1000]
    print(solution.maximumElementAfterDecrementingAndRearranging(arr2))  # Expected output: 3

    # Test case 3
    arr3 = [1, 1, 1, 1]
    print(solution.maximumElementAfterDecrementingAndRearranging(arr3))  # Expected output: 1

    # Test case 4
    arr4 = [3, 2, 1]
    print(solution.maximumElementAfterDecrementingAndRearranging(arr4))  # Expected output: 3

    # Test case 5
    arr5 = [10, 9, 8, 7]
    print(solution.maximumElementAfterDecrementingAndRearranging(arr5))  # Expected output: 4

test_maximum_element_after_decrementing_and_rearranging()