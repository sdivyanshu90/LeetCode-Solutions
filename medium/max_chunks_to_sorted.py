class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        prefix_max = arr[:]
        suffix_min = arr[:]

        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], prefix_max[i])

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], suffix_min[i])

        chunks = 0
        for i in range(n):
            if i == 0 or suffix_min[i] > prefix_max[i - 1]:
                chunks += 1

        return chunks

def test_max_chunks_to_sorted():
    solution = Solution()
    
    # Test case 1
    arr1 = [4,3,2,1,0]
    print(solution.maxChunksToSorted(arr1)) # Expected: 1
    
    # Test case 2
    arr2 = [1,0,2,3,4]
    print(solution.maxChunksToSorted(arr2)) # Expected: 4
    
    # Test case 3
    arr3 = [2,0,1,3]
    print(solution.maxChunksToSorted(arr3)) # Expected: 2
    
    # Test case 4
    arr4 = [0,1,2,3,4]
    print(solution.maxChunksToSorted(arr4)) # Expected: 5

    # Test case 5
    arr5 = [1,2,0,3,4]
    print(solution.maxChunksToSorted(arr5)) # Expected: 3

    # Test case 6
    arr6 = [3,2,1,0,4]
    print(solution.maxChunksToSorted(arr6)) # Expected: 2

    # Test case 7
    arr7 = [2,1,0,3,4]
    print(solution.maxChunksToSorted(arr7)) # Expected: 2

    # Test case 8
    arr8 = [1,2,3,4,0]
    print(solution.maxChunksToSorted(arr8)) # Expected: 1

    # Test case 9
    arr9 = [0]
    print(solution.maxChunksToSorted(arr9)) # Expected: 1

    # Test case 10
    arr10 = [1,0]
    print(solution.maxChunksToSorted(arr10)) # Expected: 1

test_max_chunks_to_sorted()