from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum = carry
            
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            carry = sum // 10
            digit = sum % 10
            
            curr.next = ListNode(digit)
            curr = curr.next
        
        return dummy.next

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to print linked list as a list
def print_linked_list(l):
    result = []
    while l:
        result.append(l.val)
        l = l.next
    return result


# Test Cases for addTwoNumbers
def test_add_two_numbers():
    solution = Solution()

    # Test Case 1: Simple Addition without Carry
    l1 = create_linked_list([2, 4, 3])  # 342
    l2 = create_linked_list([5, 6, 4])  # 465
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [7, 0, 8] (807)

    # Test Case 2: Addition with Carry
    l1 = create_linked_list([9, 9, 9])  # 999
    l2 = create_linked_list([1])        # 1
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [0, 0, 0, 1] (1000)

    # Test Case 3: One empty list
    l1 = create_linked_list([1, 2, 3])  # 321
    l2 = create_linked_list([])         # 0
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [1, 2, 3] (321)

    # Test Case 4: Both lists with carry
    l1 = create_linked_list([8, 9, 9])  # 998
    l2 = create_linked_list([2, 1, 2])  # 212
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [0, 1, 2, 1] (1210)

    # Test Case 5: Large Numbers with Carry
    l1 = create_linked_list([9, 9, 9, 9, 9])  # 99999
    l2 = create_linked_list([1])                # 1
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [0, 0, 0, 0, 0, 1] (100000)

    # Test Case 6: Single Digit Numbers
    l1 = create_linked_list([5])  # 5
    l2 = create_linked_list([7])  # 7
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [2, 1] (12)

    # Test Case 7: Both lists are of different lengths
    l1 = create_linked_list([1, 2])  # 21
    l2 = create_linked_list([9, 9, 9])  # 999
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [0, 0, 0, 1] (1020)

    # Test Case 8: One list is larger than the other
    l1 = create_linked_list([1, 2, 3, 4])  # 4321
    l2 = create_linked_list([5, 6])        # 65
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [6, 8, 3, 4] (4386)

    # Test Case 9: No Carry for the last digit
    l1 = create_linked_list([4, 3, 2, 1])  # 1234
    l2 = create_linked_list([5, 6, 7, 8])  # 8765
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [9, 9, 9, 9] (9999)

    # Test Case 10: Empty lists
    l1 = create_linked_list([])  # 0
    l2 = create_linked_list([])  # 0
    result = solution.addTwoNumbers(l1, l2)
    print(print_linked_list(result))  # Expected output: [0] (0)

# Run all the test cases
test_add_two_numbers()