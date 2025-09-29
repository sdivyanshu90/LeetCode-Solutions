from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        leftMax = rightMax = trap_water = 0
        left = 0
        right = n - 1
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    trap_water += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    trap_water += rightMax - height[right]
                right -= 1
        return trap_water

def test_trap():
    solution = Solution()
    
    # Test case 1: Regular case with multiple bars
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Expected output: 6
    
    # Test case 2: No bars
    print(solution.trap([]))  # Expected output: 0

    # Test case 3: Single bar
    print(solution.trap([4]))  # Expected output: 0

    # Test case 4: Two bars
    print(solution.trap([4,2]))  # Expected output: 0

    # Test case 5: Three bars with trapping
    print(solution.trap([4,2,3]))  # Expected output: 1

    # Test case 6: All bars of same height
    print(solution.trap([3,3,3,3]))  # Expected output: 0

    # Test case 7: Increasing heights
    print(solution.trap([1,2,3,4,5]))  # Expected output: 0

    # Test case 8: Decreasing heights
    print(solution.trap([5,4,3,2,1]))  # Expected output: 0

    # Test case 9: Large input with random heights
    print(solution.trap([0,2,0,4,0,3,0,5,0,1]))  # Expected output: 12

    # Test case 10: Complex pattern
    print(solution.trap([5,2,1,2,1,5]))  # Expected output: 14

test_trap()