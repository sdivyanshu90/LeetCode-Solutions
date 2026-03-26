class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        n1, n2 = len(word1), len(word2)
        max_len = max(n1, n2)

        for i in range(max_len):
            if i < n1:
                res.append(word1[i])
            if i < n2:
                res.append(word2[i])

        return ''.join(res)

def test_merge_alternately():
    solution = Solution()

    # Test Case 1
    word1 = "abc"
    word2 = "pqr"
    print(solution.mergeAlternately(word1, word2)) # Expected Output: "apbqcr"

    # Test Case 2
    word1 = "ab"
    word2 = "pqrs"
    print(solution.mergeAlternately(word1, word2)) # Expected Output: "apbqrs"

    # Test Case 3
    word1 = "abcd"
    word2 = "pq"
    print(solution.mergeAlternately(word1, word2)) # Expected Output: "apbqcd"

    # Test Case 4
    word1 = ""
    word2 = "xyz"
    print(solution.mergeAlternately(word1, word2)) # Expected Output: "xyz"

    # Test Case 5
    word1 = "hello"
    word2 = "abcd"
    print(solution.mergeAlternately(word1, word2)) # Expected Output: "habcldlo"

test_merge_alternately()