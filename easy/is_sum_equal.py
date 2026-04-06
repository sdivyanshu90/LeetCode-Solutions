class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabet = {chr(i + ord('a')): i for i in range(26)}
        
        def word_to_number(word, alphabet):
            return int("".join(str(alphabet[char]) for char in word if char in alphabet))

        return word_to_number(firstWord, alphabet) + word_to_number(secondWord, alphabet) == word_to_number(targetWord, alphabet)

def test_is_sum_equal():
    solution = Solution()

    # Test case 1
    firstWord1 = "acb"
    secondWord1 = "cba"
    targetWord1 = "cdb"
    print(solution.isSumEqual(firstWord1, secondWord1, targetWord1))  # Expected output: True

    # Test case 2
    firstWord2 = "aaa"
    secondWord2 = "a"
    targetWord2 = "aaaa"
    print(solution.isSumEqual(firstWord2, secondWord2, targetWord2))  # Expected output: True

    # Test case 3
    firstWord3 = "aaa"
    secondWord3 = "a"
    targetWord3 = "aaaaa"
    print(solution.isSumEqual(firstWord3, secondWord3, targetWord3))  # Expected output: True

    # Test case 4
    firstWord4 = "abc"
    secondWord4 = "def"
    targetWord4 = "abd"
    print(solution.isSumEqual(firstWord4, secondWord4, targetWord4))  # Expected output: False

    # Test case 5
    firstWord5 = "abc"
    secondWord5 = "def"
    targetWord5 = "abcde"
    print(solution.isSumEqual(firstWord5, secondWord5, targetWord5))  # Expected output: False

test_is_sum_equal()