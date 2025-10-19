# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def __prepare_next_element(self):
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(reversed(self.stack.pop().getList()))

    def next(self) -> int:
        self.__prepare_next_element()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self.__prepare_next_element()
        return bool(self.stack)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

def test_nested_iterator():
    # Helper function to create mock NestedInteger
    def create_integer(val):
        ni = NestedInteger()
        ni.isInteger = lambda: True
        ni.getInteger = lambda: val
        return ni
    
    def create_list(items):
        ni = NestedInteger()
        ni.isInteger = lambda: False
        ni.getList = lambda: items
        return ni

    # Test Case 1: Empty nested list
    nestedList = []
    i = NestedIterator(nestedList)
    result = []
    while i.hasNext():
        result.append(i.next())
    print(f"Test 1: {result}")  # Expected: []

    # Test Case 2: Single integer
    nestedList = [create_integer(5)]
    i = NestedIterator(nestedList)
    result = []
    while i.hasNext():
        result.append(i.next())
    print(f"Test 2: {result}")  # Expected: [5]

    # Test Case 3: Nested list with multiple integers
    nestedList = [
        create_list([create_integer(1), create_integer(2)]),
        create_integer(3)
    ]
    i = NestedIterator(nestedList)
    result = []
    while i.hasNext():
        result.append(i.next())
    print(f"Test 3: {result}")  # Expected: [1, 2, 3]

    # Test Case 4: Deeply nested list
    nestedList = [
        create_list([
            create_list([create_integer(10)])
        ])
    ]
    i = NestedIterator(nestedList)
    result = []
    while i.hasNext():
        result.append(i.next())
    print(f"Test 4: {result}")  # Expected: [10]

    # Test Case 5: Mixed nested list [[4,[5]],6]
    nestedList = [
        create_list([
            create_integer(4),
            create_list([create_integer(5)])
        ]),
        create_integer(6)
    ]
    i = NestedIterator(nestedList)
    result = []
    while i.hasNext():
        result.append(i.next())
    print(f"Test 5: {result}")  # Expected: [4, 5, 6]

test_nested_iterator()