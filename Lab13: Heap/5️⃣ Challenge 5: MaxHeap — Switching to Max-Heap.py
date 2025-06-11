class MaxHeap:
    # 🦁 MaxHeap data structure using list
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Insert and heapify up for max-heap property
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Move up while parent < current (for MaxHeap: parent < child)
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def delete_max(self):
        # Remove and return the largest (root) element
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_down(self, index):
        # Move down while current < child (for MaxHeap: current < largest child)
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1);         print("🦁 Test 1:", h.heap == [1])
    for v in [3,2,8,5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0] == max(h.heap))
    h.delete_max();      print("🦁 Test 3:", h.heap[0] == max(h.heap))
    h = MaxHeap()
    for v in [5,3,1]:
        h.insert(v)
    h.delete_max();      print("🦁 Test 4:", h.heap == [3,1])
    h = MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max() == 10 and h.heap == [])

test_max_heap()
