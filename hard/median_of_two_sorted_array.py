# Approach 1
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums) - 1
        if len(nums) % 2 == 0:
            a = ((nums[n//2]) + (math.ceil(nums[(n+1)//2])))/2
            return a
        else:
            b = math.ceil(nums[(n+1)//2])
            return b

# Approach 2
import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        return statistics.median(arr)