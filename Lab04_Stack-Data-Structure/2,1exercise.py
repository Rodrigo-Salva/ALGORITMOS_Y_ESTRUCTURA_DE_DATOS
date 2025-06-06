class ArrayStack:
    """Stack implementation using a fixed-size array."""
    
    def __init__(self, capacity=10):
        """Initialize empty stack with fixed capacity."""
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1  # Index of top element, -1 means empty stack
    
    def is_empty(self):
        """Check if stack is empty."""
        return self.top == -1
    
    def is_full(self):
        """Check if stack is full."""
        return self.top == self.capacity - 1
    
    def push(self, item):
        """Add item to the top of the stack."""
        if self.is_full():
            print("Warning: Stack is full, cannot add more items.")
            return False  
        self.top += 1
        self.data[self.top] = item
        return True
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            print("Warning: Stack is empty, cannot pop.")
            return None  
        item = self.data[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            print("Warning: Stack is empty, cannot peek.")
            return None 
        return self.data[self.top]
    
    def size(self):
        """Return the number of items in the stack."""
        return self.top + 1
    
    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack: []"
        
        items = [str(self.data[i]) for i in range(self.top + 1)]
        return f"Stack: [{', '.join(items)}]"


def test_array_stack():
    """Test fixed array stack implementation with basic operations."""
    print("="*40)
    print("Test: Basic operations with fixed array stack")
    print("="*40)
    
    stack = ArrayStack(5)
    
    print(f"Empty stack: {stack}")
    print(f"Is empty? {stack.is_empty()}")

    # Push operations
    for i in range(1, 4):
        stack.push(i * 10)
        print(f"After push({i*10}): {stack}")
    
    # Test peek
    print(f"Peek: {stack.peek()}")
    
    # Test pop
    print(f"Pop: {stack.pop()}")
    print(f"After pop: {stack}")
    
    # Test full stack
    stack.push(40)
    stack.push(50)
    print(f"Full stack: {stack}")
    
    try:
        stack.push(60)  # Should raise OverflowError
        print("Push succeeded unexpectedly")
    except OverflowError as e:
        print(f"Error as expected: {e}")
    
    # Empty the stack
    while not stack.is_empty():
        print(f"Pop: {stack.pop()}")
    
    print(f"Final stack: {stack}")
    print("All array stack tests passed!")

# Example usage
if __name__ == "__main__":
    test_array_stack()
