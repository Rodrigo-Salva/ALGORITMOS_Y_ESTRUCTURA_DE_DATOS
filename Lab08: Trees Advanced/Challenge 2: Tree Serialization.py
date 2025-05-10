# Definimos la clase TreeNode, que representa un nodo del árbol binario
class TreeNode:
    def __init__(self, value):
        self.value = value  # Valor del nodo
        self.left = None    # Referencia al hijo izquierdo
        self.right = None   # Referencia al hijo derecho

# Definimos la clase BinaryTree para construir el árbol binario
class BinaryTree:
    def __init__(self):
        self.root = None  # Inicialmente el árbol no tiene raíz

    # Método para construir el árbol desde una lista
    def build_tree_from_list(self, values):
        if not values:  # Si la lista está vacía, no hay nada que construir
            return None

        # Creamos la raíz si el primer valor no es None
        self.root = TreeNode(values[0]) if values[0] is not None else None
        # Creamos una cola para construir el árbol por niveles
        queue = [self.root] if self.root else []
        index = 1  # Índice que apunta al siguiente valor de la lista

        # Mientras haya nodos en la cola y valores por procesar
        while queue and index < len(values):
            current = queue.pop(0)  # Tomamos el primer nodo de la cola

            # Procesamos el hijo izquierdo
            if values[index] is not None:
                current.left = TreeNode(values[index])  # Creamos nodo hijo izquierdo
                queue.append(current.left)              # Lo añadimos a la cola
            index += 1  # Avanzamos al siguiente valor

            # Verificamos si aún hay valores
            if index < len(values) and values[index] is not None:
                current.right = TreeNode(values[index])  # Creamos nodo hijo derecho
                queue.append(current.right)              # Lo añadimos a la cola
            index += 1  # Avanzamos al siguiente valor

# Función para serializar un árbol a una cadena
def serialize(root):
    if not root:  # Si el árbol está vacío
        return ""

    result = []        # Lista donde guardaremos los valores serializados
    queue = [root]     # Usamos una cola para recorrer el árbol en anchura (BFS)

    while queue:
        node = queue.pop(0)  # Tomamos el nodo del frente de la cola

        if node:
            result.append(str(node.value))  # Agregamos el valor del nodo
            queue.append(node.left)         # Agregamos su hijo izquierdo a la cola
            queue.append(node.right)        # Agregamos su hijo derecho a la cola
        else:
            result.append('N')  # Si el nodo es None, agregamos 'N'

    # Eliminamos los 'N' del final para optimizar la representación
    while result and result[-1] == 'N':
        result.pop()

    return ','.join(result)  # Devolvemos la cadena separada por comas

# Función para deserializar una cadena a un árbol binario
def deserialize(data):
    if not data:  # Si la cadena está vacía
        return None

    values = data.split(',')  # Convertimos la cadena a una lista

    if values[0] == 'N':  # Si la raíz es 'N', el árbol está vacío
        return None

    root = TreeNode(int(values[0]))  # Creamos la raíz con el primer valor
    queue = [root]                   # Inicializamos la cola con la raíz
    index = 1                        # Apuntamos al siguiente valor

    while queue and index < len(values):
        node = queue.pop(0)  # Tomamos el nodo del frente de la cola

        # Procesamos el hijo izquierdo
        if index < len(values) and values[index] != 'N':
            node.left = TreeNode(int(values[index]))  # Creamos el hijo izquierdo
            queue.append(node.left)                   # Lo añadimos a la cola
        index += 1  # Avanzamos

        # Procesamos el hijo derecho
        if index < len(values) and values[index] != 'N':
            node.right = TreeNode(int(values[index]))  # Creamos el hijo derecho
            queue.append(node.right)                   # Lo añadimos a la cola
        index += 1  # Avanzamos

    return root  # Retornamos la raíz del árbol reconstruido

# Test Cases
def test_serialize_deserialize():
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])  # Árbol con valores variados

    tree2 = BinaryTree()  # Árbol vacío

    tree3 = BinaryTree()
    tree3.build_tree_from_list([42])  # Árbol con un solo nodo

    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, None, 3, None, None, None, 4])  # Árbol inclinado a la izquierda

    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])  # Árbol inclinado a la derecha

    # Ejecutamos la prueba con todos los árboles
    for i, tree in enumerate([tree1, tree2, tree3, tree4, tree5], 1):
        serialized = serialize(tree.root)               # Serializamos el árbol
        deserialized_root = deserialize(serialized)     # Lo deserializamos
        result = "PASS" if serialize(deserialized_root) == serialized else "FAIL"
        print(f"Test Case {i} -> Serialized: {serialized} | Result: {result}")  # Imprime el resultado

    print("All tests completed!")  # Mensaje si todo pasó correctamente

# Llamamos a la función de prueba
test_serialize_deserialize()
