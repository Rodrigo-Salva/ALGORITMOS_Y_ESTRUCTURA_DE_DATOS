# Lab 11: Binary Search Tree 🌳

## 🎯 Capacidades

- **Diseñar e implementar** árboles BST
- **Aplicar** los árboles BST para la resolución de problemas

## 🛡️ Seguridad

- ✅ Generar un ambiente seguro
- 🚫 Evitar el consumo de alimentos
- 🧹 Dejar el ambiente ordenado y limpio

## 📚 Preparación

El alumno debe revisar previamente el material cargado.

## 🛠️ Recursos

- 💻 Computadora

## 📋 Instrucciones

- Se debe distribuir el desarrollo del laboratorio entre los integrantes
- Subir el proyecto en un solo repositorio de GitHub
- Poner evidencia de su proyecto finalizando en la sección de desarrollo con el siguiente formato:

### 📝 Formato de Entrega

**Nombre del alumno**
- Título del desarrollo
- Captura del resultado
- Prompt engineering (Si aplica)
- Prompt ingresado y/o captura
- Prompt de interacción y/o captura

**Código**
- Código desarrollado (Diagrama opcional)
- Explicación de línea por línea con comentarios

**Casos de prueba**

> ⚠️ **Importante:** Todo debe ser desarrollado en inglés.

**Captura de la estructura de tu proyecto en VSC.**

---

# 🌳✨ Binary Search Tree Technical Challenges

**by @elliotgaramendi** 👨‍💻

Welcome to this interactive journey through Binary Search Trees (BST) 🚀. These fun and practical challenges will boost your coding skills, reinforce algorithmic thinking 🧠, and prepare you for interviews and real-world applications 💼.

## 🌟 Visualizando BSTs con ASCII Art

¡Una imagen vale más que mil palabras! 👀 Aquí usamos arte ASCII para representar cómo luce un árbol binario y sus operaciones 🔍

### 🧱 Estructura de un Binary Search Tree

```
       8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

### 🔍 Propiedades del BST:

- Todos los nodos del subárbol izquierdo de un nodo tienen valores **menores**
- Todos los nodos del subárbol derecho tienen valores **mayores**
- El recorrido inorder de este árbol nos da los valores ordenados: 
  > 👉 **[1, 3, 4, 6, 7, 8, 10, 13, 14]**

### 🔁 Visualizando Traversals (Recorridos)

#### 1️⃣ Inorder (left ➡️ root ➡️ right): 📝
```
1 → 3 → 4 → 6 → 7 → 8 → 10 → 13 → 14
```

#### 2️⃣ Preorder (root ➡️ left ➡️ right): 🚀
```
8 → 3 → 1 → 6 → 4 → 7 → 10 → 14 → 13
```

#### 3️⃣ Postorder (left ➡️ right ➡️ root): 🧠
```
1 → 4 → 7 → 6 → 3 → 13 → 14 → 10 → 8
```

### 🧮 Visual Simplification of an Expression Tree

```
        +
       /   \
      *     5
     / \
    2   3
```

**🌱 Simplificación:**
1. Se evalúa el subárbol * → 2 * 3 = 6
2. El árbol se transforma en:
   ```
       +
       / \
      6   5
   ```
3. **📘 Resultado:** 6 + 5 = 11

---

## 🧱 Common Base Code (Node + BinarySearchTree) 🌱

```python
class Node:
    """🌱 Node for Binary Search Tree"""
    def __init__(self, value):
        self.value = value  # 🔢 Node value
        self.left = None    # 🌿 Left child
        self.right = None   # 🌿 Right child

class BinarySearchTree:
    """🌳 Binary Search Tree with basic functionality"""
    def __init__(self):
        self.root = None  # 📭 Initially empty

    def insert(self, value):
        """🧩 Insert a value into the BST"""
        if self.root is None:
            self.root = Node(value)  # 🌱 First node
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        """🔄 Recursive insert logic"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)  # 👈 Go left
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)  # 👉 Go right
            else:
                self._insert(node.right, value)

    def build_from_list(self, values):
        """📦 Build BST from a list of values"""
        for val in values:
            self.insert(val)
```

---

## ✅ Challenge 1: 🎯 Find Range Values in BST

**Problem:** Find all values in a BST that fall within a given range [min_val, max_val] 🔍

**Input:** BST root node and two integers min_val, max_val  
**Output:** List of all values in the range, sorted in ascending order 📈

### Approach:
- Use inorder traversal to visit nodes in sorted order 🔄
- Only traverse left subtree if current value > min_val 📉
- Only traverse right subtree if current value < max_val 📈
- Add current value if it lies within the range 🎯

```python
class BinarySearchTree(BinarySearchTree):
    def range_query(self, min_val, max_val):
        """🎯 Find all values in BST within given range"""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_range_query():
    bst1 = BinarySearchTree()
    bst1.build_from_list([7, 3, 11, 1, 5, 9, 13])
    print("🧪 Test 1:", bst1.range_query(5, 10) == [5, 7, 9])  # ✅

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 4, 8, 2])
    print("🧪 Test 2:", bst2.range_query(1, 10) == [2, 4, 6, 8])  # 🌐

    bst3 = BinarySearchTree()
    bst3.build_from_list([20, 10, 30])
    print("🧪 Test 3:", bst3.range_query(1, 5) == [])  # 📭

    bst4 = BinarySearchTree()
    bst4.build_from_list([15])
    print("🧪 Test 4:", bst4.range_query(10, 20) == [15])  # 🌱

    bst5 = BinarySearchTree()
    bst5.build_from_list([15, 10, 20, 5, 25])
    print("🧪 Test 5:", bst5.range_query(10, 20) == [10, 15, 20])  # 🔗

# 🚀 Run all tests
test_range_query()
```

---

## ✅ Challenge 2: 🧬 Find Lowest Common Ancestor (LCA)

**Problem:** Find the lowest common ancestor of two nodes in a BST 🌲

**Input:** BST root node and two target values val1 and val2  
**Output:** Value of the lowest common ancestor node 🎯

### Approach:
- Start from the root and move down the tree 🧭
- If both values are smaller than current → go left 👈
- If both values are larger → go right 👉
- If they diverge, current node is the LCA 🌟

```python
class BinarySearchTree(BinarySearchTree):
    def find_lca(self, val1, val2):
        """🧬 Find lowest common ancestor of two values in the BST"""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_find_lca():
    bst1 = BinarySearchTree()
    bst1.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 1:", bst1.find_lca(2, 8) == 6)  # 🌲 Root is LCA

    bst2 = BinarySearchTree()
    bst2.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 2:", bst2.find_lca(0, 4) == 2)  # 📚 Subtree LCA

    bst3 = BinarySearchTree()
    bst3.build_from_list([6, 2, 8, 0, 4, 7, 9, 3, 5])
    print("🧪 Test 3:", bst3.find_lca(2, 3) == 2)  # 🔗 Ancestor node

    bst4 = BinarySearchTree()
    bst4.build_from_list([5, 3, 7])
    print("🧪 Test 4:", bst4.find_lca(5, 5) == 5)  # 🎯 Same node

    bst5 = BinarySearchTree()
    bst5.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 5:", bst5.find_lca(1, 3) == 2)  # 🌿 Leaf node LCA

# 🚀 Run all tests
test_find_lca()
```

---

## ✅ Challenge 3: 🧪 Validate BST Property

**Problem:** Determine if a binary tree maintains the BST property ✅

**Input:** Root node of a binary tree 🌱  
**Output:** Boolean indicating if the tree is a valid BST 🧼

### Approach:
- Use recursive validation with min and max bounds 🔁
- For each node, ensure value is within valid range ⚖️
- Left subtree: values must be less than current 👈
- Right subtree: values must be greater than current 👉

```python
class BinarySearchTree(BinarySearchTree):
    def is_valid_bst(self):
        """🧼 Check if the tree satisfies the BST property"""
        def validate(node, min_val, max_val):
            # Your solution here 🛠️
            pass
        return validate(self.root, float('-inf'), float('inf'))

# 🧪 Test cases
def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 1:", bst1.is_valid_bst() == True)  # ✅ Valid tree

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # ❌ Incorrect: left > root
    bst2.root.right = Node(7)
    print("🧪 Test 2:", bst2.is_valid_bst() == False)  # ❌ Left violation

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # ❌ Incorrect: right < root
    print("🧪 Test 3:", bst3.is_valid_bst() == False)  # ❌ Right violation

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("🧪 Test 4:", bst4.is_valid_bst() == True)  # 🌱 Single node

    bst5 = BinarySearchTree()
    print("🧪 Test 5:", bst5.is_valid_bst() == True)  # 📭 Empty tree

# 🚀 Run tests
test_is_valid_bst()
```

---

## ✅ Challenge 4: 🏅 Find Kth Smallest Element

**Problem:** Find the kth smallest element in a BST without converting to array 🧮

**Input:** BST root node and integer k (1-indexed) 🔢  
**Output:** Value of the kth smallest element 🎯

### Approach:
- Use inorder traversal (yields sorted elements) 🔄
- Keep a counter to track elements visited 📊
- Return value when counter reaches k ✅
- Apply early termination for efficiency ⚡

```python
class BinarySearchTree(BinarySearchTree):
    def kth_smallest(self, k):
        """📊 Find the kth smallest value in the BST"""
        # Your solution here 🛠️
        pass

# 🧪 Test cases
def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print("🧪 Test 1:", bst1.kth_smallest(2) == 2)  # 🎯

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 2:", bst2.kth_smallest(1) == 2)  # 📉 First (min)
    print("🧪 Test 3:", bst2.kth_smallest(7) == 8)  # 📈 Last (max)

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 Middle

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print("🧪 Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Single node

# 🚀 Run tests
test_kth_smallest()
```

---

## ✅ Challenge 5: 🔄 Convert BST to Sorted Doubly Linked List

**Problem:** Convert a BST to a sorted circular doubly linked list in-place ♻️

**Input:** Root node of a BST  
**Output:** Head of the converted doubly linked list 🔗

### Approach:
- Use inorder traversal to visit nodes in sorted order 📈
- Update pointers:
  - `left` ⬅️ becomes previous
  - `right` ➡️ becomes next
- Connect first and last nodes to make it circular ⭕
- Return the head of the new list 🎉

```python
class BinarySearchTree(BinarySearchTree):
    def bst_to_dll(self):
        """🔁 Convert BST to sorted circular doubly linked list"""
        # Your solution here 🛠️
        pass

# ✅ DLL validator helper
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    return values == expected_values

# 🧪 Test cases
def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 🌳

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)  # 🌱

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)  # 📭 Empty tree

# 🚀 Run tests
test_bst_to_dll()
```

---

## 🎉 ¡Felicidades!

Has completado todos los desafíos del Binary Search Tree. Estos ejercicios te han ayudado a:

- 🧠 Fortalecer tu pensamiento algorítmico
- 💪 Mejorar tus habilidades de programación
- 🎯 Prepararte para entrevistas técnicas
- 🚀 Aplicar BSTs en problemas del mundo real

¡Sigue practicando y explorando más estructuras de datos! 🌟
