from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1

        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > greatest:
                arr[i], greatest = greatest, arr[i]
            else:
                arr[i] = greatest
        return arr

def test_replace_elements():
    solution = Solution()

    # Test case 1
    arr = [17,18,5,4,6,1]
    print(solution.replaceElements(arr))  # Expected output: [18,6,6,6,1,-1]

    # Test case 2
    arr = [400]
    print(solution.replaceElements(arr))  # Expected output: [-1]

    # Test case 3
    arr = [1,2,3,4]
    print(solution.replaceElements(arr))  # Expected output: [4,4,4,-1]

    # Test case 4
    arr = [7,7,7]
    print(solution.replaceElements(arr))  # Expected output: [7,7,-1]

    # Test case 5
    arr = [5,4,3,2,1]
    print(solution.replaceElements(arr))  # Expected output: [4,3,2,1,-1]

test_replace_elements()