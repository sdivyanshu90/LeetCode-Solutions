from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []
        for num in arr:
            if num == 0:
                new_arr.extend([0, 0])
            else:
                new_arr.append(num)
        for i in range(len(arr)):
            arr[i] = new_arr[i]

def test_duplicate_zeros():
    solution = Solution()

    # Test case 1
    arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(arr1)
    print(arr1)  # Expected output: [1,0,0,2,3,0,0,4]

    # Test case 2
    arr2 = [1, 2, 3]
    solution.duplicateZeros(arr2)
    print(arr2)  # Expected output: [1,2,3]

    # Test case 3
    arr3 = [0, 0, 0, 0, 0]
    solution.duplicateZeros(arr3)
    print(arr3)  # Expected output: [0,0,0,0,0]

    # Test case 4
    arr4 = [8, 4, 5, 0, 0, 0, 0, 7]
    solution.duplicateZeros(arr4)
    print(arr4)  # Expected output: [8,4,5,0,0,0,0,0]

    # Test case 5
    arr5 = [1]
    solution.duplicateZeros(arr5)
    print(arr5)  # Expected output: [1]

test_duplicate_zeros()