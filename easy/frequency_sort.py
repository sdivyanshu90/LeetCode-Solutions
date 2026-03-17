class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))

def test_frequency_sort():
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 2, 2, 2, 3]
    print(solution.frequencySort(nums1))  # Expected output: [3, 1, 1, 2, 2, 2]

    # Test case 2
    nums2 = [2, 3, 1, 3, 2]
    print(solution.frequencySort(nums2))  # Expected output: [1, 2, 2, 3, 3]

    # Test case 3
    nums3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(solution.frequencySort(nums3))  # Expected output: [5, -1, 4, 4, -6, -6, 1, 1, 1]

    # Test case 4
    nums4 = [1, 2, 3, 4, 5]
    print(solution.frequencySort(nums4))  # Expected output: [1, 2, 3, 4, 5]

    # Test case 5
    nums5 = [1, 1, 1, 2, 2, 3]
    print(solution.frequencySort(nums5))  # Expected output: [3, 2, 2, 1, 1, 1]

test_frequency_sort()