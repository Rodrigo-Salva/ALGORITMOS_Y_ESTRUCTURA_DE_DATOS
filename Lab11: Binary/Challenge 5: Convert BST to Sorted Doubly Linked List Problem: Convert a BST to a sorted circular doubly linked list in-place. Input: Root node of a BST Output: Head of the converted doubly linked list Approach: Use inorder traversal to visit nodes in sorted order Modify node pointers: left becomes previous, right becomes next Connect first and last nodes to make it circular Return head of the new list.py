# 🌳 Nodo del árbol (también sirve como nodo de la lista doble)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None  # ⬅️ Nodo anterior en la lista
        self.right = None  # ➡️ Nodo siguiente en la lista

# 🌲 Árbol Binario de Búsqueda
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inserta un valor en el árbol
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

    # Construye el árbol desde una lista
    def build_from_list(self, values):
        for value in values:
            self.insert(value)

    # 🔁 Convierte BST a lista doblemente enlazada circular ordenada
    def bst_to_dll(self):
        """🔁 Convert BST to sorted circular doubly linked list"""
        if not self.root:
            return None  # 📭 Árbol vacío

        self.prev = None   # Último nodo procesado
        self.head = None   # Primer nodo de la lista

        def in_order(node):
            if not node:
                return
            in_order(node.left)

            # Primer nodo visitado se convierte en la cabeza
            if not self.prev:
                self.head = node
            else:
                # Conectar nodo previo con el actual
                self.prev.right = node
                node.left = self.prev

            self.prev = node  # Avanzamos

            in_order(node.right)

        # Recorrido inorden del árbol
        in_order(self.root)

        # 🔄 Hacer la lista circular
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head

# ✅ Validador de la lista doblemente enlazada circular
def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    return values == expected_values

# 🧪 Casos de prueba
def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)  # 🔗

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)  # 🌳

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)  # 🌱

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)  # 📈 Degenerate

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)  # 📭 Empty tree

# 🚀 Ejecutar pruebas
test_bst_to_dll()
