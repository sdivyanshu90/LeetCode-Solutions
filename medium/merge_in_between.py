# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1

        for index in range (b):
            if index == a - 1:
                start = end
            end = end.next

        start.next = list2
        while (list2.next is not None):
            list2 = list2.next
        list2.next = end.next
        end.next = None
        
        return list1

def test_merge_in_between():
    solution = Solution()

    # Test case 1
    list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    a = 3
    b = 4
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    result = solution.mergeInBetween(list1, a, b, list2)
    while result:
        print(result.val)  # Expected output: 0 -> 1 -> 2 -> 1000000 -> 1000001 -> 1000002 -> 5
        result = result.next

    # Test case 2
    list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    a = 1
    b = 2
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    result = solution.mergeInBetween(list1, a, b, list2)
    while result:
        print(result.val)  # Expected output: 0 -> 1000000 -> 1000001 -> 1000002 -> 3 -> 4 -> 5
        result = result.next

    # Test case 3
    list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    a = 0
    b = 0
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    result = solution.mergeInBetween(list1, a, b, list2)
    while result:
        print(result.val)  # Expected output: 1000000 -> 1000001 -> 1000002 -> 1 -> 2 -> 3 -> 4 -> 5
        result = result.next

    # Test case 4
    list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    a = 4
    b = 5
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    result = solution.mergeInBetween(list1, a, b, list2)
    while result:
        print(result.val)  # Expected output: 0 -> 1 -> 2 -> 3 -> 1000000 -> 1000001 -> 1000002
        result = result.next

    # Test case 5
    list1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    a = 2
    b = 3
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    result = solution.mergeInBetween(list1, a, b, list2)
    while result:
        print(result.val)  # Expected output: 0 -> 1 -> 1000000 -> 1000001 -> 1000002 -> 4 -> 5
        result = result.next

test_merge_in_between()