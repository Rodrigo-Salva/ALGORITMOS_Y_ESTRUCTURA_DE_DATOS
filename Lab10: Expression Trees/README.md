# Lab 10: Expression Trees

## 🧠 Capabilities

* Build expression trees using Python
* Perform basic mathematical equation evaluations

## 🔐 Safety Guidelines

* Ensure a secure and respectful work environment
* Do not consume food in the lab
* Keep the workspace clean and organized

## 📚 Preparation

Students should review the provided material before beginning the lab.

## 💻 Resources

* A computer with Python installed

## 📝 Instructions

* The lab development must be distributed among team members.
* Submit the project in a single GitHub repository.
* Provide evidence of your final project in the "Development" section with the following format:

```
Student Name  
Development Title  
Screenshot of the result  
Prompt engineering (If applicable)  
Entered prompt and/or screenshot  
Interaction prompt and/or screenshot  
Code  
→ Developed code (Optional: diagram)  
→ Line-by-line explanation with comments  
Test cases  
```

* All documentation and comments must be written in **English**.
* Include a screenshot of your project structure in **Visual Studio Code**.

---

## 🧩 Technical Challenges

### ✅ Challenge 1: Convert Infix to Postfix

* **Goal:** Convert an infix expression to postfix notation
* **Techniques:** Use a stack, handle operator precedence and parentheses

**Test Case:**

```python
# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # ➕ Simple operation

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # 📊 Precedence test

# Test 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # 🔗 Parentheses

# Test 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # 🧮 Complex

# Test 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # 🔤 Variables

```

### ✅ Challenge 2: Build Expression Tree from Postfix

* **Goal:** Construct an expression tree from a postfix list
* **Techniques:** Stack-based tree construction

**Test Case:**

```python
# ✅ Test cases
# Test 1: Simple addition
# Input: 2 3 +
# Tree:    +
#         / \
#        2   3
tokens1 = ['2', '3', '+']
tree1 = build_expression_tree(tokens1)
print(tree1.value == '+' and tree1.left.value == '2' and tree1.right.value == '3')  # 🌱 Simple tree

# Test 2: Complex expression
# Input: 2 3 4 * +
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tokens2 = ['2', '3', '4', '*', '+']
tree2 = build_expression_tree(tokens2)
print(tree2.value == '+' and tree2.left.value == '2' and tree2.right.value == '*')  # 📊 Operator precedence

# Test 3: Nested operations
# Input: 1 2 + 3 4 - *
# Tree:    *
#         / \
#        +   -
#       / \ / \
#      1  2 3  4
tokens3 = ['1', '2', '+', '3', '4', '-', '*']
tree3 = build_expression_tree(tokens3)
print(tree3.value == '*' and tree3.left.value == '+' and tree3.right.value == '-')  # 🔗 Nested operations

# Test 4: Expression with variables
# Input: a b c * +
# Tree:    +
#         / \
#        a   *
#           / \
#          b   c
tokens4 = ['a', 'b', 'c', '*', '+']
tree4 = build_expression_tree(tokens4)
print(tree4.value == '+' and tree4.left.value == 'a' and tree4.right.value == '*')  # 🔤 Variable tree

# Test 5: More complex expression
# Input: a b + c d - /
# Tree:    /
#         / \
#        +   -
#       / \ / \
#      a  b c  d
tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
tree5 = build_expression_tree(tokens5)
print(tree5.value == '/' and tree5.left.value == '+' and tree5.right.value == '-')  # 🧮 Complex tree

```

### ✅ Challenge 3: Expression Tree Evaluation

* **Goal:** Recursively evaluate an expression tree
* **Techniques:** Post-order traversal with arithmetic evaluation

**Test Case:**

```python
# ✅ Test cases
# Test 1: Simple addition
# Tree:    +
#         / \
#        2   3
# Result: 5
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(evaluate_expression_tree(node1) == 5)  # ➕ Basic addition

# Test 2: Multiplication
# Tree:    *
#         / \
#        4   5
# Result: 20
node2 = Node('*')
node2.left = Node('4')
node2.right = Node('5')
print(evaluate_expression_tree(node2) == 20)  # ✖️ Multiplication

# Test 3: Combined operations
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
# Result: 14
node3 = Node('+')
node3.left = Node('2')
node3.right = Node('*')
node3.right.left = Node('3')
node3.right.right = Node('4')
print(evaluate_expression_tree(node3) == 14)  # 🔢 Combined operations

# Test 4: Division
# Tree:    /
#         / \
#        8   4
# Result: 2
node4 = Node('/')
node4.left = Node('8')
node4.right = Node('4')
print(evaluate_expression_tree(node4) == 2)  # ➗ Division

# Test 5: Complex tree
# Tree:      *
#          /   \
#         +     -
#        / \   / \
#       1   2 8   3
# Result: 15
node5 = Node('*')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('1')
node5.left.right = Node('2')
node5.right.left = Node('8')
node5.right.right = Node('3')
print(evaluate_expression_tree(node5) == 15)  # 🧮 Complex calculation

```

### ✅ Challenge 4: Tree Traversal Methods

* **Goal:** Implement inorder, preorder, and postorder traversals
* **Techniques:** Use recursion for all methods

**Test Case:**

```python
# ✅ Test cases
# Test 1: Simple expression tree
# Tree:    +
#         / \
#        2   3
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(inorder_traversal(node1) == ['2', '+', '3'])  # 📝 Infix notation
print(preorder_traversal(node1) == ['+', '2', '3'])  # 📝 Prefix notation
print(postorder_traversal(node1) == ['2', '3', '+'])  # 📝 Postfix notation

# Test 2: More complex tree
# Tree:    +
#         / \
#        *   5
#       / \
#      2   3
node2 = Node('+')
node2.left = Node('*')
node2.right = Node('5')
node2.left.left = Node('2')
node2.left.right = Node('3')
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])  # 📝 Infix with precedence
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])  # 📝 Prefix order
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])  # 📝 Postfix order

# Test 3: Single node tree
# Tree: X
node3 = Node('X')
print(inorder_traversal(node3) == ['X'])  # 🌱 Single node inorder
print(preorder_traversal(node3) == ['X'])  # 🌱 Single node preorder
print(postorder_traversal(node3) == ['X'])  # 🌱 Single node postorder

# Test 4: Empty tree
# Tree: None
print(inorder_traversal(None) == [])  # 📭 Empty tree inorder
print(preorder_traversal(None) == [])  # 📭 Empty tree preorder
print(postorder_traversal(None) == [])  # 📭 Empty tree postorder

# Test 5: Complex nested tree
# Tree:      /
#          /   \
#         +     -
#        / \   / \
#       a   b c   d
node5 = Node('/')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('a')
node5.left.right = Node('b')
node5.right.left = Node('c')
node5.right.right = Node('d')
print(inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'])  # 🧮 Complex inorder
print(preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'])  # 🧮 Complex preorder
print(postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/'])  # 🧮 Complex postorder

```

### ✅ Challenge 5: Expression Tree Simplification

* **Goal:** Extend the evaluation function to handle variables with assigned values
* **Techniques:** Dictionary-based value lookup during evaluation

**Test Case:**

```python
# ✅ Test cases
# Test 1: All constants
# Tree:    +        Result: 5
#         / \
#        2   3
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # 🔢 Full evaluation

# Test 2: Mixed variables and constants
# Tree:    +        Result:    +
#         / \               / \
#        x   3             x   3
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # 🔤 Variable preserved

# Test 3: Partial simplification
# Tree:      +          Result:    +
#          /   \                 /   \
#         *     -               6     5
#        / \   / \
#       2   3 8   3
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')  # 📊 Subtree simplification

# Test 4: All variables
# Tree:    +        Result:    + (unchanged)
#         / \               / \
#        x   y             x   y
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # 🔤 No simplification

# Test 5: Complex nested simplification
# Tree:          +               Result:    +
#              /   \                      /   \
#             /     \                    5     *
#            / \     \                        / \
#           2   3     *                      z   4
#                    / \
#                   z   4
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')  # 🧮 Mixed simplification

```

---

## ✅ Final Notes

Ensure code readability and thorough commenting. Maintain team communication throughout the lab and follow all submission guidelines.

Good luck and have fun building your expression trees! 🌳💻
