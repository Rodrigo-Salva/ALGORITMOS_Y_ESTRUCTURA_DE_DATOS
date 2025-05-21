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
# Challenge 1 Test
infix_expr = "a+b*(c-d)"
expected_postfix = ['a', 'b', 'c', 'd', '-', '*', '+']
result = infix_to_postfix(infix_expr)
print("Test 1 - Postfix:", result)
assert result == expected_postfix, "❌ Test 1 Failed!"
print("✅ Test 1 Passed!")
```

### ✅ Challenge 2: Build Expression Tree from Postfix

* **Goal:** Construct an expression tree from a postfix list
* **Techniques:** Stack-based tree construction

**Test Case:**

```python
# Challenge 2 Test
postfix = ['a', 'b', 'c', 'd', '-', '*', '+']
tree = build_expression_tree(postfix)
print("Test 2 - Root Node:", tree.value)
assert tree.value == '+', "❌ Test 2 Failed! Root should be '+'"
print("✅ Test 2 Passed!")
```

### ✅ Challenge 3: Evaluate Expression Tree

* **Goal:** Recursively evaluate an expression tree
* **Techniques:** Post-order traversal with arithmetic evaluation

**Test Case:**

```python
# Challenge 3 Test
# Use numeric postfix for evaluation
numeric_postfix = ['3', '4', '2', '-', '*', '5', '+']  # 3 * (4 - 2) + 5 = 11
tree = build_expression_tree(numeric_postfix)
result = evaluate_tree(tree)
print("Test 3 - Evaluation Result:", result)
assert result == 11, "❌ Test 3 Failed!"
print("✅ Test 3 Passed!")
```

### ✅ Challenge 4: Tree Traversal Methods

* **Goal:** Implement inorder, preorder, and postorder traversals
* **Techniques:** Use recursion for all methods

**Test Case:**

```python
# Challenge 4 Test
print("Test 4 - Traversals")

print("Inorder traversal:", end=" ")
inorder(tree)
print()

print("Preorder traversal:", end=" ")
preorder(tree)
print()

print("Postorder traversal:", end=" ")
postorder(tree)
print()

print("✅ Traversal methods ran without error!")
```

### ✅ Challenge 5: Handle Variables in Expression Tree

* **Goal:** Extend the evaluation function to handle variables with assigned values
* **Techniques:** Dictionary-based value lookup during evaluation

**Test Case:**

```python
# Challenge 5 Test
postfix = ['x', 'y', '2', '-', '*', 'z', '+']  # x * (y - 2) + z
tree = build_expression_tree(postfix)
variables = {'x': 3, 'y': 4, 'z': 5}
result = evaluate_tree_with_variables(tree, variables)
print("Test 5 - Evaluation with variables:", result)
assert result == 11, "❌ Test 5 Failed!"  # 3 * (4 - 2) + 5 = 6 + 5 = 11
print("✅ Test 5 Passed!")
```

---

## ✅ Final Notes

Ensure code readability and thorough commenting. Maintain team communication throughout the lab and follow all submission guidelines.

Good luck and have fun building your expression trees! 🌳💻
