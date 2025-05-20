# Clase que representa un nodo en el árbol de expresiones
class Node:
    def __init__(self, value):
        self.value = value         # Valor del nodo (operador o operando)
        self.left = None           # Hijo izquierdo
        self.right = None          # Hijo derecho

# Recorrido inorden (left, root, right)
def inorder_traversal(root):
    """Perform inorder traversal (left, root, right)"""
    if root is None:
        return []  # Si el nodo está vacío, retorna lista vacía
    # Recursivamente recorre el subárbol izquierdo, luego el valor actual, y luego el subárbol derecho
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Recorrido preorden (root, left, right)
def preorder_traversal(root):
    """Perform preorder traversal (root, left, right)"""
    if root is None:
        return []  # Si el nodo está vacío, retorna lista vacía
    # Devuelve primero el valor actual, luego el subárbol izquierdo, luego el derecho
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Recorrido postorden (left, right, root)
def postorder_traversal(root):
    """Perform postorder traversal (left, right, root)"""
    if root is None:
        return []  # Si el nodo está vacío, retorna lista vacía
    # Primero recorre el subárbol izquierdo, luego el derecho, y por último el valor actual
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]


# ✅ Test 1: Árbol simple con operador '+'
#     +
#    / \
#   2   3
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
print(inorder_traversal(node1) == ['2', '+', '3'])
print(preorder_traversal(node1) == ['+', '2', '3'])
print(postorder_traversal(node1) == ['2', '3', '+'])

# ✅ Test 2: Árbol más complejo con '*'
#       +
#      / \
#     *   5
#    / \
#   2   3
node2 = Node('+')
node2.left = Node('*')
node2.right = Node('5')
node2.left.left = Node('2')
node2.left.right = Node('3')
print(inorder_traversal(node2) == ['2', '*', '3', '+', '5'])
print(preorder_traversal(node2) == ['+', '*', '2', '3', '5'])
print(postorder_traversal(node2) == ['2', '3', '*', '5', '+'])

# ✅ Test 3: Árbol con un solo nodo
node3 = Node('X')
print(inorder_traversal(node3) == ['X'])
print(preorder_traversal(node3) == ['X'])
print(postorder_traversal(node3) == ['X'])

# ✅ Test 4: Árbol vacío
print(inorder_traversal(None) == [])
print(preorder_traversal(None) == [])
print(postorder_traversal(None) == [])

# ✅ Test 5: Árbol complejo con múltiples operadores
#           /
#         /   \
#        +     -
#       / \   / \
#      a   b c   d
node5 = Node('/')
node5.left = Node('+')
node5.right = Node('-')
node5.left.left = Node('a')
node5.left.right = Node('b')
node5.right.left = Node('c')
node5.right.right = Node('d')
print(inorder_traversal(node5) == ['a', '+', 'b', '/', 'c', '-', 'd'])
print(preorder_traversal(node5) == ['/', '+', 'a', 'b', '-', 'c', 'd'])
print(postorder_traversal(node5) == ['a', 'b', '+', 'c', 'd', '-', '/'])
