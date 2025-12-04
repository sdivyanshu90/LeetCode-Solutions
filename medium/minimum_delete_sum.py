# Approach 1: Using Dynamic Programming

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        total_ascii_s1 = sum(ord(ch) for ch in s1)
        total_ascii_s2 = sum(ord(ch) for ch in s2)        
        return total_ascii_s1 + total_ascii_s2 - 2 * dp[m][n]

# Approach 2: Using Recursion with Memoization
# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         result = {}

#         def ascii_cost(i, j):
#             if i < 0 and j < 0:
#                 return 0
#             if (i, j) in result:
#                 return result[(i, j)]
#             if i < 0:
#                 result[(i, j)] = ord(s2[j]) + ascii_cost(i, j - 1)
#                 return result[(i, j)]
#             if j < 0:
#                 result[(i, j)] = ord(s1[i]) + ascii_cost(i - 1, j)
#                 return result[(i, j)]
#             if s1[i] == s2[j]:
#                 result[(i, j)] = ascii_cost(i - 1, j - 1)
#             else:
#                 result[(i, j)] = min(
#                     ord(s1[i]) + ascii_cost(i - 1, j),
#                     ord(s2[j]) + ascii_cost(i, j - 1)
#                 )
#             return result[(i, j)]
#         return ascii_cost(len(s1) - 1, len(s2) - 1)

def test_minimum_delete_sum():
    solution = Solution()

    # Test Case 1
    s1 = "sea"
    s2 = "eat"
    print(solution.minimumDeleteSum(s1, s2))  # Expected: 231

    # Test Case 2
    s1 = "delete"
    s2 = "leet"
    print(solution.minimumDeleteSum(s1, s2))  # Expected: 403

    # Test Case 3: Both strings are empty
    s1 = ""
    s2 = ""
    print(solution.minimumDeleteSum(s1, s2))  # Expected: 0

    # Test Case 4: One string is empty
    s1 = "abc"
    s2 = ""
    print(solution.minimumDeleteSum(s1, s2))  # Expected: 294 (ASCII sum of 'a', 'b', 'c')

    # Test Case 5: No common characters
    s1 = "abc"
    s2 = "def"
    print(solution.minimumDeleteSum(s1, s2))  # Expected: 597 (ASCII sum of 'a', 'b', 'c', 'd', 'e', 'f')

test_minimum_delete_sum()