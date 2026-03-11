from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr)
        
        while low < high:
            mid = (low + high) // 2
            missing_count = arr[mid] - (mid + 1)
            
            if missing_count < k:
                low = mid + 1
            else:
                high = mid

        return low + k

def test_find_kth_positive():
    solution = Solution()

    # Test case 1
    arr1 = [2, 3, 4, 7, 11]
    k1 = 5
    print(solution.findKthPositive(arr1, k1))  # Expected output: 9

    # Test case 2
    arr2 = [1, 2, 3, 4]
    k2 = 2
    print(solution.findKthPositive(arr2, k2))  # Expected output: 6

    # Test case 3
    arr3 = [2, 3, 4]
    k3 = 3
    print(solution.findKthPositive(arr3, k3))  # Expected output: 6

    # Test case 4
    arr4 = [1, 2, 3]
    k4 = 1
    print(solution.findKthPositive(arr4, k4))  # Expected output: 4

    # Test case 5
    arr5 = [1, 3, 5, 7]
    k5 = 4
    print(solution.findKthPositive(arr5, k5))  # Expected output: 8

test_find_kth_positive()