class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0
        
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1
        
        return min(start0, start1)

def test_min_operations():
    solution = Solution()

    # Test Case 1
    s1 = "0100"
    print(solution.minOperations(s1)) # Expected Output: 1

    # Test Case 2
    s2 = "10"
    print(solution.minOperations(s2)) # Expected Output: 0

    # Test Case 3
    s3 = "1111"
    print(solution.minOperations(s3)) # Expected Output: 2

    # Test Case 4
    s4 = "0000"
    print(solution.minOperations(s4)) # Expected Output: 2

    # Test Case 5
    s5 = "001001001110"
    print(solution.minOperations(s5)) # Expected Output: 5

test_min_operations()