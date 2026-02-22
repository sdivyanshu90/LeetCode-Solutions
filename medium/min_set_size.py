class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        freq = sorted(freq.items(), key = lambda x: -x[1])
        res = 0
        count = 0
        for key, val in freq:
            count += val
            res += 1
            if count >= len(arr) // 2:
                return res
        return res

def test_minSetSize():
    solution = Solution()

    # Test case 1
    arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
    expected = 2
    print(solution.minSetSize(arr))  # Expected Output: 2

    # Test case 2
    arr = [7, 7, 7, 7, 7, 7]
    expected = 1
    print(solution.minSetSize(arr))  # Expected Output: 1

    # Test case 3
    arr = [1,9]
    expected = 1
    print(solution.minSetSize(arr))  # Expected Output: 1

    # Test case 4
    arr = [1000,1000,3,7]
    expected = 1
    print(solution.minSetSize(arr))  # Expected Output: 1

    # Test case 5
    arr = [1,2,3,4,5,6,7,8,9,10]
    expected = 5
    print(solution.minSetSize(arr))  # Expected Output: 5

test_minSetSize()