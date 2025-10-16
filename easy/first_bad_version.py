_BAD_VERSION = 0

def isBadVersion(version: int) -> bool:
    global _BAD_VERSION
    return version >= _BAD_VERSION

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        
        return left

def test_first_bad_version():

    s = Solution()
    global _BAD_VERSION

    # Test Case 1
    _BAD_VERSION = 4
    n = 5
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 4

    # Test Case 2: Edge case, the last version is the first bad one
    _BAD_VERSION = 50
    n = 50
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 50

    # Test Case 3: Edge case, the first version is bad
    _BAD_VERSION = 1
    n = 100
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 1

    # Test Case 4: Minimal case, two versions, second is bad
    _BAD_VERSION = 2
    n = 2
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 2

    # Test Case 5: Minimal case, two versions, first is bad
    _BAD_VERSION = 1
    n = 2
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 1

    # Test Case 6: The smallest possible input
    _BAD_VERSION = 1
    n = 1
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 1

    # Test Case 7: Odd number of versions, bad version after midpoint
    _BAD_VERSION = 8
    n = 13
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 8

    # Test Case 8: Even number of versions, bad version is the first midpoint
    _BAD_VERSION = 10
    n = 20
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 10

    # Test Case 9: Large numbers to test performance and correctness
    _BAD_VERSION = 1702766719
    n = 2126753390
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 1702766719

    # Test Case 10: Small even number of versions, bad in the first half
    _BAD_VERSION = 3
    n = 6
    print(f"n = {n}, bad = {_BAD_VERSION}, result = {s.firstBadVersion(n)}") # Expected: 3

test_first_bad_version()