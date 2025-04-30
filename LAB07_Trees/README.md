# LAB07: Binary Trees 🌳
**Course:** Algoritmos y Estructuras de Datos  
**Lab:** GLAB-S07: Trees

---

## 🌐 Repository
[GitHub Repository](https://github.com/Rodrigo-Salva/ALGORITMOS_Y_ESTRUCTURA_DE_DATOS/tree/main/LAB07_Trees)

---

## ✅ Objective
Implement binary tree structures and operations using Python, applying them to various algorithmic challenges.

---

## 📚 Contents
- Tree Basics and Terminology
- Binary Tree Implementation
- Tree Traversals
- Extended Operations (Height, Size, Print)
- Expression Tree Evaluation
- Directory Tree Representation
- Syntax Tree for Compiler
- Challenges & Solutions (Height, Leaves, Mirror, Level Order, Balance)

---

## 👨‍💼 Developed Challenges

### Challenge 1: Tree Height Calculation

#### Prompt:
Write a function to calculate the height of a binary tree (number of edges from root to the deepest leaf).

#### Code:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    if root is None:
        return -1
    return 1 + max(tree_height(root.left), tree_height(root.right))
```

#### Explanation:
- `TreeNode`: defines the structure of each node.
- `tree_height`: uses recursion to find the max depth between left and right subtrees.
- `+1` accounts for the current level.

#### Test Cases:
```python
# Empty tree
assert tree_height(None) == -1

# Single node
assert tree_height(TreeNode(1)) == 0

# Left-skewed tree
n = TreeNode(1)
n.left = TreeNode(2)
n.left.left = TreeNode(3)
assert tree_height(n) == 2

# Perfect binary tree
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
r.right.right = TreeNode(7)
assert tree_height(r) == 2
```

---

### Challenge 2: Count Leaf Nodes

#### Prompt:
Count how many leaf nodes exist in a binary tree.

#### Code:
```python
def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)
```

#### Test Cases:
- Tree with 3 leaves: 4, 5, and 3
- Empty tree: 0
- Tree with one node: 1

---

### Challenge 3: Tree Mirroring

#### Prompt:
Mirror a binary tree (swap left and right children recursively).

#### Code:
```python
def mirror_tree(root):
    if not root:
        return None
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root
```

---

### Challenge 4: Level Order Traversal

#### Prompt:
Print the tree nodes level-by-level (BFS).

#### Code:
```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
```

---

### Challenge 5: Check if a Binary Tree is Balanced

#### Prompt:
Return True if the tree is balanced (height difference between left and right is ≤ 1).

#### Code:
```python
def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
    return height(root) != -1
```

---

## 📝 Conclusions
- Binary trees allow structured and hierarchical data storage.
- Understanding traversal types is key to various operations.
- Python makes tree operations clean and modular.
- Recursive techniques are powerful tools for manipulating trees.

---

## 📊 Key Learnings
- TreeNode structures and object-oriented implementation
- Traversals: Preorder, Inorder, Postorder, Level Order
- Functional operations: height, size, balance, mirror
- Real-world applications: expressions, file systems, syntax parsing

---

## ✨ Final Note
Mastering tree structures unlocks deeper algorithmic understanding essential in software engineering, AI, and data structures. This lab was key to reinforcing recursion, design, and problem-solving skills.

---

🌐 [Return to Repository](https://github.com/Rodrigo-Salva/ALGORITMOS_Y_ESTRUCTURA_DE_DATOS/tree/main/LAB07_Trees)

