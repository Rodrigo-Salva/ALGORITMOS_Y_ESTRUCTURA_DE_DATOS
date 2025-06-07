from collections import deque  # Importamos deque para usar una cola eficiente en BFS

# Clase que representa cada nodo del árbol AVL
class AVLNode:
    def __init__(self, key):
        self.key = key         # Clave o valor del nodo
        self.left = None       # Hijo izquierdo
        self.right = None      # Hijo derecho
        self.height = 1        # Altura del nodo (inicialmente 1 al insertarse)

# Clase principal del Árbol AVL
class AVLTree:

    # Función para obtener la altura de un nodo (devuelve 0 si es None)
    def get_height(self, node):
        return node.height if node else 0

    # Función para actualizar la altura de un nodo después de cambios
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # Rotación hacia la izquierda
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self.update_height(z)
        self.update_height(y)
        return y

    # Rotación hacia la derecha
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self.update_height(z)
        self.update_height(y)
        return y

    # Función para obtener el factor de balance de un nodo
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Inserción en árbol AVL con balanceo
    def insert(self, node, key):
        # Paso base: insertar como en un BST normal
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # Actualizar altura del nodo actual
        self.update_height(node)

        # Obtener el factor de balance
        balance = self.get_balance(node)

        # Caso 1: Izquierda - Izquierda
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Caso 2: Derecha - Derecha
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Caso 3: Izquierda - Derecha
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Caso 4: Derecha - Izquierda
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        # Retornar el nodo sin cambios
        return node

    # 📡 Imprimir recorrido por niveles incluyendo altura
    def print_level_order(self, root):
        if not root:
            return  # Si el árbol está vacío, no imprimimos nada

        queue = deque([root])  # Cola para el recorrido BFS

        while queue:
            level_size = len(queue)  # Número de nodos en el nivel actual
            current_level = []       # Lista temporal para almacenar nodos del nivel

            for _ in range(level_size):
                node = queue.popleft()  # Sacamos el primer nodo de la cola
                current_level.append(f"{node.key}(h{node.height})")  # Formato valor(hX)

                # Agregamos los hijos a la cola si existen
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Imprimimos todos los nodos del nivel actual
            print(", ".join(current_level))

# 🧪 Test it!
def test_level_order_heights():
    avl = AVLTree()
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)

    print("🧪 Test 1–5: Expected output:")
    # 10(h3)
    # 5(h2), 15(h1)
    # 2(h1), 7(h1)
    avl.print_level_order(root)

# 🚀 Go!
test_level_order_heights()
