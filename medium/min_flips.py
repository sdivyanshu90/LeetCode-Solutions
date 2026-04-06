class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)        
        s = s + s 
        alt1 = ""
        alt2 = ""
        for i in range(len(s)):
            alt1 += "0" if i % 2 == 0 else "1"
            alt2 += "1" if i % 2 == 0 else "0"
            
        res = float('inf')
        diff1 = 0
        diff2 = 0
        
        left = 0
        
        for right in range(len(s)):
            if s[right] != alt1[right]: diff1 += 1
            if s[right] != alt2[right]: diff2 += 1
            
            if right - left + 1 > n:
                if s[left] != alt1[left]: diff1 -= 1
                if s[left] != alt2[left]: diff2 -= 1
                left += 1 
                
            if right - left + 1 == n:
                res = min(res, diff1, diff2)
                
        return res

def test_min_flips():
    solution = Solution()

    # Test case 1
    s1 = "111000"
    print(solution.minFlips(s1))  # Expected output: 2

    # Test case 2
    s2 = "010"
    print(solution.minFlips(s2))  # Expected output: 0

    # Test case 3
    s3 = "1110"
    print(solution.minFlips(s3))  # Expected output: 1

    # Test case 4
    s4 = "0000"
    print(solution.minFlips(s4))  # Expected output: 2

    # Test case 5
    s5 = "101010"
    print(solution.minFlips(s5))  # Expected output: 0

test_min_flips()