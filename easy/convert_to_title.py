from typing import List

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        
        while columnNumber > 0:
            columnNumber -= 1
            title.append(chr((columnNumber % 26) + 65))
            columnNumber //= 26
        
        return ''.join(reversed(title))

def test_convert_to_title():
    s = Solution()

    # Test Case 1: First column number
    print(s.convertToTitle(1)) # Expected Output: A

    # Test Case 2: Last single-letter column
    print(s.convertToTitle(26)) # Expected Output: Z

    # Test Case 3: First double-letter column
    print(s.convertToTitle(27)) # Expected Output: AA

    # Test Case 4: A standard double-letter column
    print(s.convertToTitle(51)) # Expected Output: AY

    # Test Case 5: Another important double-letter boundary
    print(s.convertToTitle(52)) # Expected Output: AZ

    # Test Case 6: The boundary right before the first three-letter column
    print(s.convertToTitle(702)) # Expected Output: ZZ

    # Test Case 7: First three-letter column
    print(s.convertToTitle(703)) # Expected Output: AAA

    # Test Case 8: A column ending in Z
    print(s.convertToTitle(78)) # Expected Output: BZ
    
    # Test Case 9: A large column number
    print(s.convertToTitle(16384)) # Expected Output: XFZ
    
    # Test Case 10: Invalid input (zero)
    print(s.convertToTitle(0)) # Expected Output: ""

test_convert_to_title()