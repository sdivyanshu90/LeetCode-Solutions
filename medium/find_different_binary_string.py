from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                
                return ""
            
            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero

            return generate(curr + "1")

        n = len(nums)
        nums = set(nums)
        return generate("")

def test_find_different_binary_string():
    solution = Solution()

    # Test case 1
    nums1 = ["01", "10"]
    print(solution.findDifferentBinaryString(nums1))  # Expected output: "00"

    # Test case 2
    nums2 = ["00", "01"]
    print(solution.findDifferentBinaryString(nums2))  # Expected output: "11"

    # Test case 3
    nums3 = ["111", "011", "001"]
    print(solution.findDifferentBinaryString(nums3))  # Expected output: "000"

    # Test case 4
    nums4 = ["0", "1"]
    print(solution.findDifferentBinaryString(nums4))  # Expected output: "00"

    # Test case 5
    nums5 = ["000", "001", "010", "011", "100", "101", "110"]
    print(solution.findDifferentBinaryString(nums5))  # Expected output: "0000000"

test_find_different_binary_string()