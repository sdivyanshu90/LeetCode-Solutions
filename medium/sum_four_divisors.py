from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for num in nums:
            count = 0
            div_sum = 0
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    count += 1
                    div_sum += i
                    if i != num // i:
                        count += 1
                        div_sum += num // i
                if count > 4:
                    break
            if count == 4:
                total_sum += div_sum
        return total_sum

def test_sum_four_divisors():
    solution = Solution()

    # Test case 1
    nums1 = [21, 4, 7]
    print(solution.sumFourDivisors(nums1))  # Expected output: 32

    # Test case 2
    nums2 = [21, 21]
    print(solution.sumFourDivisors(nums2))  # Expected output: 64

    # Test case 3
    nums3 = [1, 2, 3, 4, 5]
    print(solution.sumFourDivisors(nums3))  # Expected output: 0

    # Test case 4
    nums4 = [6, 28, 496]
    print(solution.sumFourDivisors(nums4))  # Expected output: 12

    # Test case 5
    nums5 = [12, 18, 20]
    print(solution.sumFourDivisors(nums5))  # Expected output: 0

test_sum_four_divisors()