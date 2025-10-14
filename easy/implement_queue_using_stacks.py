class MyQueue:
    def __init__(self):
        self.s1 = [] # Main stack for queue storage
        self.s2 = [] # Helper stack for reordering

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.
        This is the "expensive push" method.
        """
        # 1. Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        
        # 2. Push the new element onto the now-empty s1
        self.s1.append(x)
        
        # 3. Move all elements back from s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of the queue and returns that element.
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1

def test_implement_queue_using_stacks():
    q = MyQueue()

    # --- Test Case 1: Initialization ---
    print("\n--- Test Case 1: Initializing a new queue ---")
    
    print(f"Is the new queue empty? {q.empty()}") # Expected: True

    # --- Test Case 2: Pushing a single element ---
    print("\n--- Test Case 2: Pushing one element ---")
    q.push(10)
    print(f"Pushed 10. Is the queue empty now? {q.empty()}") # Expected: False
    print(f"What is the front element (peek)? {q.peek()}") # Expected: 10

    # --- Test Case 3: Pushing a second element ---
    print("\n--- Test Case 3: Pushing a second element ---")
    q.push(20)
    print(f"Pushed 20. What is the front element now (peek)? {q.peek()}") # Expected: 10 (FIFO)

    # --- Test Case 4: Popping an element ---
    print("\n--- Test Case 4: Popping the front element ---")
    popped_value = q.pop()
    print(f"Popped value: {popped_value}") # Expected: 10
    print(f"What is the front element after pop (peek)? {q.peek()}") # Expected: 20

    # --- Test Case 5: Checking if empty after one pop ---
    print("\n--- Test Case 5: Checking empty status ---")
    print(f"Is the queue empty? {q.empty()}") # Expected: False

    # --- Test Case 6: Popping the last element ---
    print("\n--- Test Case 6: Popping the final element ---")
    popped_value = q.pop()
    print(f"Popped value: {popped_value}") # Expected: 20
    print(f"Is the queue empty now? {q.empty()}") # Expected: True

    # --- Test Case 7: FIFO (First-In, First-Out) verification ---
    print("\n--- Test Case 7: Verifying FIFO order ---")
    print("Pushing 1, then 2, then 3.")
    q.push(1)
    q.push(2)
    q.push(3)
    print(f"First pop: {q.pop()}")  # Expected: 1
    print(f"Second pop: {q.pop()}") # Expected: 2
    print(f"Third pop: {q.pop()}")   # Expected: 3
    print(f"Is the queue empty after all pops? {q.empty()}") # Expected: True

    # --- Test Case 8: Pushing after the queue has been emptied ---
    print("\n--- Test Case 8: Pushing after emptying ---")
    q.push(100)
    q.push(200)
    print(f"Front element is: {q.peek()}") # Expected: 100
    print(f"Popped value: {q.pop()}") # Expected: 100
    print(f"Front element is now: {q.peek()}") # Expected: 200
    q.pop() # Clearing the queue for the next test

    # --- Test Case 9: Attempting to pop from an empty queue ---
    print("\n--- Test Case 9: Popping from an empty queue ---")
    try:
        q.pop()
    except IndexError:
        print("Successfully caught IndexError as expected.") # Expected

    # --- Test Case 10: Attempting to peek at an empty queue ---
    print("\n--- Test Case 10: Peeking at an empty queue ---")
    try:
        q.peek()
    except IndexError:
        print("Successfully caught IndexError as expected.") # Expected

test_implement_queue_using_stacks()