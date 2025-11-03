from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children

def test_find_content_children():
    s = Solution()

    # Test case 1
    g = [1,2,3]
    s_cookies = [1,1]
    print(s.findContentChildren(g, s_cookies))  # Expected output: 1

    # Test case 2
    g = [1,2]
    s_cookies = [1,2,3]
    print(s.findContentChildren(g, s_cookies))  # Expected output: 2

    # Test case 3
    g = [10,9,8,7]
    s_cookies = [5,6,7,8]
    print(s.findContentChildren(g, s_cookies))  # Expected output: 2

    # Test case 4
    g = [1,2,3]
    s_cookies = [3]
    print(s.findContentChildren(g, s_cookies))  # Expected output: 1

    # Test case 5
    g = [1,2,3]
    s_cookies = []
    print(s.findContentChildren(g, s_cookies))  # Expected output: 0

test_find_content_children()