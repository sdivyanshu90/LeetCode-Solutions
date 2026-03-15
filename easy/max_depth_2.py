class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max_num = 0
        for i in s:
            if i == "(":
                count += 1
                if max_num < count:
                    max_num = count
            if i == ")":
                count -= 1
        return(max_num)

def test_max_depth():
    solution = Solution()

    # Test case 1
    s = "(1+(2*3)+((8)/4))+1"
    print(solution.maxDepth(s))  # Expected output: 3

    # Test case 2
    s = "(1)+((2))+(((3)))"
    print(solution.maxDepth(s))  # Expected output: 3

    # Test case 3
    s = "1+(2*3)/(2-1)"
    print(solution.maxDepth(s))  # Expected output: 1

    # Test case 4
    s = "1"
    print(solution.maxDepth(s))  # Expected output: 0

    # Test case 5
    s = "(((((1+2)+3)+4)+5)+6)+7)+8)+9)"
    print(solution.maxDepth(s))  # Expected output: 6

test_max_depth()