# Clase para representar cada nodo del árbol
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Clase principal del Árbol Binario de Búsqueda
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertar un valor en el árbol
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = TreeNode(value)

    # Crear el árbol a partir de una lista
    def build_from_list(self, values):
        for value in values:
            self.insert(value)

    # Encontrar el k-ésimo valor más pequeño (inorden)
    def kth_smallest(self, k):
        """📊 Find the kth smallest value in the BST"""
        result = []

        def in_order(node):
            if not node or len(result) >= k:
                return
            in_order(node.left)
            result.append(node.value)
            in_order(node.right)

        in_order(self.root)

        return result[k - 1] if k <= len(result) else None

# 🧪 Casos de prueba
def test_kth_smallest():
    bst1 = BinarySearchTree()
    bst1.build_from_list([3, 1, 4, 2])
    print("🧪 Test 1:", bst1.kth_smallest(2) == 2)  # 🎯

    bst2 = BinarySearchTree()
    bst2.build_from_list([5, 3, 7, 2, 4, 6, 8])
    print("🧪 Test 2:", bst2.kth_smallest(1) == 2)  # 📉 Primer valor

    print("🧪 Test 3:", bst2.kth_smallest(7) == 8)  # 📈 Último valor

    bst3 = BinarySearchTree()
    bst3.build_from_list([4, 2, 6, 1, 3, 5, 7])
    print("🧪 Test 4:", bst3.kth_smallest(4) == 4)  # 🔗 Valor en el medio

    bst4 = BinarySearchTree()
    bst4.build_from_list([10])
    print("🧪 Test 5:", bst4.kth_smallest(1) == 10)  # 🌱 Solo un nodo

# 🚀 Ejecutar pruebas
test_kth_smallest()
