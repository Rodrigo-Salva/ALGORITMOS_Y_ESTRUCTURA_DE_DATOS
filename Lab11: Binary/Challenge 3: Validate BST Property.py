from collections import deque

# Definición del nodo de árbol
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Validación del BST
def is_valid_bst(root):
    """Check if binary tree is a valid BST"""
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

# Construcción de árbol a partir de lista (orden por niveles)
def build_tree(values):
    """Build binary tree from list (level order)"""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# Árbol inválido - violación por la izquierda
def build_invalid_tree1():
    # Tree:    5
    #         / \
    #        6   7  (6 > 5, invalido)
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.right = TreeNode(7)
    return root

# Árbol inválido - violación por la derecha
def build_invalid_tree2():
    # Tree:    5
    #         / \
    #        3   4  (4 < 5, invalido)
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    return root

# ✅ Casos de prueba
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)   # ✅ Válido
print(is_valid_bst(build_invalid_tree1()) == False)             # ❌ Violación izquierda
print(is_valid_bst(build_invalid_tree2()) == False)             # ❌ Violación derecha
print(is_valid_bst(build_tree([42])) == True)                   # 🌱 Nodo único válido
print(is_valid_bst(None) == True)                               # 📭 Árbol vacío válido
