class TreeNode:
    def __init__(self, value):
        self.value = value  # El valor del nodo
        self.left = None  # Hijo izquierdo (inicialmente vacío)
        self.right = None  # Hijo derecho (inicialmente vacío)

def count_leaves(root):
    # Si el nodo es nulo, no hay nodos hoja
    if root is None:
        return 0
    
    # Si el nodo no tiene hijos izquierdo y derecho, es un nodo hoja
    if root.left is None and root.right is None:
        return 1
    
    # Si el nodo tiene hijos, contamos los nodos hoja en los subárboles
    return count_leaves(root.left) + count_leaves(root.right)

# Casos de prueba
def test_count_leaves():
    # Test Case 1: Árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print("Test Case 1:", count_leaves(root))  # Esperado: 3 (nodos 4, 5, 3)

    # Test Case 2: Árbol vacío
    empty_tree = None
    print("Test Case 2:", count_leaves(empty_tree))  # Esperado: 0

    # Test Case 3: Árbol con un solo nodo
    single_node = TreeNode(1)
    print("Test Case 3:", count_leaves(single_node))  # Esperado: 1 (nodo 1)

    # Test Case 4: No hay nodos hoja en el primer nivel
    no_leaves_at_first = TreeNode(1)
    no_leaves_at_first.left = TreeNode(2)
    no_leaves_at_first.right = TreeNode(3)
    print("Test Case 4:", count_leaves(no_leaves_at_first))  # Esperado: 0

    # Test Case 5: Todos los nodos son hojas, excepto la raíz
    all_leaves = TreeNode(1)
    all_leaves.left = TreeNode(2)
    all_leaves.right = TreeNode(3)
    all_leaves.left.left = TreeNode(4)
    all_leaves.left.right = TreeNode(5)
    all_leaves.right.left = TreeNode(6)
    all_leaves.right.right = TreeNode(7)
    print("Test Case 5:", count_leaves(all_leaves))  # Esperado: 4 (nodos 4, 5, 6, 7)

# Ejecutar los casos de prueba
test_count_leaves()
