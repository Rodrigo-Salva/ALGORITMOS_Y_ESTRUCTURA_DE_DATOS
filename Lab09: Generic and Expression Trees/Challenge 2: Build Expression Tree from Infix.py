class ExpressionNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class ExpressionTree:
    """Expression tree implementation"""
    
    def __init__(self):
        self.root = None

    @classmethod
    def from_infix(cls, tokens):
        """Build expression tree from infix notation"""

        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def to_postfix(tokens):
            output = []
            stack = []
            for token in tokens:
                if token.isalnum():  # operand (numbers or variables)
                    output.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()  # remove '('
                else:  # operator
                    while stack and precedence(stack[-1]) >= precedence(token):
                        output.append(stack.pop())
                    stack.append(token)
            while stack:
                output.append(stack.pop())
            return output

        def build_tree(postfix_tokens):
            stack = []
            for token in postfix_tokens:
                if token.isalnum():
                    node = ExpressionNode(token)
                    stack.append(node)
                else:
                    right = stack.pop()
                    left = stack.pop()
                    node = ExpressionNode(token, left, right)
                    stack.append(node)
            return stack[0]

        postfix = to_postfix(tokens)
        tree = cls()
        tree.root = build_tree(postfix)
        return tree

# ✅ Test cases

# Test 1: Simple addition
# Input: 2 + 3
# Tree:    +
#         / \
#        2   3
tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # 🌱 Simple tree

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')  # 📊 Precedence structure

# Test 3: Parentheses change structure
# Input: (2 + 3) * 4
# Tree:    *
#         / \
#        +   4
#       / \
#      2   3
tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')  # 🔗 Parentheses effect

# Test 4: Variables in expression
# Input: x + y * z
# Tree:    +
#         / \
#        x   *
#           / \
#          y   z
tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
print(tree4.root.value == '+' and tree4.root.right.value == '*')  # 🔤 Variable tree

# Test 5: Complex nested expression
# Input: (a + b) / (c - d)
# Tree:      /
#          /   \
#         +     -
#        / \   / \
#       a   b c   d
tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')  # 🧮 Complex tree
