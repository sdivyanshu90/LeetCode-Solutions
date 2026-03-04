from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        arr = sorted(arr, key=lambda x: (k + x % k) % k)

        start = 0
        end = len(arr) - 1
        while start < end:
            if arr[start] % k != 0:
                break
            if arr[start + 1] % k != 0:
                return False
            start = start + 2

        while start < end:
            if (arr[start] + arr[end]) % k != 0:
                return False
            start += 1
            end -= 1

        return True

def test_can_arrange():
    solution = Solution()

    # Test Case 1
    arr1 = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    k1 = 5
    print(solution.canArrange(arr1, k1))  # Expected output: True

    # Test Case 2
    arr2 = [1, 2, 3, 4, 5, 6]
    k2 = 7
    print(solution.canArrange(arr2, k2))  # Expected output: True

    # Test Case 3
    arr3 = [-10, 10]
    k3 = 2
    print(solution.canArrange(arr3, k3))  # Expected output: True

    # Test Case 4
    arr4 = [-1, -2, -3, -4, -5]
    k4 = 5
    print(solution.canArrange(arr4, k4))  # Expected output: False

    # Test Case 5
    arr5 = [1, -1]
    k5 = 2
    print(solution.canArrange(arr5, k5))  # Expected output: True

test_can_arrange()