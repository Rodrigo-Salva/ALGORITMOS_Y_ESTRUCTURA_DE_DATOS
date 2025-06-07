# Clase que representa un nodo del árbol AVL
class AVLNode:
    def __init__(self, val):
        self.val = val              # Valor del nodo
        self.left = None            # Hijo izquierdo
        self.right = None           # Hijo derecho
# Clase del Árbol AVL con métodos para insertar y verificar si está balanceado
class AVLTree:

    def insert(self, root, key):
        """Inserta un nuevo valor en el árbol de forma ordenada (tipo BST)."""
        if root is None:
            return AVLNode(key)    # Crea un nuevo nodo si el lugar está vacío
        elif key < root.val:
            root.left = self.insert(root.left, key)   # Inserta en el subárbol izquierdo
        else:
            root.right = self.insert(root.right, key) # Inserta en el subárbol derecho
        return root  # Devuelve el nodo raíz actualizado

    def is_avl_balanced(self, root):
        """
        Verifica si el árbol está balanceado según las reglas AVL.
        Devuelve True si está balanceado, False si no.
        """
        def check(node):
            if node is None:
                return 0  # Caso base: altura de un nodo vacío es 0

            # Verifica recursivamente la altura del subárbol izquierdo
            left_height = check(node.left)
            if left_height == -1:
                return -1  # Si el subárbol izquierdo no está balanceado, corta

            # Verifica recursivamente la altura del subárbol derecho
            right_height = check(node.right)
            if right_height == -1:
                return -1  # Si el subárbol derecho no está balanceado, corta

            # Verifica el factor de balance (diferencia de alturas)
            if abs(left_height - right_height) > 1:
                return -1  # Si la diferencia es mayor a 1, no es AVL

            # Retorna la altura actual: 1 + el mayor de sus hijos
            return max(left_height, right_height) + 1

        # El árbol está balanceado si la verificación no devuelve -1
        return check(root) != -1
# Casos de prueba para verificar si la función is_avl_balanced funciona correctamente
def test_is_avl_balanced():
    avl = AVLTree()

    # Test 1: Árbol balanceado con 3 nodos
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)  # ✅ Debería ser True

    # Test 2: Árbol desbalanceado manualmente (más pesado a la derecha)
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)  # ❌ Debería ser False

    # Test 3: Árbol vacío (caso base)
    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)  # 🌱 True, un árbol vacío es AVL

    # Test 4: Árbol muy desbalanceado a la izquierda (desequilibrio profundo)
    deep = AVLNode(50)
    deep.left = AVLNode(40)
    deep.left.left = AVLNode(30)
    deep.left.left.left = AVLNode(20)
    deep.left.left.left.left = AVLNode(10)
    print("🧪 Test 4:", avl.is_avl_balanced(deep) == False)  # ❌ No está balanceado

    # Test 5: Árbol balanceado más grande con 7 nodos
    avl_root = None
    for val in [15, 10, 20, 5, 12, 17, 25]:
        avl_root = avl.insert(avl_root, val)
    print("🧪 Test 5:", avl.is_avl_balanced(avl_root) == True)  # ✅ Correcto, es AVL
    
# Ejecutar los test
test_is_avl_balanced()
