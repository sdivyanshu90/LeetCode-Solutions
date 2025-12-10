class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        spl = sentence.split(" ")
        vowel = "aeiouAEIOU"
        for i in range(len(spl)):
            if spl[i][0] in vowel:
                spl[i] = spl[i] + "ma"
            else:
                spl[i] = spl[i][1:] + spl[i][0] + "ma"
            spl[i] = spl[i] + "a" * (i + 1)
        return " ".join(spl)

def test_to_goat_latin():
    solution = Solution()

    # Test Case 1
    sentence1 = "I speak Goat Latin"
    print(solution.toGoatLatin(sentence1)) # Expected: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

    # Test Case 2
    sentence2 = "The quick brown fox jumped over the lazy dog"
    print(solution.toGoatLatin(sentence2)) # Expected: "heTmaa uickqmaaa ownbrmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

    # Test Case 3
    sentence3 = "Each word consists of lowercase and uppercase letters only"
    print(solution.toGoatLatin(sentence3)) # Expected: "Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa andmaaaaaa uppercasemaaaaaa etterslmaaaaaaa onlymaaaaaaaa"

    # Test Case 4
    sentence4 = "Goat Latin is fun"
    print(solution.toGoatLatin(sentence4)) # Expected: "oatGmaa atinLmaaa ismaaaa unfmaaaaa"

    # Test Case 5
    sentence5 = "Hello World"
    print(solution.toGoatLatin(sentence5)) # Expected: "elloHmaa orldWmaaa"

test_to_goat_latin()