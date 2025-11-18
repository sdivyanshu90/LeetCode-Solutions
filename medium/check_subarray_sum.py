class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i

        return False

def test_check_subarray_sum():
    s = Solution()

    # Test case 1
    nums1 = [23, 2, 4, 6, 7]
    k1 = 6
    peinr(s.checkSubarraySum(nums1, k1)) # Expected output: True

    # Test case 2
    nums2 = [23, 2, 6, 4, 7]
    k2 = 6
    print(s.checkSubarraySum(nums2, k2)) # Expected output: True

    # Test case 3
    nums3 = [23, 2, 6, 4, 7]
    k3 = 13
    print(s.checkSubarraySum(nums3, k3)) # Expected output: False

    # Test case 4
    nums4 = [0, 0]
    k4 = 0
    print(s.checkSubarraySum(nums4, k4)) # Expected output: True

    # Test case 5
    nums5 = [1, 2, 3]
    k5 = 5
    print(s.checkSubarraySum(nums5, k5)) # Expected output: True

test_check_subarray_sum()