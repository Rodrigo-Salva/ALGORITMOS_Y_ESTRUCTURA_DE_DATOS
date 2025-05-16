class ArrayStack:
    def __init__(self, capacity=100):
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            print("Warning: Stack is full.")
            return False
        self.top += 1
        self.data[self.top] = item
        return True

    def pop(self):
        if self.is_empty():
            print("Warning: Stack is empty.")
            return None
        item = self.data[self.top]
        self.top -= 1
        return item

def reverse_string(input_str):
    if not input_str:
        return ""

    stack = ArrayStack(len(input_str))
    for char in input_str:
        stack.push(char)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

if __name__ == "__main__":
    test_input = "OpenAI"
    print(f"Original string: {test_input}")
    print(f"Reversed string: {reverse_string(test_input)}")
