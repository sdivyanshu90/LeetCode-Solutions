class Solution:
    def arrangeWords(self, text: str) -> str:
        words = sorted(text.split(" "), key=len)
        if words:
            words[0] = words[0].capitalize()
            for i in range(1, len(words)):
                words[i] = words[i].lower()

        return " ".join(words)

def test_arrange_words():
    solution = Solution()

    # Test case 1
    text = "Leetcode is cool"
    print(solution.arrangeWords(text))  # Expected output: "Is cool leetcode"

    # Test case 2
    text = "Keep calm and code on"
    print(solution.arrangeWords(text))  # Expected output: "On and keep calm code"

    # Test case 3
    text = "To be or not to be"
    print(solution.arrangeWords(text))  # Expected output: "To be or to be not"

    # Test case 4
    text = "Hello"
    print(solution.arrangeWords(text))  # Expected output: "Hello"

    # Test case 5
    text = "A b C d E"
    print(solution.arrangeWords(text))  # Expected output: "A b c d e"

test_arrange_words()