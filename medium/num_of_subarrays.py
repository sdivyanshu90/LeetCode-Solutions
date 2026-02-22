class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        target = threshold * k
        window = sum(arr[:k])
        
        if window >= target:
            res += 1

        for i in range(k , len(arr)):
            window += arr[i] - arr[i - k]
            if window >= target:
                res += 1

        return res

def test_numOfSubarrays():
    solution = Solution()

    # Test case 1
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    expected = 3
    print(solution.numOfSubarrays(arr, k, threshold))  # Expected Output: 3

    # Test case 2
    arr = [1, 1, 1, 1, 1]
    k = 1
    threshold = 0
    expected = 5
    print(solution.numOfSubarrays(arr, k, threshold))  # Expected Output: 5

    # Test case 3
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    expected = 6
    print(solution.numOfSubarrays(arr, k, threshold))  # Expected Output: 6

    # Test case 4
    arr = [7,7,7,7,7,7,7]
    k = 7
    threshold = 7
    expected = 1
    print(solution.numOfSubarrays(arr, k, threshold))  # Expected Output: 1

    # Test case 5
    arr = [4,4,4,4]
    k = 4
    threshold = 1
    expected = 1
    print(solution.numOfSubarrays(arr, k, threshold))  # Expected Output: 1

test_numOfSubarrays()