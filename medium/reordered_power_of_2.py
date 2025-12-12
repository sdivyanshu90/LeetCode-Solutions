class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted(str(n))
        for i in range(31):
            if sorted(str(1 << i)) == target:
                return True
        return False

def test_reorderedPowerOf2():
    solution = Solution()
    
    # Test Case 1
    print(solution.reorderedPowerOf2(1)) # Expected: True

    # Test Case 2
    print(solution.reorderedPowerOf2(10)) # Expected: False

    # Test Case 3
    print(solution.reorderedPowerOf2(16)) # Expected: True

    # Test Case 4
    print(solution.reorderedPowerOf2(24)) # Expected: False

    # Test Case 5
    print(solution.reorderedPowerOf2(46)) # Expected: True

test_reorderedPowerOf2()