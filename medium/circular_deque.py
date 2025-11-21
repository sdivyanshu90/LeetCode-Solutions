class MyCircularDeque:

    def __init__(self, k):
        self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

def test_circular_deque():
    deque = MyCircularDeque(3)

    print(deque.insertLast(1))  # Expected output: True
    print(deque.insertLast(2))  # Expected output: True
    print(deque.insertFront(3))  # Expected output: True
    print(deque.insertFront(4))  # Expected output: False (deque is full)
    print(deque.getRear())       # Expected output: 2
    print(deque.isFull())       # Expected output: True
    print(deque.deleteLast())   # Expected output: True
    print(deque.insertFront(4))  # Expected output: True
    print(deque.getFront())      # Expected output: 4

test_circular_deque()