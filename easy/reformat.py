class Solution:
    def reformat(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        digits = [ch for ch in s if ch.isdigit()]
        
        if abs(len(letters) - len(digits)) > 1:
            return ""
        
        if len(letters) < len(digits):
            letters, digits = digits, letters
        
        result = []
        for i in range(len(s)):
            if i % 2 == 0:
                result.append(letters.pop())
            else:
                result.append(digits.pop())
        
        return ''.join(result)

def test_reformat():
    solution = Solution()

    # Test case 1
    s1 = "a0b1c2"
    print(solution.reformat(s1))  # Expected output: "a0b1c2" or "0a1b2c"

    # Test case 2
    s2 = "leetcode"
    print(solution.reformat(s2))  # Expected output: ""

    # Test case 3
    s3 = "1229857369"
    print(solution.reformat(s3))  # Expected output: ""

    # Test case 4
    s4 = "covid2019"
    print(solution.reformat(s4))  # Expected output: "c2o0v1i9d" or similar

    # Test case 5
    s5 = "ab123"
    print(solution.reformat(s5))  # Expected output: "a1b23"

test_reformat()