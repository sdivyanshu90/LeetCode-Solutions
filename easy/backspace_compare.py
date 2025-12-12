class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s) -> str:
            ls = []
            for l in s:
                try:
                    if l == '#':
                        ls.pop()
                    else:
                        ls.append(l)
                except IndexError:
                    continue
            print(ls)
            return ''.join(ls)
        
        return helper(s) == helper(t)

def test_backspaceCompare():
    solution = Solution()
    
    # Test Case 1
    print(solution.backspaceCompare("ab#c", "ad#c")) # Expected: True

    # Test Case 2
    print(solution.backspaceCompare("ab##", "c#d#")) # Expected: True

    # Test Case 3
    print(solution.backspaceCompare("a##c", "#a#c")) # Expected: True

    # Test Case 4
    print(solution.backspaceCompare("a#c", "b")) # Expected: False

    # Test Case 5
    print(solution.backspaceCompare("xywrrmp", "xywrrmu#p")) # Expected: True

test_backspaceCompare()