class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
 
        return False

def test_checkIfExist():
    solution = Solution()

    # Test case 1
    arr = [10, 2, 5, 3]
    expected = True
    print(solution.checkIfExist(arr))  # Expected Output: True

    # Test case 2
    arr = [7, 1, 14, 11]
    expected = True
    print(solution.checkIfExist(arr))  # Expected Output: True

    # Test case 3
    arr = [3, 1, 7, 11]
    expected = False
    print(solution.checkIfExist(arr))  # Expected Output: False

    # Test case 4
    arr = [-2,0,10,-19,4,6,-8]
    expected = False
    print(solution.checkIfExist(arr))  # Expected Output: False

    # Test case 5
    arr = [0,0]
    expected = True
    print(solution.checkIfExist(arr))  # Expected Output: True

test_checkIfExist()