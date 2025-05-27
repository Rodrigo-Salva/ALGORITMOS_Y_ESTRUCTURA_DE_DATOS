# Clase del nodo del Árbol Binario de Búsqueda
class TreeNode:
    def __init__(self, val):
        self.val = val              # Valor del nodo
        self.left = None            # Hijo izquierdo
        self.right = None           # Hijo derecho

# Función para insertar un valor en el BST
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)        # Crea un nuevo nodo si el árbol está vacío
    if val < root.val:
        root.left = insert_bst(root.left, val)  # Inserta en el subárbol izquierdo
    else:
        root.right = insert_bst(root.right, val)  # Inserta en el subárbol derecho
    return root

# Construye un BST a partir de una lista
def build_bst(values):
    root = None
    for val in values:
        root = insert_bst(root, val)  # Inserta cada valor en el árbol
    return root

# Construye un BST degenerado (forma de lista enlazada)
def build_degenerate_bst(values):
    root = None
    for val in values:
        root = insert_bst(root, val)  # Inserta en orden creciente
    return root

# Valida que la lista doblemente enlazada circular sea correcta
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    result = []
    node = head
    for _ in range(len(expected_values)):
        result.append(node.val)         # Agrega el valor actual
        node = node.right               # Avanza al siguiente nodo
    return result == expected_values and node == head  # Verifica circularidad

# Función principal para convertir BST a lista doblemente enlazada circular
def bst_to_dll(root):
    """Convierte un BST a una lista doblemente enlazada circular ordenada"""

    if not root:
        return None  # Si el árbol está vacío, retorna None

    # Variables para mantener referencia al primer y último nodo
    first, last = None, None

    # Función interna para recorrido inorden
    def helper(node):
        nonlocal first, last
        if not node:
            return
        
        # Procesa el subárbol izquierdo primero
        helper(node.left)

        # Conecta el nodo actual con el nodo anterior (last)
        if last:
            last.right = node      # Establece el siguiente del anterior al actual
            node.left = last       # Establece el previo del actual al anterior
        else:
            first = node           # Si es el primero, se guarda como inicio de la lista

        last = node                # Actualiza el último nodo procesado

        # Procesa el subárbol derecho
        helper(node.right)

    # Inicia el recorrido desde la raíz
    helper(root)

    # Conecta el primero y el último nodo para hacer la lista circular
    first.left = last
    last.right = first

    return first  # Devuelve el inicio de la lista circular

# Test 1: Árbol simple
head1 = bst_to_dll(build_bst([2, 1, 3]))
print(validate_circular_dll(head1, [1, 2, 3]) == True)  # True

# Test 2: Árbol más grande
head2 = bst_to_dll(build_bst([4, 2, 6, 1, 3, 5, 7]))
print(validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # True

# Test 3: Árbol con un solo nodo
head3 = bst_to_dll(build_bst([5]))
print(validate_circular_dll(head3, [5]) == True)  # True

# Test 4: Árbol degenerado (como lista enlazada)
head4 = bst_to_dll(build_degenerate_bst([1, 2, 3, 4]))
print(validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # True

# Test 5: Árbol vacío
head5 = bst_to_dll(None)
print(head5 is None)  # True
