from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def normalize_vowels(word: str) -> str:
            return "".join('*' if ch in vowels else ch for ch in word.lower())
        
        exact = set(wordlist)
        lower_map = {}
        vowel_map = {}
        
        for w in wordlist:
            lw = w.lower()
            vw = normalize_vowels(w)
            lower_map.setdefault(lw, w)
            vowel_map.setdefault(vw, w)
        
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lw = q.lower()
            if lw in lower_map:
                ans.append(lower_map[lw])
                continue
            vw = normalize_vowels(q)
            if vw in vowel_map:
                ans.append(vowel_map[vw])
                continue
            ans.append("")
        
        return ans

def test_spellchecker():
    solution = Solution()

    # Test case 1
    wordlist1 = ["KiTe","kite","hare","Hare"]
    queries1 = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    print(solution.spellchecker(wordlist1, queries1))  
    # Expected output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","",""]

    # Test case 2
    wordlist2 = ["yellow","YellOw"]
    queries2 = ["YellOw","yellow","YELLOW","yellOw","yeLLoW"]
    print(solution.spellchecker(wordlist2, queries2))  
    # Expected output: ["YellOw","yellow","yellow","YellOw","YellOw"]

    # Test case 3
    wordlist3 = ["apple"]
    queries3 = ["Apple","aPPle","applE","APple"]
    print(solution.spellchecker(wordlist3, queries3))  
    # Expected output: ["apple","apple","apple","apple"]

    # Test case 4
    wordlist4 = ["banana"]
    queries4 = ["BANANA","Banana","bAnAnA"]
    print(solution.spellchecker(wordlist4, queries4))  
    # Expected output: ["banana","banana","banana"]

    # Test case 5
    wordlist5 = ["orange"]
    queries5 = ["orAnge","ORANGE","oRaNgE"]
    print(solution.spellchecker(wordlist5, queries5))  
    # Expected output: ["orange","orange","orange"]

test_spellchecker()