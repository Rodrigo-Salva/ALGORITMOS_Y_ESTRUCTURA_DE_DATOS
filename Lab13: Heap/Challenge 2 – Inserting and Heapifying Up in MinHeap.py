class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)             # Añadir al final
        self._heapify_up(len(self.heap) - 1)  # Reordenar hacia arriba

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                # Intercambiar si el hijo es menor que el padre
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent  # Seguir subiendo
            else:
                break

# 🧪 Test cases
def test_min_heap_insert():
    h = MinHeap()
    h.insert(5); print("🍀 Test 1:", h.heap == [5])
    h.insert(3); print("🍀 Test 2:", h.heap == [3,5])
    h.insert(4); print("🍀 Test 3:", h.heap == [3,5,4])
    h.insert(1); print("🍀 Test 4:", h.heap == [1,3,4,5])
    # 🍀 Test 5: parent ≤ children
    valid = all(
        (h.heap[i] <= h.heap[2*i+1] if 2*i+1 < len(h.heap) else True)
        and (h.heap[i] <= h.heap[2*i+2] if 2*i+2 < len(h.heap) else True)
        for i in range(len(h.heap))
    )
    print("🍀 Test 5:", valid)

test_min_heap_insert()
