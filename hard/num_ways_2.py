class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 1000000007
        word_length = len(words[0])
        target_length = len(target)
        char_frequency = [[0] * 26 for _ in range(word_length)]

        for word in words:
            for j in range(word_length):
                char_frequency[j][ord(word[j]) - ord("a")] += 1

        prev_count = [0] * (target_length + 1)
        curr_count = [0] * (target_length + 1)

        prev_count[0] = 1

        for curr_word in range(1, word_length + 1):
            curr_count = prev_count.copy()
            for curr_target in range(1, target_length + 1):
                cur_pos = ord(target[curr_target - 1]) - ord("a")

                curr_count[curr_target] += (
                    char_frequency[curr_word - 1][cur_pos]
                    * prev_count[curr_target - 1]
                ) % MOD
                curr_count[curr_target] %= MOD

            prev_count = curr_count.copy()

        return curr_count[target_length]

def test_num_ways():
    solution = Solution()

    # Test case 1
    words1 = ["acca", "bbbb", "caca"]
    target1 = "aba"
    print(solution.numWays(words1, target1))  # Expected output: 6

    # Test case 2
    words2 = ["abba", "baab"]
    target2 = "bab"
    print(solution.numWays(words2, target2))  # Expected output: 4

    # Test case 3
    words3 = ["abcd"]
    target3 = "abcd"
    print(solution.numWays(words3, target3))  # Expected output: 1

    # Test case 4
    words4 = ["abab", "baba", "abba", "baab"]
    target4 = "abba"
    print(solution.numWays(words4, target4))  # Expected output: 16

    # Test case 5
    words5 = ["abc", "def", "ghi"]
    target5 = "xyz"
    print(solution.numWays(words5, target5))  # Expected output: 0

test_num_ways()