class Solution:
    def countAndSay(self, n: int) -> str:
        current_sequence = '1'
        
        for i in range(2, n + 1):
            next_sequence = ''
            count = 1
            current_digit = current_sequence[0]
            
            for digit in current_sequence[1:]:
                if digit == current_digit:
                    count += 1
                else:
                    next_sequence += str(count) + current_digit
                    count = 1
                    current_digit = digit
            
            next_sequence += str(count) + current_digit
            current_sequence = next_sequence
        
        return current_sequence

def test_count_and_say():
    solution = Solution()

    # Test case 1: Basic case
    n1 = 1
    result1 = solution.countAndSay(n1)
    print(result1)  # Expected output: "1"

    # Test case 2: Second term
    n2 = 2
    result2 = solution.countAndSay(n2)
    print(result2)  # Expected output: "11"

    # Test case 3: Third term
    n3 = 3
    result3 = solution.countAndSay(n3)
    print(result3)  # Expected output: "21"

    # Test case 4: Fourth term
    n4 = 4
    result4 = solution.countAndSay(n4)
    print(result4)  # Expected output: "1211"

    # Test case 5: Fifth term
    n5 = 5
    result5 = solution.countAndSay(n5)
    print(result5)  # Expected output: "111221"

    # Test case 6: Sixth term
    n6 = 6
    result6 = solution.countAndSay(n6)
    print(result6)  # Expected output: "312211"

    # Test case 7: Seventh term
    n7 = 7
    result7 = solution.countAndSay(n7)
    print(result7)  # Expected output: "13112221"

    # Test case 8: Eighth term
    n8 = 8
    result8 = solution.countAndSay(n8)
    print(result8)  # Expected output: "1113213211"

    # Test case 9: Ninth term
    n9 = 9
    result9 = solution.countAndSay(n9)
    print(result9)  # Expected output: "31131211131221"

    # Test case 10: Tenth term
    n10 = 10
    result10 = solution.countAndSay(n10)
    print(result10)  # Expected output: "13211311123113112211"

test_count_and_say()