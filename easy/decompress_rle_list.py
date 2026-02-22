class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(0, len(nums), 2):
            key, val = nums[i], nums[i + 1]
            res.extend([val] * key)
        return res

def test_decompress_rle_list():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 4]
    expected = [2, 4, 4, 4]
    print(solution.decompressRLElist(nums))  # Expected Output: [2, 4, 4, 4]

    # Test case 2
    nums = [1, 1, 2, 3]
    expected = [1, 3, 3]
    print(solution.decompressRLElist(nums))  # Expected Output: [1, 3, 3]

    # Test case 3
    nums = [1, 1, 1, 2]
    expected = [1, 2]
    print(solution.decompressRLElist(nums))  # Expected Output: [1, 2]

    # Test case 4
    nums = [3, 4]
    expected = [4, 4, 4]
    print(solution.decompressRLElist(nums))  # Expected Output: [4, 4, 4]

    # Test case 5
    nums = [2, 5, 3, 6]
    expected = [5, 5, 6, 6, 6]
    print(solution.decompressRLElist(nums))  # Expected Output: [5, 5, 6, 6, 6]

test_decompress_rle_list()