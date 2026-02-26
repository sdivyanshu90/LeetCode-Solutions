class CustomStack:

    def __init__(self, maxSize: int):
        self._stack = []
        self._max_size = maxSize

    def push(self, x: int) -> None:
        if len(self._stack) < self._max_size:
            self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop() if self._stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self._stack))):
            self._stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

def test_custom_stack():
    # Test case 1
    customStack1 = CustomStack(3)
    customStack1.push(1)
    customStack1.push(2)
    print(customStack1.pop())  # Expected output: 2
    customStack1.push(2)
    customStack1.push(3)
    customStack1.push(4)  # This push should be ignored since the stack is at max capacity
    customStack1.increment(5, 100)  # Increment the bottom 5 elements by 100 (only 3 elements in stack)
    customStack1.increment(2, 100)  # Increment the bottom 2 elements by 100
    print(customStack1.pop())  # Expected output: 103 (3 + 100)
    print(customStack1.pop())  # Expected output: 202 (2 + 100 + 100)
    print(customStack1.pop())  # Expected output: 201 (1 + 100 + 100)
    print(customStack1.pop())  # Expected output: -1 (stack is empty)

    # Test case 2
    customStack2 = CustomStack(2)
    customStack2.push(1)
    customStack2.push(2)
    customStack2.push(3)  # This push should be ignored since the stack is at max capacity
    customStack2.increment(2, 100)  # Increment the bottom 2 elements by 100
    print(customStack2.pop())  # Expected output: 102 (2 + 100)
    print(customStack2.pop())  # Expected output: 101 (1 + 100)
    print(customStack2.pop())  # Expected output: -1 (stack is empty)

    # Test case 3
    customStack3 = CustomStack(1)
    customStack3.push(1)
    customStack3.increment(1, 100)  # Increment the bottom 1 element by 100
    print(customStack3.pop())  # Expected output: 101 (1 + 100)
    print(customStack3.pop())  # Expected output: -1 (stack is empty)

    # Test case 4
    customStack4 = CustomStack(0)  # Stack with max size 0
    customStack4.push(1)  # This push should be ignored since the stack is at max capacity
    print(customStack4.pop())  # Expected output: -1 (stack is empty)
    customStack4.increment(1, 100)  # Increment should have no effect since the stack is empty
    print(customStack4.pop())  # Expected output: -1 (stack is empty)

    # Test case 5
    customStack5 = CustomStack(5)
    customStack5.push(1)
    customStack5.push(2)
    customStack5.push(3)
    customStack5.push(4)
    customStack5.push(5)
    customStack5.increment(3, 100)  # Increment the bottom 3 elements by 100
    print(customStack5.pop())  # Expected output: 5 (not incremented)
    print(customStack5.pop())  # Expected output: 4 (not incremented)
    print(customStack5.pop())  # Expected output: 103 (3 + 100)
    print(customStack5.pop())  # Expected output: 102 (2 + 100)
    print(customStack5.pop())  # Expected output: 101 (1 + 100)
    print(customStack5.pop())  # Expected output: -1 (stack is empty)

test_custom_stack()