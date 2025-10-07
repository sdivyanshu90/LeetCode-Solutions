from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])
        res = []
        backtrack(0, [])
        return res

def test_partition():
    solution = Solution()
    
    # Test case 1
    s = "aab"
    print(solution.partition(s))  # Expected output: [["a","a","b"],["aa","b"]]

    # Test case 2
    s = "a"
    print(solution.partition(s))  # Expected output: [["a"]]

    # Test case 3
    s = "racecar"
    print(solution.partition(s))  # Expected output: [["r","a","c","e","c","a","r"], ["r","a","cec","a","r"], ["r", "aceca", "r"], ["racecar"]]

    # Test case 4
    s = "level"
    print(solution.partition(s))  # Expected output: [["l","e","v","e","l"], ["l","eve","l"], ["level"]]

    # Test case 5
    s = "noon"
    print(solution.partition(s))  # Expected output: [["n","o","o","n"], ["n","oo","n"], ["noon"]]

test_partition()