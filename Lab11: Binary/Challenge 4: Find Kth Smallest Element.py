# Definición del nodo del Árbol Binario de Búsqueda (BST)
class TreeNode:
    def __init__(self, val):
        self.val = val              # Almacena el valor del nodo
        self.left = None            # Hijo izquierdo (valores menores)
        self.right = None           # Hijo derecho (valores mayores)

# Función para insertar un valor en el BST
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)        # Si el árbol está vacío, crea un nuevo nodo
    if val < root.val:
        root.left = insert_bst(root.left, val)  # Insertar recursivamente en la izquierda
    else:
        root.right = insert_bst(root.right, val)  # Insertar recursivamente en la derecha
    return root                     # Retorna la raíz actualizada

# Construye un BST a partir de una lista de valores
def build_bst(values):
    root = None
    for val in values:
        root = insert_bst(root, val)  # Inserta cada valor en el árbol
    return root

# Función para encontrar el k-ésimo elemento más pequeño en el BST
def kth_smallest(root, k):
    """Encuentra el k-ésimo elemento más pequeño en un BST usando recorrido inorden."""

    def inorder(node):
        if not node:
            return None  # Caso base: nodo nulo
        
        # Recorrido inorden: primero visita el subárbol izquierdo
        left = inorder(node.left)
        if left is not None:
            return left  # Si ya se encontró el valor, lo retornamos inmediatamente
        
        # Procesa el nodo actual
        self.count += 1  # Aumenta el contador
        if self.count == k:
            return node.val  # Si llegamos al k-ésimo, devolvemos el valor
        
        # Luego recorre el subárbol derecho
        return inorder(node.right)

    self = type('', (), {})()  # Crea un objeto vacío para mantener la variable de contador
    self.count = 0             # Inicializa el contador
    return inorder(root)       # Comienza el recorrido desde la raíz



# Caso 1: Segundo más pequeño en un BST balanceado
print(kth_smallest(build_bst([3, 1, 4, 2]), 2) == 2)  # True

# Caso 2: Mínimo (el primer elemento más pequeño)
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 1) == 2)  # True

# Caso 3: El valor más grande (último)
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 7) == 8)  # True

# Caso 4: Elemento en el medio
print(kth_smallest(build_bst([4, 2, 6, 1, 3, 5, 7]), 4) == 4)  # True

# Caso 5: Árbol con un solo nodo
print(kth_smallest(build_bst([10]), 1) == 10)  # True

