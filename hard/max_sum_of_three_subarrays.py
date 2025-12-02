from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        best_sum = [[0] * (n + 1) for _ in range(4)]
        best_index = [[0] * (n + 1) for _ in range(4)]

        for t in range(1, 4):
            for i in range(k * t, n + 1):
                current_sum = (
                    prefix_sum[i] - prefix_sum[i - k] + best_sum[t - 1][i - k]
                )

                if current_sum > best_sum[t][i - 1]:
                    best_sum[t][i] = current_sum
                    best_index[t][i] = i - k
                else:
                    best_sum[t][i] = best_sum[t][i - 1]
                    best_index[t][i] = best_index[t][i - 1]

        result = [0] * 3
        end = n
        for t in range(3, 0, -1):
            result[t - 1] = best_index[t][end]
            end = result[t - 1]

        return result

def test_max_sum_of_three_subarrays():
    solution = Solution()

    # Test Case 1
    nums1 = [1,2,1,2,6,7,5,1]
    k1 = 2
    print(solution.maxSumOfThreeSubarrays(nums1, k1))  # Expected: [0, 3, 5]

    # Test Case 2
    nums2 = [4,5,10,6,11,17,4,5,10,6,11,17]
    k2 = 3
    print(solution.maxSumOfThreeSubarrays(nums2, k2))  # Expected: [0, 3, 9]

    # Test Case 3
    nums3 = [1,2,1,2,1,2,1,2,1]
    k3 = 2
    print(solution.maxSumOfThreeSubarrays(nums3, k3))  # Expected: [0, 2, 4]

    # Test Case 4
    nums4 = [7,13,20,19,19,2,10,1,1,19]
    k4 = 3
    print(solution.maxSumOfThreeSubarrays(nums4, k4))  # Expected: [1, 4, 7]

    # Test Case 5
    nums5 = [3,8,1,3,2,1,8,9,0,7,1,2]
    k5 = 2
    print(solution.maxSumOfThreeSubarrays(nums5, k5))  # Expected: [0, 6, 9]

test_max_sum_of_three_subarrays()