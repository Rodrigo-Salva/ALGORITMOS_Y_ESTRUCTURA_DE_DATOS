# Circular Buffer for Streaming Data

class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.start = 0
        self.size = 0

    def add(self, value):
        index = (self.start + self.size) % self.capacity
        self.buffer[index] = value
        if self.size < self.capacity:
            self.size += 1
        else:
            self.start = (self.start + 1) % self.capacity

    def get_latest(self):
        result = []
        for i in range(self.size):
            index = (self.start + i) % self.capacity
            result.append(self.buffer[index])
        return result

    def average(self):
        if self.size == 0:
            return 0
        return sum(self.get_latest()) / self.size

    def maximum(self):
        if self.size == 0:
            return None
        return max(self.get_latest())

    def minimum(self):
        if self.size == 0:
            return None
        return min(self.get_latest())

def main():
    print("=== Circular Buffer Demo ===")
    cb = CircularBuffer(5)
    stream_data = [10, 20, 30, 40, 50, 60]  # 60 will overwrite 10
    for val in stream_data:
        cb.add(val)

    print("Buffer Content:", cb.get_latest())
    print("Average:", cb.average())
    print("Max:", cb.maximum())
    print("Min:", cb.minimum())

if __name__ == "__main__":
    main()

# Test Case 1: Standard test case with a buffer size of 3
print("Test Case 1: Standard Test Case")
cb = CircularBuffer(3)
stream_data = [10, 20, 30, 40]  # 40 will overwrite 10
for val in stream_data:
    cb.add(val)

print("Buffer Content:", cb.get_latest())
print("Average:", cb.average())
print("Max:", cb.maximum())
print("Min:", cb.minimum())

# Test Case 2: Buffer size is 1, only one data point at a time
print("\nTest Case 2: Buffer Size 1")
cb = CircularBuffer(1)
stream_data = [10, 20, 30]  # The data is overwritten each time
for val in stream_data:
    cb.add(val)

print("Buffer Content:", cb.get_latest())
print("Average:", cb.average())
print("Max:", cb.maximum())
print("Min:", cb.minimum())

# Test Case 3: Large data stream with a buffer size of 5
print("\nTest Case 3: Large Data Stream with Buffer Size 5")
cb = CircularBuffer(5)
stream_data = [100, 200, 300, 400, 500, 600, 700]  # 100 will be overwritten
for val in stream_data:
    cb.add(val)

print("Buffer Content:", cb.get_latest())
print("Average:", cb.average())
print("Max:", cb.maximum())
print("Min:", cb.minimum())
