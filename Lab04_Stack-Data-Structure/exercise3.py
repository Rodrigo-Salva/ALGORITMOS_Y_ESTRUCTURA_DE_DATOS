class MinStack:
    """Stack that supports retrieving the minimum element in O(1) time."""
    
    def __init__(self):
        self.stack = []        # Main stack to store elements
        self.min_stack = []    # Auxiliary stack to store the current minimums
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, x):
        """Push element onto the stack."""
        self.stack.append(x)
        # If min_stack is empty or new element is smaller or equal, push to min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        return True
    
    def pop(self):
        """Remove the element on top of the stack."""
        if self.is_empty():
            print("Warning: Stack is empty. Cannot pop.")
            return None
        popped = self.stack.pop()
        # If popped value is current min, pop it from min_stack too
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped
    
    def top(self):
        """Get the top element."""
        if self.is_empty():
            print("Warning: Stack is empty. No top element.")
            return None
        return self.stack[-1]
    
    def get_min(self):
        """Retrieve the minimum element in the stack."""
        if not self.min_stack:
            print("Warning: Stack is empty. No minimum element.")
            return None
        return self.min_stack[-1]
    
    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack: {self.stack}, MinStack: {self.min_stack}"


# Test function
def test_min_stack():
    print("="*45)
    print("Test: Stack with getMin() functionality")
    print("="*45)
    
    stack = MinStack()
    
    print("Initial state:", stack)
    
    stack.push(5)
    print("After push(5):", stack)
    stack.push(3)
    print("After push(3):", stack)
    stack.push(7)
    print("After push(7):", stack)
    stack.push(2)
    print("After push(2):", stack)
    
    print(f"Current min: {stack.get_min()}")
    print(f"Top element: {stack.top()}")
    
    print("Pop:", stack.pop())
    print("After pop:", stack)
    print(f"Current min: {stack.get_min()}")
    
    print("Pop:", stack.pop())
    print("After pop:", stack)
    print(f"Current min: {stack.get_min()}")
    
    print("Pop:", stack.pop())
    print("After pop:", stack)
    print(f"Current min: {stack.get_min()}")
    
    print("Pop:", stack.pop())
    print("After pop:", stack)
    print(f"Current min: {stack.get_min()}")
    
    print("All tests for getMin stack completed!")


# Example usage
if __name__ == "__main__":
    test_min_stack()
