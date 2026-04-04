class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        res = [""]*len(words)

        for word in words:
            idx = int(word[-1]) - 1
            res[idx] = word[:-1]
        return " ".join(res)

def test_sort_sentence():
    solution = Solution()

    # Test case 1
    s1 = "is2 sentence4 This1 a3"
    print(solution.sortSentence(s1))  # Expected output: "This is a sentence"

    # Test case 2
    s2 = "Myself2 Me1 I4 and3"
    print(solution.sortSentence(s2))  # Expected output: "Me Myself and I"

    # Test case 3
    s3 = "Hello1"
    print(solution.sortSentence(s3))  # Expected output: "Hello"

    # Test case 4
    s4 = "a1b2c3d4e5f6g7h8i9j10"
    print(solution.sortSentence(s4))  # Expected output: "a1b2c3d4e5f6g7h8i9j1"

    # Test case 5
    s5 = "sentence4 This1 is2 a3"
    print(solution.sortSentence(s5))  # Expected output: "This is a sentence"

test_sort_sentence()