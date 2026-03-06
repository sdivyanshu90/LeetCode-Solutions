class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = list(s)
        for i in range(len(s)):
            res[indices[i]] = s[i]
        return "".join(res)

def test_restore_string():
    solution = Solution()

    # Test case 1
    s1 = "codeleet"
    indices1 = [4, 5, 6, 7, 0, 2, 1, 3]
    print(solution.restoreString(s1, indices1))  # Expected output: "leetcode"

    # Test case 2
    s2 = "abc"
    indices2 = [0, 1, 2]
    print(solution.restoreString(s2, indices2))  # Expected output: "abc"

    # Test case 3
    s3 = "aiohn"
    indices3 = [3, 1, 4, 2, 0]
    print(solution.restoreString(s3, indices3))  # Expected output: "nihao"

    # Test case 4
    s4 = "aaiougrt"
    indices4 = [4, 0, 2, 6, 7, 3, 1, 5]
    print(solution.restoreString(s4, indices4))  # Expected output: "arigatou"

    # Test case 5
    s5 = "art"
    indices5 = [1, 0, 2]
    print(solution.restoreString(s5, indices5))  # Expected output: "rat"

test_restore_string()