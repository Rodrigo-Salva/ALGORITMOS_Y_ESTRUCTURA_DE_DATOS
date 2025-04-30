class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Valor del nodo
        self.left = left  # Referencia al hijo izquierdo
        self.right = right  # Referencia al hijo derecho

def tree_height(root):
    if root is None:
        return -1  # Si el árbol está vacío, su altura es -1
    return 1 + max(tree_height(root.left), tree_height(root.right))  
    # Llamadas recursivas para encontrar la altura del subárbol izquierdo y derecho.

def test_tree_height():
    #Se inicia una función de prueba para validar varios casos de uso del árbol binario.
        # Árbol normal
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert tree_height(root) == 2
    # La altura del árbol es 2 (nodos 4 y 5 son hojas)


        # Árbol vacío
    empty_tree = None
    assert tree_height(empty_tree) == -1
    # La altura de un árbol vacío es -1

        # Árbol con un solo nodo
    single = TreeNode(1)
    assert tree_height(single) == 0
    # La altura de un árbol con un solo nodo es 0

        # Árbol inclinado a la izquierda
    left = TreeNode(1)
    left.left = TreeNode(2)
    left.left.left = TreeNode(3)
    left.left.left.left = TreeNode(4)
    assert tree_height(left) == 3
    # La altura del árbol es 3 (nodos 2, 3 y 4 son hojas)

        # Árbol binario perfecto
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    assert tree_height(perfect) == 2
    # La altura del árbol es 2 (nodos 4, 5, 6 y 7 son hojas) aristas

    print("All test cases passed!")
    #Mensaje final si todo es correcto.

# Test Case 1: Empty tree
empty_tree = None
print("Test Case 1 (Empty Tree):", tree_height(empty_tree))  # Expected: -1

# Test Case 2: Single-node tree
single = TreeNode(1)
print("Test Case 2 (Single Node):", tree_height(single))     # Expected: 0

# Test Case 3: Left-skewed tree
left = TreeNode(1)
left.left = TreeNode(2)
left.left.left = TreeNode(3)
left.left.left.left = TreeNode(4)
print("Test Case 3 (Left-skewed Tree):", tree_height(left))  # Expected: 3


