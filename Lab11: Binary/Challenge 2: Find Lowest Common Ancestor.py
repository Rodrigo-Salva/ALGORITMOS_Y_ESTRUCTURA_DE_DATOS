class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    """Inserta un valor en el BST"""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def build_bst(values):
    """Construye un BST a partir de una lista de valores"""
    root = None
    for val in values:
        root = insert_bst(root, val)
    return root

def find_lca(root, val1, val2):
    """Encuentra el Ancestro Común Más Bajo (LCA) en un BST"""
    while root:
        if val1 < root.val and val2 < root.val:
            root = root.left  # Ambos están a la izquierda
        elif val1 > root.val and val2 > root.val:
            root = root.right  # Ambos están a la derecha
        else:
            return root.val  # Se dividen o uno es el actual
    return None
# Test 1: Valores en subárboles diferentes
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 8) == 6)  # ✅

# Test 2: Valores en mismo subárbol
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 0, 4) == 2)  # ✅

# Test 3: Un valor es ancestro del otro
print(find_lca(build_bst([6, 2, 8, 0, 4, 7, 9, 3, 5]), 2, 3) == 2)  # ✅

# Test 4: Mismos valores
print(find_lca(build_bst([5, 3, 7]), 5, 5) == 5)  # ✅

# Test 5: Valores en nivel de hoja
print(find_lca(build_bst([4, 2, 6, 1, 3, 5, 7]), 1, 3) == 2)  # ✅
