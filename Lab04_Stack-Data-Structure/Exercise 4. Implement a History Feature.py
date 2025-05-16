class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def type_text(self, new_text):
        self.history.append(self.text)
        self.text += new_text

    def delete_last_char(self):
        if self.text:
            self.history.append(self.text)
            self.text = self.text[:-1]

    def undo(self):
        if self.history:
            self.text = self.history.pop()

    def get_text(self):
        return self.text


# Example usage
editor = TextEditor()
editor.type_text("Hello")
editor.type_text(" World")
editor.delete_last_char()
editor.undo()
print(editor.get_text())  # Output: "Hello World"

# Test Case 1
editor = TextEditor()
editor.type_text("Hi")
editor.type_text(" there")
editor.undo()
print(editor.get_text())  # Expected: "Hi"

# Test Case 2
editor = TextEditor()
editor.type_text("Test")
editor.delete_last_char()
editor.undo()
print(editor.get_text())  # Expected: "Test"

# Test Case 3
editor = TextEditor()
editor.type_text("A")
editor.delete_last_char()
editor.type_text("B")
editor.undo()
print(editor.get_text())  # Expected: ""
