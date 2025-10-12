class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        d1 = [int(i) for i in version1.split(".")]
        d2 = [int(i) for i in version2.split(".")]
        while len(d1) > len(d2): d2.append(0)
        while len(d2) > len(d1): d1.append(0)

        for i in range(len(d1)):
            if d1[i] < d2[i]: return -1
            elif d2[i] < d1[i]: return 1
        return 0

def test_compare_version():
    s = Solution()

    # Test Case 1: Basic greater than
    print(s.compareVersion("1.2", "1.1")) # Expected Output: 1

    # Test Case 2: Basic less than
    print(s.compareVersion("7.5.2", "7.5.3")) # Expected Output: -1

    # Test Case 3: Equal versions
    print(s.compareVersion("1.0.1", "1.0.1")) # Expected Output: 0

    # Test Case 4: Trailing zeros ignored (Equality)
    print(s.compareVersion("1.0", "1")) # Expected Output: 0

    # Test Case 5: Unequal number of revisions (v1 > v2)
    print(s.compareVersion("1.0.1", "1.0")) # Expected Output: 1

    # Test Case 6: Unequal number of revisions (v1 < v2)
    print(s.compareVersion("0.1", "1.1")) # Expected Output: -1

    # Test Case 7: Leading zeros ignored (Equality)
    print(s.compareVersion("1.01", "1.1")) # Expected Output: 0

    # Test Case 8: Multi-digit revisions
    print(s.compareVersion("1.10", "1.2")) # Expected Output: 1

    # Test Case 9: All zero versions
    print(s.compareVersion("0.0.0", "0.0")) # Expected Output: 0

    # Test Case 10: Complex case with mixed numbers and lengths
    print(s.compareVersion("1.0.0.5", "1.0.1")) # Expected Output: -1

test_compare_version()