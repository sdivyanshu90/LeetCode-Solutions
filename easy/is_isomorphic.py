class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def test_is_isomorphic():
    s = Solution()

    # Test Case 1: Basic isomorphic case
    str_s, str_t = "egg", "add"
    print(f"\nInput: s='{str_s}', t='{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: True
    # Mapping: e -> a, g -> d

    # Test Case 2: Basic non-isomorphic case (two chars in s map to the same char in t)
    str_s, str_t = "foo", "bar"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: False
    # 'f' -> 'b', 'o' -> 'a', but then the second 'o' would need to map to 'r', which is not allowed.
    # The code catches this because len(set(s)) is 2, but len(set(t)) is 3.

    # Test Case 3: More complex isomorphic case
    str_s, str_t = "paper", "title"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: True
    # Mapping: p->t, a->i, e->l, r->e

    # Test Case 4: Non-isomorphic case where a single char in s would need to map to two different chars in t
    str_s, str_t = "badc", "baba"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: False
    # `b` maps to `b`, `a` maps to `a`. But then `d` maps to `b`. No two source characters can map to the same target char.
    # The code catches this because len(set(s)) is 4, but len(set(t)) is 2.

    # Test Case 5: Empty strings
    str_s, str_t = "", ""
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: True

    # Test Case 6: Single character strings
    str_s, str_t = "a", "b"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: True

    # Test Case 7: Identical strings
    str_s, str_t = "turtle", "turtle"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: True

    # Test Case 8: Strings with numbers and symbols
    str_s, str_t = "13-5", "42*6"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: True

    # Test Case 9: Strings with different lengths
    str_s, str_t = "abc", "defg"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: False
    # The logic correctly fails as len(set(s)) is 3 and len(set(t)) is 4.

    # Test Case 10: One character mapping to itself, another mapping to something else
    str_s, str_t = "abca", "bdbc"
    print(f"Input: s = '{str_s}', t = '{str_t}'. Output: {s.isIsomorphic(str_s, str_t)}") # Expected: False
    # 'a' maps to 'b' initially, but maps to 'c' at the end. This violates the rule.
    # The code catches this because len(set(zip(s,t))) is 4, but len(set(s)) is 3.

test_is_isomorphic()