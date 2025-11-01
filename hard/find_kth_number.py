class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1

        while k > 0:
            step = self._count_steps(n, curr, curr + 1)
            if step <= k:
                curr += 1
                k -= step
            else:
                curr *= 10
                k -= 1
        return curr

    def _count_steps(self, n, prefix1, prefix2):
        steps = 0
        while prefix1 <= n:
            steps += min(n + 1, prefix2) - prefix1
            prefix1 *= 10
            prefix2 *= 10
        return steps

def test_find_kth_number():
    s = Solution()

    # Test case 1
    n = 13
    k = 2
    print(s.findKthNumber(n, k))  # Expected output: 10

    # Test case 2
    n = 100
    k = 10
    print(s.findKthNumber(n, k))  # Expected output: 17

    # Test case 3
    n = 1000
    k = 100
    print(s.findKthNumber(n, k))  # Expected output: 188

    # Test case 4
    n = 10
    k = 5
    print(s.findKthNumber(n, k))  # Expected output: 4

    # Test case 5
    n = 10000
    k = 1000
    print(s.findKthNumber(n, k))  # Expected output: 1878

test_find_kth_number()