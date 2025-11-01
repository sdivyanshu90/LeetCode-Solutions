class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for char in s:
            if freq.get(char):
                freq[char] += 1
            else:
                freq[char] = 1
        
        sorted_chars = sorted(freq, key = lambda x: freq[x], reverse=True)

        return ''.join([char * freq[char] for char in sorted_chars])

def test_frequency_sort():
    s = Solution()

    # Test case 1
    string = "tree"
    print(s.frequencySort(string))  # Expected output: "eetr"

    # Test case 2
    string = "cccaaa"
    print(s.frequencySort(string))  # Expected output: "cccaaa"

    # Test case 3
    string = "Aabb"
    print(s.frequencySort(string))  # Expected output: "bbAa"

    # Test case 4
    string = "rat"
    print(s.frequencySort(string))  # Expected output: "rat"

    # Test case 5
    string = "ababab"
    print(s.frequencySort(string))  # Expected output: "aaabbb"

test_frequency_sort()