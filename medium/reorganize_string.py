from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_count = max(counter.values())
        n = len(s)
        
        if max_count > (n + 1) // 2:
            return ""
        
        result = [''] * n
        even_index = 0
        odd_index = 1
        
        for char, count in counter.items():
            while count > 0 and count <= n // 2 and odd_index < n:
                result[odd_index] = char
                count -= 1
                odd_index += 2
            
            while count > 0:
                result[even_index] = char
                count -= 1
                even_index += 2
        
        return ''.join(result)

def test_reorganize_string():
    solution = Solution()
    
    # Test case 1
    s1 = "aab"
    print(solution.reorganizeString(s1)) # Expected: "aba"
    
    # Test case 2
    s2 = "aaab"
    print(solution.reorganizeString(s2)) # Expected: ""
    
    # Test case 3
    s3 = "vvvlo"
    print(solution.reorganizeString(s3)) # Expected: "vlvov"
    
    # Test case 4
    s4 = "aaaabbbbcc"
    print(solution.reorganizeString(s4)) # Expected: "bababacacb"
    
    # Test case 5
    s5 = "aabbcc"
    print(solution.reorganizeString(s5)) # Expected: "bacacb"
    
    # Test case 6
    s6 = "aaaaa"
    print(solution.reorganizeString(s6)) # Expected: ""
    
    # Test case 7
    s7 = "abcde"
    print(solution.reorganizeString(s7)) # Expected: "cadbe"
    
    # Test case 8
    s8 = "aaabbbccc"
    print(solution.reorganizeString(s8)) # Expected: "babacacbc"
    
    # Test case 9
    s9 = "zzzyyyxxx"
    print(solution.reorganizeString(s9)) # Expected: "yzyzxzxyx"
    
    # Test case 10
    s10 = "aabb"
    print(solution.reorganizeString(s10)) # Expected: "abab"
test_reorganize_string()