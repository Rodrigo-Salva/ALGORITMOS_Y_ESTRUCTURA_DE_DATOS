# Clase que representa un nodo en el árbol AVL
class AVLNode:
    def __init__(self, key):
        self.key = key           # Guarda el valor de la clave del nodo
        self.left = None         # Referencia al hijo izquierdo
        self.right = None        # Referencia al hijo derecho
        self.height = 1          # Altura del nodo (inicialmente 1 si es hoja)

# Clase que contiene las operaciones del árbol AVL
class AVLTree:
    def get_height(self, node):
        # Devuelve la altura del nodo, o 0 si el nodo es None
        return node.height if node else 0

    def update_height(self, node):
        # Actualiza la altura del nodo en función de sus hijos
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    def rotate_left(self, z):
        # Realiza una rotación hacia la izquierda
        y = z.right            # y será el nuevo padre (hijo derecho de z)
        T2 = y.left            # T2 es el subárbol izquierdo de y

        y.left = z             # z se convierte en hijo izquierdo de y
        z.right = T2           # T2 pasa a ser el hijo derecho de z

        self.update_height(z)  # Actualiza la altura de z
        self.update_height(y)  # Actualiza la altura de y (nuevo padre)

        return y               # Retorna el nuevo nodo raíz después de la rotación

    def rotate_right(self, z):
        # Realiza una rotación hacia la derecha
        y = z.left             # y será el nuevo padre (hijo izquierdo de z)
        T3 = y.right           # T3 es el subárbol derecho de y

        y.right = z            # z se convierte en hijo derecho de y
        z.left = T3            # T3 pasa a ser el hijo izquierdo de z

        self.update_height(z)  # Actualiza la altura de z
        self.update_height(y)  # Actualiza la altura de y (nuevo padre)

        return y               # Retorna el nuevo nodo raíz después de la rotación

def test_rotations():
    tree = AVLTree()

    # Test 1: Left Rotation - [10, 20, 30] -> should become [20, 10, 30]
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print("🧪 Test 1:", z.key == 20 and z.left.key == 10 and z.right.key == 30)

    # Test 2: Right Rotation - [30, 20, 10] -> should become [20, 10, 30]
    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    z = tree.rotate_right(z)
    print("🧪 Test 2:", z.key == 20 and z.left.key == 10 and z.right.key == 30)

    # Test 3: Heights after left rotation
    print("🧪 Test 3 Heights:", z.height == 2 and z.left.height == 1 and z.right.height == 1)

    # Test 4: Children preserved in left rotation
    print("🧪 Test 4 Children:", z.left.key == 10 and z.right.key == 30)

    # Test 5: Heights updated correctly
    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    z = tree.rotate_left(z)
    print("🧪 Test 5 Heights after rotation:", z.height == 2 and z.left.height == 1 and z.right.height == 1)

test_rotations()

