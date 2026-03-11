class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  
        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)

def test_make_good():
    solution = Solution()

    # Test case 1
    s1 = "leEeetcode"
    print(solution.makeGood(s1))  # Expected output: "leetcode"

    # Test case 2
    s2 = "abBAcC"
    print(solution.makeGood(s2))  # Expected output: ""

    # Test case 3
    s3 = "s"
    print(solution.makeGood(s3))  # Expected output: "s"

    # Test case 4
    s4 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(solution.makeGood(s4))  # Expected output: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Test case 5
    s5 = "aAbBcCdD"
    print(solution.makeGood(s5))  # Expected output: ""

test_make_good()