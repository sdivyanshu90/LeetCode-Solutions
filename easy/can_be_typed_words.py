class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split(" "):
            if not any(letter in word for letter in brokenLetters):
                count += 1

        return count

def test_can_be_typed_words():
    solution = Solution()

    # Test case 1
    text1 = "hello world"
    brokenLetters1 = "ad"
    print(solution.canBeTypedWords(text1, brokenLetters1))  # Expected output: 1

    # Test case 2
    text2 = "leet code"
    brokenLetters2 = "lt"
    print(solution.canBeTypedWords(text2, brokenLetters2))  # Expected output: 1

    # Test case 3
    text3 = "leet code"
    brokenLetters3 = "e"
    print(solution.canBeTypedWords(text3, brokenLetters3))  # Expected output: 0

    # Test case 4
    text4 = "hello world"
    brokenLetters4 = "xyz"
    print(solution.canBeTypedWords(text4, brokenLetters4))  # Expected output: 2

    # Test case 5
    text5 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    brokenLetters5 = "aeiou"
    print(solution.canBeTypedWords(text5, brokenLetters5))  # Expected output: 21

test_can_be_typed_words()