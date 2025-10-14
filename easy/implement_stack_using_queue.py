class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack

def test_my_stack():
    s = MyStack()

    # --- Test Case 1: Initialization ---
    print("\n--- Test Case 1: Initializing a new stack ---")
    print(f"Is the new stack empty? {s.empty()}") # Expected: True

    # --- Test Case 2: Pushing a single element ---
    print("\n--- Test Case 2: Pushing one element ---")
    s.push(1)
    print(f"Pushed 1. Is the stack empty now? {s.empty()}") # Expected: False
    print(f"What is the top element? {s.top()}") # Expected: 1

    # --- Test Case 3: Pushing another element ---
    print("\n--- Test Case 3: Pushing a second element ---")
    s.push(2)
    print(f"Pushed 2. What is the top element now? {s.top()}") # Expected: 2

    # --- Test Case 4: Popping an element ---
    print("\n--- Test Case 4: Popping the top element ---")
    popped_value = s.pop()
    print(f"Popped value: {popped_value}") # Expected: 2
    print(f"What is the top element after pop? {s.top()}") # Expected: 1

    # --- Test Case 5: Checking if empty after one pop ---
    print("\n--- Test Case 5: Checking empty status ---")
    print(f"Is the stack empty? {s.empty()}") # Expected: False

    # --- Test Case 6: Popping the last element ---
    print("\n--- Test Case 6: Popping the final element ---")
    popped_value = s.pop()
    print(f"Popped value: {popped_value}") # Expected: 1
    print(f"Is the stack empty now? {s.empty()}") # Expected: True

    # --- Test Case 7: LIFO (Last-In, First-Out) verification ---
    print("\n--- Test Case 7: Verifying LIFO order ---")
    print("Pushing 10, then 20, then 30.")
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"First pop: {s.pop()}")  # Expected: 30
    print(f"Second pop: {s.pop()}") # Expected: 20
    print(f"Third pop: {s.pop()}")   # Expected: 10
    print(f"Is the stack empty after all pops? {s.empty()}") # Expected: True

    # --- Test Case 8: Pushing zero and negative numbers ---
    print("\n--- Test Case 8: Pushing zero and negative numbers ---")
    s.push(-5)
    s.push(0)
    print(f"Top element is: {s.top()}") # Expected: 0
    print(f"Popped value: {s.pop()}") # Expected: 0
    print(f"Top element is now: {s.top()}") # Expected: -5
    s.pop() # Clearing the stack for the next test

    # --- Test Case 9: Attempting to pop from an empty stack ---
    print("\n--- Test Case 9: Popping from an empty stack ---")
    try:
        s.pop()
    except IndexError:
        print("Successfully caught IndexError as expected.") # Expected

    # --- Test Case 10: Attempting to get top from an empty stack ---
    print("\n--- Test Case 10: Getting top from an empty stack ---")
    try:
        s.top()
    except IndexError:
        print("Successfully caught IndexError as expected.") # Expected

test_my_stack()