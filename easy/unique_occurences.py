from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        has = set()
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
                
        # print(freq)
        for key, val in freq.items():
            if val in has:
                return False
            has.add(val)
        return True

def test_unique_occurrences():
    solution = Solution()

    # Test Case 1
    arr1 = [1,2,2,1,1,3]
    print(solution.uniqueOccurrences(arr1))  # Expected Output: True

    # Test Case 2
    arr2 = [1,2]
    print(solution.uniqueOccurrences(arr2))  # Expected Output: False

    # Test Case 3
    arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
    print(solution.uniqueOccurrences(arr3))  # Expected Output: True

    # Test Case 4
    arr4 = [1,1,2,2,2,3,3,3]
    print(solution.uniqueOccurrences(arr4))  # Expected Output: False

    # Test Case 5
    arr5 = [5]
    print(solution.uniqueOccurrences(arr5))  # Expected Output: True

test_unique_occurrences()