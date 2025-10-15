class Solution:
    number_to_words_map = {
        1000000000: "Billion", 
        1000000: "Million", 
        1000: "Thousand",
        100: "Hundred", 
        90: "Ninety", 
        80: "Eighty", 
        70: "Seventy",
        60: "Sixty", 
        50: "Fifty", 
        40: "Forty", 
        30: "Thirty",
        20: "Twenty", 
        19: "Nineteen", 
        18: "Eighteen", 
        17: "Seventeen",
        16: "Sixteen", 
        15: "Fifteen", 
        14: "Fourteen", 
        13: "Thirteen",
        12: "Twelve", 
        11: "Eleven", 
        10: "Ten", 
        9: "Nine", 
        8: "Eight",
        7: "Seven", 
        6: "Six", 
        5: "Five", 
        4: "Four", 
        3: "Three",
        2: "Two", 
        1: "One"
    }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        for value, word in self.number_to_words_map.items():
            if num >= value:
                prefix = (self.numberToWords(num // value) + " ") if num >= 100 else ""
                unit = word
                suffix = "" if num % value == 0 else " " + self.numberToWords(num % value)
                return prefix + unit + suffix

        return ""

def test_all_cases():
    s = Solution()

    # Test Case 1: The maximum 32-bit signed integer.
    num1 = 2147483647
    print(f"\nInput: {num1}")
    print(f"Expected Output: Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven")
    print(f"Actual Output:   {s.numberToWords(num1)}")

    # Test Case 2: A number with internal zeros across different scales.
    num2 = 1000010
    print(f"\nInput: {num2}")
    print(f"Expected Output: One Million Ten")
    print(f"Actual Output:   {s.numberToWords(num2)}")

    # Test Case 3: A number that is a large power of 1000.
    num3 = 1000000
    print(f"\nInput: {num3}")
    print(f"Expected Output: One Million")
    print(f"Actual Output:   {s.numberToWords(num3)}")

    # Test Case 4: A number just below a major threshold.
    num4 = 999999999
    print(f"\nInput: {num4}")
    print(f"Expected Output: Nine Hundred Ninety Nine Million Nine Hundred Ninety Nine Thousand Nine Hundred Ninety Nine")
    print(f"Actual Output:   {s.numberToWords(num4)}")

    # Test Case 5: A number with a zero in the hundreds place.
    num5 = 1005
    print(f"\nInput: {num5}")
    print(f"Expected Output: One Thousand Five")
    print(f"Actual Output:   {s.numberToWords(num5)}")
    
    # Test Case 6: A number with a complex pattern of repeated digits and zeros.
    num6 = 101101101
    print(f"\nInput: {num6}")
    print(f"Expected Output: One Hundred One Million One Hundred One Thousand One Hundred One")
    print(f"Actual Output:   {s.numberToWords(num6)}")

    # Test Case 7: A number that ends in a 'teen'.
    num7 = 618
    print(f"\nInput: {num7}")
    print(f"Expected Output: Six Hundred Eighteen")
    print(f"Actual Output:   {s.numberToWords(num7)}")

    # Test Case 8: A number with a zero in the thousands group.
    num8 = 5000821
    print(f"\nInput: {num8}")
    print(f"Expected Output: Five Million Eight Hundred Twenty One")
    print(f"Actual Output:   {s.numberToWords(num8)}")

    # Test Case 9: A number that tests the transition from tens to teens.
    num9 = 12021
    print(f"\nInput: {num9}")
    print(f"Expected Output: Twelve Thousand Twenty One")
    print(f"Actual Output:   {s.numberToWords(num9)}")

    # Test Case 10: The absolute base case for recursion.
    # Though the main function has a check for `num == 0`, this tests the recursive path for a remainder of 0 ending on a single digit.
    num10 = 10
    print(f"\nInput: {num10}")
    print(f"Expected Output: Ten")
    print(f"Actual Output:   {s.numberToWords(num10)}")


test_all_cases()