class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split(" ")])

def test_reverse_words():
    s = Solution()

    # Test case 1
    str1 = "Let's take LeetCode contest"
    print(s.reverseWords(str1)) # Expected output: "s'teL ekat edoCteeL tsetnoc"

    # Test case 2
    str2 = "Hello World"
    print(s.reverseWords(str2)) # Expected output: "olleH dlroW"

    # Test case 3
    str3 = "a b c d e"
    print(s.reverseWords(str3)) # Expected output: "a b c d e"

    # Test case 4
    str4 = "The quick brown fox"
    print(s.reverseWords(str4)) # Expected output: "ehT kciuq nworb xof"

    # Test case 5
    str5 = "Python is fun"
    print(s.reverseWords(str5)) # Expected output: "nohtyP si nuf"

test_reverse_words()