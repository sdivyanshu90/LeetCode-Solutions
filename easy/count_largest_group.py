from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] += 1
        maxValue = max(hashMap.values())
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count

def test_count_largest_group():
    solution = Solution()

    # Test case 1
    n1 = 13
    print(solution.countLargestGroup(n1))  # Expected output: 4

    # Test case 2
    n2 = 2
    print(solution.countLargestGroup(n2))  # Expected output: 2

    # Test case 3
    n3 = 15
    print(solution.countLargestGroup(n3))  # Expected output: 6

    # Test case 4
    n4 = 24
    print(solution.countLargestGroup(n4))  # Expected output: 5

    # Test case 5
    n5 = 1000
    print(solution.countLargestGroup(n5))  # Expected output: 2

test_count_largest_group()