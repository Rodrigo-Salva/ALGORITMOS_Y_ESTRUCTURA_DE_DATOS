class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert value and maintain heap property"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """Move the value up to restore heap property"""
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] <= self.heap[index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def delete_min(self):
        """Remove and return the smallest element"""
        if not self.heap:  # Check if heap is empty
            return None
        
        if len(self.heap) == 1:  # Only one element
            return self.heap.pop()
        
        # Store minimum value (root)
        min_value = self.heap[0]
        # Move last element to root
        self.heap[0] = self.heap.pop()
        # Restore heap property from root
        self._heapify_down(0)
        return min_value

    def _heapify_down(self, index):
        """Restore heap property downward"""
        while True:
            smallest = index
            left_child = 2 * index + 1   # Left child index
            right_child = 2 * index + 2  # Right child index
            
            # Find smallest among parent and children
            if (left_child < len(self.heap) and 
                self.heap[left_child] < self.heap[smallest]):
                smallest = left_child
            
            if (right_child < len(self.heap) and 
                self.heap[right_child] < self.heap[smallest]):
                smallest = right_child
            
            # If parent is smallest, heap property is satisfied
            if smallest == index:
                break
            
            # Swap with smaller child
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest

def test_min_heap_delete_min():
    """Test MinHeap delete_min operation and heap property maintenance"""
    print("Testing MinHeap delete_min operation:")
    
    # Test 1: Delete from empty heap
    h = MinHeap()
    result = h.delete_min()
    print("🧹 Test 1:", result is None)
    # Expected: None - empty heap should return None
    
    # Test 2: Delete from single element heap
    h.heap = [1]
    result = h.delete_min()
    test2_passed = result == 1 and h.heap == []
    print("🧹 Test 2:", test2_passed)
    # Expected: return 1, heap becomes []
    
    # Test 3: Delete from three element heap
    h.heap = [1,3,2]
    result = h.delete_min()
    test3_passed = result == 1 and h.heap == [2,3]
    print("🧹 Test 3:", test3_passed)
    # Expected: return 1, heap becomes [2,3]
    
    # Test 4: Delete from four element heap
    h.heap = [1,3,4,5]
    result = h.delete_min()
    test4_passed = result == 1 and h.heap == [3,5,4]
    print("🧹 Test 4:", test4_passed)
    # Expected: return 1, heap becomes [3,5,4]
    
    # Test 5: Delete from larger heap
    h.heap = [1,2,3,4,5]
    result = h.delete_min()
    test5_passed = result == 1
    print("🧹 Test 5:", test5_passed)
    # Expected: return 1, verify minimum was removed

# Execute test
test_min_heap_delete_min()
