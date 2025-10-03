from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(self.format_line(line, maxWidth))
                line = [word]
                line_length = len(word)
        
        result.append(' '.join(line).ljust(maxWidth))
        
        return result
    
    def format_line(self, line, maxWidth):
        if len(line) == 1:
            return line[0].ljust(maxWidth)
        
        total_spaces = maxWidth - sum(len(word) for word in line)
        space_gaps = len(line) - 1
        spaces_per_gap = total_spaces // space_gaps
        extra_spaces = total_spaces % space_gaps
        
        formatted_line = line[0]
        for i in range(1, len(line)):
            if extra_spaces > 0:
                spaces = spaces_per_gap + 1
                extra_spaces -= 1
            else:
                spaces = spaces_per_gap
            formatted_line += ' ' * spaces + line[i]
        
        return formatted_line

def test_full_justify():
    solution = Solution()
    # Test Case 1
    print(solution.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    # Expected output: ["This    is    an", "example  of text", "justification.  "]
    
    # Test Case 2
    print(solution.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    # Expected output: ["What   must   be", "acknowledgment  ", "shall be        "]
    
    # Test Case 3
    print(solution.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
                                "to","a","computer.","Art","is","everything","else","we","do"], 20))
    # Expected output: ["Science  is  what we", "understand      well", "enough to explain to",
    #                   "a  computer.  Art is", "everything else we do"]
    
    # Test Case 4
    print(solution.fullJustify(["Hello"], 10))
    # Expected output: ["Hello     "]
    
    # Test Case 5
    print(solution.fullJustify(["A", "quick", "brown", "fox"], 15))
    # Expected output: ["A     quick brown", "fox            "]
    
    # Test Case 6
    print(solution.fullJustify(["The", "sky", "is", "blue"], 10))
    # Expected output: ["The   sky", "is      blue"]
    
    # Test Case 7
    print(solution.fullJustify(["Longword"], 8))
    # Expected output: ["Longword"]
    
    # Test Case 8
    print(solution.fullJustify(["Fit"], 3))
    # Expected output: ["Fit"]
    
    # Test Case 9
    print(solution.fullJustify(["Two", "words"], 10))
    # Expected output: ["Two      ", "words     "]
    
    # Test Case 10
    print(solution.fullJustify(["One", "more", "test", "case"], 12))
    # Expected output: ["One   more", "test case"]

test_full_justify()