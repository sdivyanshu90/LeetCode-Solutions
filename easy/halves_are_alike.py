class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[:len(s)//2].lower()
        b = s[len(s)//2 : ].lower()
        vowels = ["a", "e", "i", "o", "u"]
        count_a = 0
        for char in a:
            if char in vowels:
                count_a += 1
        count_b = 0
        for char in b:
            if char in vowels:
                count_b += 1

        if count_a == count_b:
            return True
        else:
            return False

def test_halves_are_alike():
    s = Solution()

    # Test Case 1
    str1 = "dad"
    print(s.halvesAreAlike(str1)) # Expected Output: False

    # Test Case 2
    str2 = "textbook"
    print(s.halvesAreAlike(str2)) # Expected Output: False

    # Test Case 3
    str3 = "MerryChristmas"
    print(s.halvesAreAlike(str3)) # Expected Output: False

    # Test Case 4
    str4 = "AbCdEfGh"
    print(s.halvesAreAlike(str4)) # Expected Output: True

    # Test Case 5
    str5 = "aeiouAEIOU"
    print(s.halvesAreAlike(str5)) # Expected Output: True

test_halves_are_alike()