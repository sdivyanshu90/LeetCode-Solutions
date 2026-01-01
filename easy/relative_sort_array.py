from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_element = max(arr1)
        count = [0] * (max_element + 1)

        for element in arr1:
            count[element] += 1

        result = []
        for value in arr2:
            while count[value] > 0:
                result.append(value)
                count[value] -= 1

        for num in range(max_element + 1):
            while count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result

def test_relative_sort_array():
    solution = Solution()

    # Test case 1
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(solution.relativeSortArray(arr1, arr2))  # Expected output: [2,2,2,1,4,3,3,9,6,7,19]

    # Test case 2
    arr1 = [28,6,22,8,44,17]
    arr2 = [22,28,8,6]
    print(solution.relativeSortArray(arr1, arr2))  # Expected output: [22,28,8,6,17,44]

    # Test case 3
    arr1 = [1,2,3,4,5]
    arr2 = [5,4,3,2,1]
    print(solution.relativeSortArray(arr1, arr2))  # Expected output: [5,4,3,2,1]

    # Test case 4
    arr1 = [10,20,30]
    arr2 = [20,10]
    print(solution.relativeSortArray(arr1, arr2))  # Expected output: [20,10,30]

    # Test case 5
    arr1 = [5,3,1,4,2]
    arr2 = [3,5]
    print(solution.relativeSortArray(arr1, arr2))  # Expected output: [3,5,1,2,4]

test_relative_sort_array()