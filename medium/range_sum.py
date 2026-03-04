class Solution:
    def rangeSum(self, nums, n, left, right):
        mod = 10**9 + 7

        def count_and_sum(nums, n, target):
            count = 0
            current_sum = 0
            total_sum = 0
            window_sum = 0
            i = 0
            for j in range(n):
                current_sum += nums[j]
                window_sum += nums[j] * (j - i + 1)
                while current_sum > target:
                    window_sum -= current_sum
                    current_sum -= nums[i]
                    i += 1
                count += j - i + 1
                total_sum += window_sum
            return count, total_sum

        def sum_of_first_k(nums, n, k):
            min_sum = min(nums)
            max_sum = sum(nums)
            left = min_sum
            right = max_sum

            while left <= right:
                mid = left + (right - left) // 2
                if count_and_sum(nums, n, mid)[0] >= k:
                    right = mid - 1
                else:
                    left = mid + 1
            count, total_sum = count_and_sum(nums, n, left)
            return total_sum - left * (count - k)

        result = (
            sum_of_first_k(nums, n, right) - sum_of_first_k(nums, n, left - 1)
        ) % mod
        return (result + mod) % mod

def test_range_sum():
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4]
    n1 = 4
    left1 = 1
    right1 = 5
    print(solution.rangeSum(nums1, n1, left1, right1))  # Expected output: 13

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    n2 = 4
    left2 = 3
    right2 = 4
    print(solution.rangeSum(nums2, n2, left2, right2))  # Expected output: 6

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    n3 = 4
    left3 = 9
    right3 = 10
    print(solution.rangeSum(nums3, n3, left3, right3))  # Expected output: 0

    # Test Case 4
    nums4 = [10**2] * (10**2)
    n4 = 10**2
    left4 = 1
    right4 = (n4 * (n4 + 1)) // 2
    print(solution.rangeSum(nums4, n4, left4, right4))  # Expected output: (10^5 * (10^5 + 1) // 2) * (10^5 % (10^9 + 7)) % (10^9 + 7)

    # Test Case 5
    nums5 = [1] * (10**5)
    n5 = 10**5
    left5 = 1
    right5 = (n5 * (n5 + 1)) // 2
    print(solution.rangeSum(nums5, n5, left5, right5))  # Expected output: (10^5 * (10^5 + 1) // 2)

test_range_sum()