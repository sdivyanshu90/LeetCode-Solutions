class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        target_count = 1 << k
        
        if len(s) < target_count + k - 1:
            return False
            
        seen = [False] * target_count        
        all_ones = target_count - 1 
        hash_val = 0
        for i in range(len(s)):
            hash_val = ((hash_val << 1) & all_ones) | int(s[i])
            if i >= k - 1:
                if not seen[hash_val]:
                    seen[hash_val] = True
                    target_count -= 1
                    
                    if target_count == 0:
                        return True                        
        return False

def test_has_all_codes():
    solution = Solution()

    # Test case 1
    s = "00110110"
    k = 2
    print(solution.hasAllCodes(s, k))  # Expected output: True

    # Test case 2
    s = "0110"
    k = 1
    print(solution.hasAllCodes(s, k))  # Expected output: True

    # Test case 3
    s = "0110"
    k = 2
    print(solution.hasAllCodes(s, k))  # Expected output: False

    # Test case 4
    s = "0000000001011100"
    k = 4
    print(solution.hasAllCodes(s, k))  # Expected output: False

    # Test case 5
    s = "0000000001011100"
    k = 3
    print(solution.hasAllCodes(s, k))  # Expected output: True

test_has_all_codes()