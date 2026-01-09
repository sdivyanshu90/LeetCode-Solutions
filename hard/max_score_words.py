from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        W = len(words)
        self.max_score = 0
        freq = [0 for i in range(26)]
        subset_letters = [0 for i in range(26)]
        for c in letters:
            freq[ord(c) - 97] += 1

        def is_valid_word(subset_letters):
            for c in range(26):
                if freq[c] < subset_letters[c]:
                    return False
            else:
                return True
        
        def check(w, words, score, subset_letters, total_score):
            if w == -1:
                self.max_score = max(self.max_score, total_score)
                return
            check(w - 1, words, score, subset_letters, total_score)
            L = len(words[w])
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] += 1
                total_score += score[c]

            if is_valid_word(subset_letters):
                check(w - 1, words, score, subset_letters, total_score)
                
            for i in range(L):
                c = ord(words[w][i]) - 97
                subset_letters[c] -= 1
                total_score -= score[c]

        check(W - 1, words, score, subset_letters, 0)
        return self.max_score

def test_max_score_words():
    solution = Solution()

    # Test case 1
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 23

    # Test case 2
    words = ["xxxz","ax","bx","cx"]
    letters = ["z","a","b","c","x","x","x"]
    score = [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 27

    # Test case 3
    words = ["leetcode"]
    letters = ["l","e","t","c","o","d"]
    score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 0

    # Test case 4
    words = ["a","b","c"]
    letters = ["a","b","c"]
    score = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 6

    # Test case 5
    words = ["hello","world","leetcode"]
    letters = ["l","e","o","l","h","d","r","w","o"]
    score = [4,2,3,5,1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    print(solution.maxScoreWords(words, letters, score))  # Expected output: 30

test_max_score_words()