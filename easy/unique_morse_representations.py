from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = []
        for word in words:
            temp = ""
            for char in word:
                idx = ord(char) - ord('a')
                temp += table[idx]
            res.append(temp)
        return len(set(res))

def test_unique_morse_representations():
    solution = Solution()

    # Test Case 1
    words1 = ["gin","zen","gig","msg"]
    print(solution.uniqueMorseRepresentations(words1)) # Expected: 2

    # Test Case 2
    words2 = ["a"]
    print(solution.uniqueMorseRepresentations(words2)) # Expected: 1

    # Test Case 3
    words3 = ["hello","world"]
    print(solution.uniqueMorseRepresentations(words3)) # Expected: 2

    # Test Case 4
    words4 = ["abc","def","ghi"]
    print(solution.uniqueMorseRepresentations(words4)) # Expected: 3

    # Test Case 5
    words5 = ["aaaa","bbbb","cccc","dddd"]
    print(solution.uniqueMorseRepresentations(words5)) # Expected: 4

test_unique_morse_representations()