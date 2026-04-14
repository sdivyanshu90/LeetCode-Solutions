class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = min(nums), max(nums)
        while b:
            a, b = b, a % b
        return a

def test_find_gcd():
    solution = Solution()

    # Test case 1
    nums1 = [2, 5, 6, 9, 10]
    print(solution.findGCD(nums1))  # Expected output: 2

    # Test case 2
    nums2 = [7, 5, 6, 8, 3]
    print(solution.findGCD(nums2))  # Expected output: 1

    # Test case 3
    nums3 = [3, 3]
    print(solution.findGCD(nums3))  # Expected output: 3

    # Test case 4
    nums4 = [12, 15, 18]
    print(solution.findGCD(nums4))  # Expected output: 3

    # Test case 5
    nums5 = [100, 75, 25]
    print(solution.findGCD(nums5))  # Expected output: 25

test_find_gcd()