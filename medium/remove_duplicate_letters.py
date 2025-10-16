class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_occurrence = {char: i for i, char in enumerate(s)}
        
        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)

def test_remove_duplicate_letters():
    s = Solution()

    # Test Case 1: Basic test with simple string
    input_str = "bcabc"
    print(s.removeDuplicateLetters(input_str))  # Expected: "abc"

    # Test Case 2: String with all characters the same
    input_str = "aaaaa"
    print(s.removeDuplicateLetters(input_str))  # Expected: "a"

    # Test Case 3: String with letters already in order
    input_str = "abc"
    print(s.removeDuplicateLetters(input_str))  # Expected: "abc"

    # Test Case 4: String with non-unique letters, needs to reorder
    input_str = "cbacdcbc"
    print(s.removeDuplicateLetters(input_str))  # Expected: "acdb"

    # Test Case 5: String with more characters
    input_str = "cdadabcc"
    print(s.removeDuplicateLetters(input_str))  # Expected: "adbc"

    # Test Case 6: String with only one unique character repeated
    input_str = "zzzzzzzz"
    print(s.removeDuplicateLetters(input_str))  # Expected: "z"

    # Test Case 7: Single character string
    input_str = "x"
    print(s.removeDuplicateLetters(input_str))  # Expected: "x"

    # Test Case 8: Large input (testing performance)
    input_str = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"
    print(s.removeDuplicateLetters(input_str))  # Expected: "abmqwertyuiopsdfghjklzxcvn"

    # Test Case 9: Mixed case (although the problem is usually case-sensitive, this assumes lowercase input)
    input_str = "AbcAbcAbc"
    print(s.removeDuplicateLetters(input_str))  # Expected: "Abc" 

test_remove_duplicate_letters()