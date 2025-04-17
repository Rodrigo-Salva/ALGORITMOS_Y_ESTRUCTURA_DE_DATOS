class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        index = len(self.queue)
        self.queue.append((priority, index, item))
        print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        if self.isEmpty():
            return None

        highest = max(self.queue, key=lambda x: (x[0], -x[1]))
        self.queue.remove(highest)
        print(f"Dequeued: {highest[2]}")
        return highest[2]

    def peek(self):
        if self.isEmpty():
            return None
        highest = max(self.queue, key=lambda x: (x[0], -x[1]))
        return highest[2]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


pq = PriorityQueue()

pq.enqueue("Task A", 2)
pq.enqueue("Task B", 3)
pq.enqueue("Task C", 3)
pq.enqueue("Task D", 1)

print("Peek:", pq.peek())
print("Size:", pq.size())

pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
print("Is empty?", pq.isEmpty())

#3 test
pq.enqueue("Email", 1)
pq.enqueue("System Alert", 5)
pq.dequeue()  # Expected output: "System Alert"

pq.enqueue("A", 3)
pq.enqueue("B", 3)
pq.peek()  # Expected output: "A" (same priority, but earlier insertion)

pq.isEmpty()  # Expected: False
pq.size()     # Expected: Total number of elements


