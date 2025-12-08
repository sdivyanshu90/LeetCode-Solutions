class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_count = {char: 0 for char in order}
        for char in s:
            if char in char_count:
                char_count[char] += 1
    
        sorted_s = ''
        for char in order:
            sorted_s += char * char_count[char]
    
        for char in s:
            if char not in order:
                sorted_s += char

        return sorted_s

def test_custom_sort_string():
    solution = Solution()
    
    # Test case 1
    order = "cba"
    s = "abcd"
    print(solution.customSortString(order, s)) # Expected: "cbad"
    
    # Test case 2
    order = "xyz"
    s = "zyxwv"
    print(solution.customSortString(order, s)) # Expected: "zyxwv"
    
    # Test case 3
    order = "hgfedcba"
    s = "abcdefgh"
    print(solution.customSortString(order, s)) # Expected: "hgfedcba"
    
    # Test case 4
    order = "abc"
    s = "aaabbbcccddd"
    print(solution.customSortString(order, s)) # Expected: "aaabbbcccddd"

    # Test case 5
    order = "qwerty"
    s = "ytrewqzxcvbn"
    print(solution.customSortString(order, s)) # Expected: "ytrewqzxcvbn"

    # Test case 6
    order = "mnop"
    s = "ponmlkjihg"
    print(solution.customSortString(order, s)) # Expected: "ponmlkjihg"

    # Test case 7
    order = "zyxwvutsrqponmlkjihgfedcba"
    s = "abcdefghijklmnopqrstuvwxyz"
    print(solution.customSortString(order, s)) # Expected: "zyxwvutsrqponmlkjihgfedcba"

    # Test case 8
    order = "abcde"
    s = "edcbaedcba"
    print(solution.customSortString(order, s)) # Expected: "aabbccddeed"

    # Test case 9
    order = "lmno"
    s = "onmlkjihgfe"
    print(solution.customSortString(order, s)) # Expected: "onmlkjihgfe"

    # Test case 10
    order = "rstuv"
    s = "uvwxyzrst"
    print(solution.customSortString(order, s)) # Expected: "rstuuvwxyz"

test_custom_sort_string()