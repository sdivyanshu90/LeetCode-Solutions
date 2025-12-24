from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        word_to_length = {}

        for word in words:
            longest_chain_length = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1:]
                if prev_word in word_to_length:
                    longest_chain_length = max(longest_chain_length, word_to_length[prev_word] + 1)

            word_to_length[word] = longest_chain_length

        return max(word_to_length.values())

def test_longest_str_chain():
    solution = Solution()

    # Test case 1
    words = ["a","b","ba","bca","bda","bdca"]
    print(solution.longestStrChain(words))  # Expected output: 4

    # Test case 2
    words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
    print(solution.longestStrChain(words))  # Expected output: 5

    # Test case 3
    words = ["abcd","dbqca"]
    print(solution.longestStrChain(words))  # Expected output: 1

    # Test case 4
    words = ["a","ab","ac","bd","abc","abd","abdd"]
    print(solution.longestStrChain(words))  # Expected output: 4

    # Test case 5
    words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh"]
    print(solution.longestStrChain(words))  # Expected output: 7

test_longest_str_chain()