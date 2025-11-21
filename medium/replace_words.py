from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_array = sentence.split()
        dict_set = set(dictionary)

        def shortest_root(word, dict_set):
            for i in range(len(word)):
                root = word[0:i]
                if root in dict_set:
                    return root
            return word

        for word in range(len(word_array)):
            word_array[word] = shortest_root(word_array[word], dict_set)
        return " ".join(word_array)

def test_replace_words():
    s = Solution()

    # Test case 1
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(s.replaceWords(dictionary, sentence))  # Expected output: "the cat was rat by the bat"

    # Test case 2
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(s.replaceWords(dictionary, sentence))  # Expected output: "a a b c"

    # Test case 3
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "aaaaa aa aaa a abcd"
    print(s.replaceWords(dictionary, sentence))  # Expected output: "a a a a a"

    # Test case 4
    dictionary = ["catt", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(s.replaceWords(dictionary, sentence))  # Expected output: "the catt was rat by the bat"

    # Test case 5
    dictionary = ["ac", "ab"]
    sentence = "it is abnormal that this solution is accepted"
    print(s.replaceWords(dictionary, sentence))  # Expected output: "it is ab that this solution is ac"

test_replace_words()