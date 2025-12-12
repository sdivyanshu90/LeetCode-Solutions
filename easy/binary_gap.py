class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        idx = []
        res = 0
        for i in range(len(bin_n)):
            if bin_n[i] == "1":
                idx.append(i)
        
        for i in range(1, len(idx)):
            res = max(res, idx[i] - idx[i - 1])
        return res

        # Method 2
        # last = -1
        # max_gap = 0
        # index = 0
        
        # while n > 0:
        #     if n & 1:
        #         if last != -1:
        #             max_gap = max(max_gap, index - last)
        #         last = index
        #     n >>= 1
        #     index += 1
        
        # return max_gap

def test_binaryGap():
    solution = Solution()
    
    # Test Case 1
    print(solution.binaryGap(22)) # Expected: 2

    # Test Case 2
    print(solution.binaryGap(5)) # Expected: 2

    # Test Case 3
    print(solution.binaryGap(6)) # Expected: 1

    # Test Case 4
    print(solution.binaryGap(8)) # Expected: 0

    # Test Case 5
    print(solution.binaryGap(1)) # Expected: 0

test_binaryGap()