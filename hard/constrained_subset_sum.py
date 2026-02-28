class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        for i in range(len(nums)):
            if q: 
                nums[i] += q[0]
            while q and q[-1] < nums[i]: 
                q.pop()
            if nums[i] > 0: 
                q.append(nums[i])
            if q and i >= k and q[0] == nums[i - k]:
                q.popleft()
        return max(nums)

def test_constrained_subset_sum():
    solution = Solution()

    # Test case 1
    nums1 = [10,2,-10,5,20]
    k1 = 2
    print(solution.constrainedSubsetSum(nums1, k1))  # Expected output: 37

    # Test case 2
    nums2 = [-1,-2,-3]
    k2 = 1
    print(solution.constrainedSubsetSum(nums2, k2))  # Expected output: -1

    # Test case 3
    nums3 = [10,-2,-10,-5,20]
    k3 = 2
    print(solution.constrainedSubsetSum(nums3, k3))  # Expected output: 23

    # Test case 4
    nums4 = [9,-1,-5]
    k4 = 1
    print(solution.constrainedSubsetSum(nums4, k4))  # Expected output: 9

    # Test case 5
    nums5 = [1,-1,-2]
    k5 = 1
    print(solution.constrainedSubsetSum(nums5, k5))  # Expected output: 1

test_constrained_subset_sum()