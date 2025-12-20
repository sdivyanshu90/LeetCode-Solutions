from typing import List

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = k
        result = []
        
        for digit in reversed(num):
            total = digit + carry
            result.append(total % 10)
            carry = total // 10
            
        while carry > 0:
            result.append(carry % 10)
            carry //= 10
        
        return result[::-1]

def test_add_to_array_form():
    solution = Solution()
    
    # Test case 1
    num = [1,2,0,0]
    k = 34
    print(solution.addToArrayForm(num, k))  # Expected output: [1,2,3,4]

    # Test case 2
    num = [2,7,4]
    k = 181
    print(solution.addToArrayForm(num, k))  # Expected output: [4,5,5]

    # Test case 3
    num = [2,1,5]
    k = 806
    print(solution.addToArrayForm(num, k))  # Expected output: [1,0,2,1]

    # Test case 4
    num = [9,9,9,9,9,9,9,9,9,9]
    k = 1
    print(solution.addToArrayForm(num, k))  # Expected output: [1,0,0,0,0,0,0,0,0,0,0]

    # Test case 5
    num = [0]
    k = 1000
    print(solution.addToArrayForm(num, k))  # Expected output: [1,0,0,0]

test_add_to_array_form()