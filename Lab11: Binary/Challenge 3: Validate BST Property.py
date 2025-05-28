# ✅ Definición del nodo del árbol
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ✅ Clase principal del árbol binario de búsqueda (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert_recursive(node.right, val)

    def build_from_list(self, values):
        for val in values:
            self.insert(val)

    # ✅ Validación de propiedad de BST 🧼
    def is_valid_bst(self):
        """🧼 Verifica si el árbol cumple con la propiedad de BST"""
        def validate(node, min_val, max_val):
            if node is None:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(self.root, float('-inf'), float('inf'))

# 🧪 Test cases
def test_is_valid_bst():
    bst1 = BinarySearchTree()
    bst1.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 1:", bst1.is_valid_bst() == True)  # ✅ Árbol válido

    bst2 = BinarySearchTree()
    bst2.root = Node(5)
    bst2.root.left = Node(6)  # ❌ Izquierdo > raíz
    bst2.root.right = Node(7)
    print("🧪 Test 2:", bst2.is_valid_bst() == False)  # ❌ Violación por la izquierda

    bst3 = BinarySearchTree()
    bst3.root = Node(5)
    bst3.root.left = Node(3)
    bst3.root.right = Node(4)  # ❌ Derecho < raíz
    print("🧪 Test 3:", bst3.is_valid_bst() == False)  # ❌ Violación por la derecha

    bst4 = BinarySearchTree()
    bst4.build_from_list([42])
    print("🧪 Test 4:", bst4.is_valid_bst() == True)  # 🌱 Nodo único

    bst5 = BinarySearchTree()
    print("🧪 Test 5:", bst5.is_valid_bst() == True)  # 📭 Árbol vacío

# 🚀 Ejecutar los tests
test_is_valid_bst()
