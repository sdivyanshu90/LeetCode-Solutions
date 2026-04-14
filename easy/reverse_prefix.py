class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx != -1:
            return word[idx::-1] + word[idx + 1:]
        return word

def test_reverse_prefix():
    solution = Solution()

    # Test case 1
    word1 = "abcdefd"
    ch1 = "d"
    print(solution.reversePrefix(word1, ch1))  # Expected output: "dcbaefd"

    # Test case 2
    word2 = "xyxzxe"
    ch2 = "z"
    print(solution.reversePrefix(word2, ch2))  # Expected output: "zxyxxe"

    # Test case 3
    word3 = "abcd"
    ch3 = "z"
    print(solution.reversePrefix(word3, ch3))  # Expected output: "abcd"

    # Test case 4
    word4 = "abcdefghijklmnopqrstuvwxyz"
    ch4 = "a"
    print(solution.reversePrefix(word4, ch4))  # Expected output: "abcdefghijklmnopqrstuvwxyz"

    # Test case 5
    word5 = "hello"
    ch5 = "o"
    print(solution.reversePrefix(word5, ch5))  # Expected output: "olleh"

test_reverse_prefix()