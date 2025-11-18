class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i : i+k] = reversed(a[i: i+k])
        return "".join(a)

def test_reverse_str():
    s = Solution()

    # Test case 1
    str1 = "abcdefg"
    k1 = 2
    print(s.reverseStr(str1, k1)) # Expected output: "bacdfeg"

    # Test case 2
    str2 = "abcd"
    k2 = 2
    print(s.reverseStr(str2, k2)) # Expected output: "bacd"

    # Test case 3
    str3 = "a"
    k3 = 1
    print(s.reverseStr(str3, k3)) # Expected output: "a"

    # Test case 4
    str4 = "abcdefghij"
    k4 = 3
    print(s.reverseStr(str4, k4)) # Expected output: "cbadefihgj"

    # Test case 5
    str5 = "zyxwvutsrqponmlkjihgfedcba"
    k5 = 5
    print(s.reverseStr(str5, k5)) # Expected output: "vwxyzutsrqlmnopkjihgbcdefa"


test_reverse_str()