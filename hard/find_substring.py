from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = len(words) * word_length
        words_count = len(words)

        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1

        result = []
        for i in range(word_length):
            left, right = i, i
            seen = {}

            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length

                if word in word_freq:
                    seen[word] = seen.get(word, 0) + 1
                    while seen[word] > word_freq[word]:
                        seen[s[left:left + word_length]] -= 1
                        left += word_length

                    if right - left == total_length:
                        result.append(left)

                else:
                    seen.clear()
                    left = right

        return result

def test_find_substring():
    solution = Solution()

    # Test case 1: Basic case
    s1 = "barfoothefoobarman"
    words1 = ["foo","bar"]
    result1 = solution.findSubstring(s1, words1)
    print(result1)  # Expected output: [0, 9]

    # Test case 2: Overlapping words
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    result2 = solution.findSubstring(s2, words2)
    print(result2)  # Expected output: []

    # Test case 3: Words with different lengths
    s3 = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words3 = ["fooo","barr","wing","ding","wing"]
    result3 = solution.findSubstring(s3, words3)
    print(result3)  # Expected output: [13]

    # Test case 4: Empty string and non-empty words
    s4 = ""
    words4 = ["a","b"]
    result4 = solution.findSubstring(s4, words4)
    print(result4)  # Expected output: []

    # Test case 5: Non-empty string and empty words
    s5 = "abc"
    words5 = []
    result5 = solution.findSubstring(s5, words5)
    print(result5)  # Expected output: []

    # Test case 6: Single character words
    s6 = "aaaaaa"
    words6 = ["a","a","a"]
    result6 = solution.findSubstring(s6, words6)
    print(result6)  # Expected output: [0, 1, 2, 3]

    # Test case 7: No valid concatenation
    s7 = "abcdefg"
    words7 = ["hij","klm"]
    result7 = solution.findSubstring(s7, words7)
    print(result7)  # Expected output: []

    # Test case 8: All characters same in string and words
    s8 = "zzzzzzzz"
    words8 = ["zz","zz"]
    result8 = solution.findSubstring(s8, words8)
    print(result8)  # Expected output: [0, 2, 4, 1, 3]

    # Test case 9: Large input
    s9 = "a" * 10000 + "b" * 10000
    words9 = ["a" * 100, "b" * 100]
    result9 = solution.findSubstring(s9, words9)
    print(result9)  # Expected output: [9900]

    # Test case 10: Words with special characters
    s10 = "a!b@c#d$e%f^g&h*i(j)k"
    words10 = ["a!","b@","c#"]
    result10 = solution.findSubstring(s10, words10)
    print(result10)  # Expected output: [0]

test_find_substring()