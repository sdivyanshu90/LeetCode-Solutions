from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)

        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)

        def dfs(ch, visited):
            visited.add(ch)
            min_ch = ch
            for nei in adj[ch]:
                if nei not in visited:
                    candidate = dfs(nei, visited)
                    min_ch = min(min_ch, candidate)
            return min_ch

        result = []
        for ch in baseStr:
            visited = set()
            result.append(dfs(ch, visited))
        
        return ''.join(result)
        
def test_smallest_equivalent_string():
    solution = Solution()

    # Test case 1
    s1_1 = "parker"
    s2_1 = "morris"
    baseStr_1 = "parser"
    print(solution.smallestEquivalentString(s1_1, s2_1, baseStr_1))  # Expected output: "makkek"

    # Test case 2
    s1_2 = "hello"
    s2_2 = "world"
    baseStr_2 = "hold"
    print(solution.smallestEquivalentString(s1_2, s2_2, baseStr_2))  # Expected output: "hdld"

    # Test case 3
    s1_3 = "leetcode"
    s2_3 = "programs"
    baseStr_3 = "sourcecode"
    print(solution.smallestEquivalentString(s1_3, s2_3, baseStr_3))  # Expected output: "aauaaaaada"

    # Test case 4
    s1_4 = "abc"
    s2_4 = "bcd"
    baseStr_4 = "cba"
    print(solution.smallestEquivalentString(s1_4, s2_4, baseStr_4))  # Expected output: "aba"

    # Test case 5
    s1_5 = "xyz"
    s2_5 = "yza"
    baseStr_5 = "zyx"
    print(solution.smallestEquivalentString(s1_5, s2_5, baseStr_5))  # Expected output: "xwx"

test_smallest_equivalent_string()