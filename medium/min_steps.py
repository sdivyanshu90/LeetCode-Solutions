class Solution:
    def __init__(self):
        self.n = 0

    def _min_steps_helper(self, curr_len, paste_len):
        if curr_len == self.n:
            return 0
        if curr_len > self.n:
            return 1000
        opt1 = 2 + self._min_steps_helper(curr_len * 2, curr_len)
        opt2 = 1 + self._min_steps_helper(curr_len + paste_len, paste_len)
        return min(opt1, opt2)

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n = n
        return 1 + self._min_steps_helper(1, 1)

def test_min_steps():
    s = Solution()

    # Test case 1
    n = 1
    print(s.minSteps(n))  # Expected output: 0

    # Test case 2
    n = 2
    print(s.minSteps(n))  # Expected output: 2

    # Test case 3
    n = 3
    print(s.minSteps(n))  # Expected output: 3

    # Test case 4
    n = 4
    print(s.minSteps(n))  # Expected output: 4

    # Test case 5
    n = 5
    print(s.minSteps(n))  # Expected output: 5

test_min_steps()