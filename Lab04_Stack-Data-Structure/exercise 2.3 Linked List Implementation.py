class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")

        item = self.head.data
        self.head = self.head.next
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow - stack is empty")
        return self.head.data

    def size(self):
        return self.count

    def __str__(self):
        if self.is_empty():
            return "Stack: []"

        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next

        return f"Stack: [{', '.join(items)}]"


def test_linked_list_stack():
    print("Test: Linked list stack implementation")
    stack = LinkedListStack()

    print(f"Empty stack: {stack}")

    for i in range(1, 6):
        stack.push(i * 10)
        print(f"After push({i*10}): {stack}")

    print(f"Stack size: {stack.size()}")
    print(f"Top element: {stack.peek()}")

    while not stack.is_empty():
        print(f"Pop: {stack.pop()}, Remaining: {stack}")

    try:
        stack.peek()
    except IndexError as e:
        print(f"Expected error: {e}")

    print("All linked list stack tests passed!")


if __name__ == "__main__":
    test_linked_list_stack()
