from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:  
        if not digits:
            return []
        
        Map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        ans = []
        path = []
        
        def backtrack(i):
            if i == len(digits):
                ans.append(''.join(path))
                return
            
            for char in Map[digits[i]]:
                path.append(char)
                backtrack(i+1)
                path.pop()
                
        backtrack(0)
        return ans

def test_letter_combinations():
    solution = Solution()

    # Test case 1
    digits = "23"
    print(solution.letterCombinations(digits))  # Expected output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    # Test case 2
    digits = ""
    print(solution.letterCombinations(digits))  # Expected output: []

    # Test case 3
    digits = "2"
    print(solution.letterCombinations(digits))  # Expected output: ["a","b","c"]

    # Test case 4
    digits = "7"
    print(solution.letterCombinations(digits))  # Expected output: ["p","q","r","s"]

    # Test case 5
    digits = "9"
    print(solution.letterCombinations(digits))  # Expected output: ["w","x","y","z"]

    # Test case 6
    digits = "79"
    print(solution.letterCombinations(digits))  # Expected output: ["pw","px","py","pz","qw","qx","qy","qz","rw","rx","ry","rz","sw","sx","sy","sz"]

    # Test case 7
    digits = "234"
    print(solution.letterCombinations(digits))  # Expected output: ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]

    # Test case 8
    digits = "2345"
    print(solution.letterCombinations(digits))  # Expected output: ['adgj', 'adgk', 'adgl', 'adhj', 'adhk', 'adhl', 'adij', 'adik', 'adil', 'aegj', 'aegk', 'aegl', 'aehj', 'aehk', 'aehl', 'aeij', 'aeik', 'aeil', 'afgj', 'afgk', 'afgl', 'afhj', 'afhk', 'afhl', 'afij', 'afik', 'afil', 'bdgj', 'bdgk', 'bdgl', 'bdhj', 'bdhk', 'bdhl', 'bdij', 'bdik', 'bdil', 'begj', 'begk', 'begl', 'behj', 'behk', 'behl', 'beij', 'beik', 'beil', 'bfgj', 'bfgk', 'bfgl', 'bfhj', 'bfhk', 'bfhl', 'bfij', 'bfik', 'bfil', 'cdgj', 'cdgk', 'cdgl', 'cdhj', 'cdhk', 'cdhl', 'cdij', 'cdik', 'cdil', 'cegj', 'cegk', 'cegl', 'cehj', 'cehk', 'cehl', 'ceij', 'ceik', 'ceil', 'cfgj', 'cfgk', 'cfgl', 'cfhj', 'cfhk', 'cfhl', 'cfij', 'cfik', 'cfil']

    # Test case 9
    digits = "8"
    print(solution.letterCombinations(digits))  # Expected output: ["t","u","v"]

    # Test case 10
    digits = "456"
    print(solution.letterCombinations(digits))  # Expected output: ['gjm', 'gjn', 'gjo', 'gkm', 'gkn', 'gko', 'glm', 'gln', 'glo', 'hjm', 'hjn', 'hjo', 'hkm', 'hkn', 'hko', 'hlm', 'hln', 'hlo', 'ijm', 'ijn', 'ijo', 'ikm', 'ikn', 'iko', 'ilm', 'iln', 'ilo']

test_letter_combinations()