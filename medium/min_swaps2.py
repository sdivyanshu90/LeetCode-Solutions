class Solution:
    def minSwaps(self, s: str) -> int:
        stack = deque()
        unbalanced = 0
        for ch in s:
            if ch == "[":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalanced += 1
        return (unbalanced + 1) // 2

def test_min_swaps():
    solution = Solution()

    # Test Case 1
    s1 = "]]][[["
    print(solution.minSwaps(s1))  # Expected output: 3

    # Test Case 2
    s2 = "[]"
    print(solution.minSwaps(s2))  # Expected output: 0

    # Test Case 3
    s3 = "[][]"
    print(solution.minSwaps(s3))  # Expected output: 0

    # Test Case 4
    s4 = "]]][["
    print(solution.minSwaps(s4))  # Expected output: 2

    # Test Case 5
    s5 = "[[[]]"
    print(solution.minSwaps(s5))  # Expected output: 1

test_min_swaps()