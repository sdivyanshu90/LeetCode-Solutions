from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_dollar_bills = 0
        ten_dollar_bills = 0

        for customer_bill in bills:
            if customer_bill == 5:
                five_dollar_bills += 1
            elif customer_bill == 10:
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    return False
            else:
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
        return True

def test_lemonadeChange():
    solution = Solution()
    
    # Test Case 1
    print(solution.lemonadeChange([5,5,5,10,20])) # Expected: True

    # Test Case 2
    print(solution.lemonadeChange([5,5,10])) # Expected: True

    # Test Case 3
    print(solution.lemonadeChange([10,10])) # Expected: False

    # Test Case 4
    print(solution.lemonadeChange([5,5,10,10,20])) # Expected: False

    # Test Case 5
    print(solution.lemonadeChange([5,5,5,5,10,5,10,10,10,20])) # Expected: True

test_lemonadeChange()