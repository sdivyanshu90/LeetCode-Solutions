class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, s in enumerate(sentence.split(" ")) :
            if s.startswith(searchWord) :
                return i + 1
        return -1

def test_is_prefix_of_word():
    solution = Solution()

    # Test case 1
    sentence = "i love eating burger"
    searchWord = "burg"
    print(solution.isPrefixOfWord(sentence, searchWord))  # Expected output: 4

    # Test case 2
    sentence = "this problem is an easy problem"
    searchWord = "pro"
    print(solution.isPrefixOfWord(sentence, searchWord))  # Expected output: 2

    # Test case 3
    sentence = "i am tired"
    searchWord = "you"
    print(solution.isPrefixOfWord(sentence, searchWord))  # Expected output: -1

    # Test case 4
    sentence = "hello world"
    searchWord = "hello"
    print(solution.isPrefixOfWord(sentence, searchWord))  # Expected output: 1

    # Test case 5
    sentence = "a quick brown fox"
    searchWord = "qu"
    print(solution.isPrefixOfWord(sentence, searchWord))  # Expected output: 2

test_is_prefix_of_word()