class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and k>0 and stack[-1] > n:
                stack.pop()
                k -= 1
            if stack or n != '0': 
                stack.append(n)       
        if k:
            stack=stack[0:-k]     
        return ''.join(stack) or '0'

def test_remove_k_digits():
    s = Solution()

    # Test case 1
    print(s.removeKdigits("1432219", 3))  # Expected output: "1219"

    # Test case 2
    print(s.removeKdigits("10200", 1))    # Expected output: "200"

    # Test case 3
    print(s.removeKdigits("10", 2))       # Expected output: "0"

    # Test case 4
    print(s.removeKdigits("1234567890", 9))  # Expected output: "0"

    # Test case 5
    print(s.removeKdigits("9", 1))        # Expected output: "0"

    # Test case 6
    print(s.removeKdigits("112", 1))      # Expected output: "11"

    # Test case 7
    print(s.removeKdigits("100200", 1))   # Expected output: "200"

    # Test case 8
    print(s.removeKdigits("765028321", 5)) # Expected output: "221"

    # Test case 9
    print(s.removeKdigits("54321", 2))    # Expected output: "321"

    # Test case 10
    print(s.removeKdigits("1000", 1))     # Expected output: "0"

test_remove_k_digits()