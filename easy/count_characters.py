from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsMap = {}
        result = 0
        for char in chars:
            if char not in charsMap:
                charsMap[char] = 1
            else:
                charsMap[char] += 1
        
        for word in words:
            charsMapCopy = charsMap.copy()
            end = True
            for char in word:
                if char in charsMapCopy and charsMapCopy[char] > 0:
                    charsMapCopy[char] -= 1
                else:
                    end = False
                    break
            if end:
                result += len(word)

        return result

def test_count_characters():
    solution = Solution()

    # Test Case 1
    words = ["cat","bt","hat","tree"]
    chars = "atach"
    print(solution.countCharacters(words, chars)) # Expected Output: 6

    # Test Case 2
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    print(solution.countCharacters(words, chars)) # Expected Output: 10

    # Test Case 3
    words = ["a","b","c","ab","bc","abc"]
    chars = "abc"
    print(solution.countCharacters(words, chars)) # Expected Output: 6

    # Test Case 4
    words = ["abcd","efgh","ijkl"]
    chars = "abcdefgh"
    print(solution.countCharacters(words, chars)) # Expected Output: 8

    # Test Case 5
    words = []
    chars = "anychars"
    print(solution.countCharacters(words, chars)) # Expected Output: 0

test_count_characters()