class Solution:
    def numSub(self, s: str) -> int:
        total_count = 0
        MOD = 10**9 + 7
        
        blocks = s.split('0')
        
        for block in blocks:
            k = len(block)
            if k > 0:
                contribution = (k * (k + 1)) // 2
                total_count = (total_count + contribution) % MOD
                
        return total_count

def test_num_sub():
    solution = Solution()

    # Test case 1
    s1 = "0110111"
    print(solution.numSub(s1))  # Expected output: 19

    # Test case 2
    s2 = "101"
    print(solution.numSub(s2))  # Expected output: 2

    # Test case 3
    s3 = "111111"
    print(solution.numSub(s3))  # Expected output: 21

    # Test case 4
    s4 = "0000"
    print(solution.numSub(s4))  # Expected output: 0

    # Test case 5
    s5 = "110100111"
    print(solution.numSub(s5))  # Expected output: 10

test_num_sub()