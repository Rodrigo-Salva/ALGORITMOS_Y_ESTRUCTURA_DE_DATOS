#Exercise 5: Sliding Window Maximum
class CircularDeque:
    def __init__(self, k):
        """Initialize the deque with a fixed capacity k."""
        self.capacity = k
        self.deque = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value):
        """Insert an item at the front. Return True if successful."""
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """Insert an item at the rear. Return True if successful."""
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self):
        """Delete an item from the front. Return True if successful."""
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        """Delete an item from the rear. Return True if successful."""
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        """Return the front item, or -1 if empty."""
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self):
        """Return the rear item, or -1 if empty."""
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self):
        """Check if the deque is empty."""
        return self.size == 0

    def isFull(self):
        """Check if the deque is full."""
        return self.size == self.capacity

    def __str__(self):
        """Visualize the internal state of the deque."""
        result = []
        i = self.front
        for _ in range(self.size):
            result.append(self.deque[i])
            i = (i + 1) % self.capacity
        return f"CircularDeque: {result}"


# 🔍 TEST CASES
def test_circular_deque():
    print("== Testing Circular Deque ==")
    dq = CircularDeque(3)

    print("Insert 10 at rear:", dq.insertLast(10))  # True
    print("Insert 20 at rear:", dq.insertLast(20))  # True
    print("Insert 5 at front:", dq.insertFront(5))  # True
    print("Deque is full?", dq.isFull())            # True
    print("Insert 99 at front (should fail):", dq.insertFront(99))  # False

    print("Front:", dq.getFront())  # 5
    print("Rear:", dq.getRear())    # 20
    print(dq)

    print("Delete rear:", dq.deleteLast())  # True
    print("Insert 30 at front:", dq.insertFront(30))  # True
    print("Front:", dq.getFront())  # 30
    print("Rear:", dq.getRear())    # 10

    print("Final deque:", dq)
    print("Deque is empty?", dq.isEmpty())  # False
    print("== All tests done ✅ ==")

# Run the test
if __name__ == "__main__":
    test_circular_deque()
