class Solution:

    class TrieNode:
        def __init__(self):
            self.frequency = 0
            self.child_nodes = {}

    def stringMatching(self, words: List[str]) -> List[str]:
        matching_words = []
        root = self.TrieNode()

        for word in words:
            for start_index in range(len(word)):
                self._insert_word(root, word[start_index:])

        for word in words:
            if self._is_substring(root, word):
                matching_words.append(word)

        return matching_words

    def _insert_word(self, root: "TrieNode", word: str) -> None:
        current_node = root
        for char in word:
            if char not in current_node.child_nodes:
                current_node.child_nodes[char] = self.TrieNode()
            current_node = current_node.child_nodes[char]
            current_node.frequency += 1

    def _is_substring(self, root: "TrieNode", word: str) -> bool:
        current_node = root
        for char in word:
            current_node = current_node.child_nodes[char]
        return current_node.frequency > 1

def test_string_matching():
    solution = Solution()

    # Test case 1
    words1 = ["mass", "as", "hero", "superhero"]
    print(solution.stringMatching(words1))  # Expected output: ["as", "hero"]

    # Test case 2
    words2 = ["leetcode", "et", "code"]
    print(solution.stringMatching(words2))  # Expected output: ["et", "code"]

    # Test case 3
    words3 = ["blue", "green", "bu"]
    print(solution.stringMatching(words3))  # Expected output: []

    # Test case 4
    words4 = ["a", "b", "c"]
    print(solution.stringMatching(words4))  # Expected output: []

    # Test case 5
    words5 = ["leetcoder", "leetcode", "od", "hamlet", "am"]
    print(solution.stringMatching(words5))  # Expected output: ["leetcode", "od", "am"]

test_string_matching()