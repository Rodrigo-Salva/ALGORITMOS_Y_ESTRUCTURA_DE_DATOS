class GenericTreeNode:  # Clase para representar un nodo de un árbol genérico
    """Node class for a generic tree."""
    def __init__(self, value):  # Constructor que recibe el valor del nodo
        self.value = value       # Asigna el valor al atributo del nodo
        self.children = []       # Inicializa la lista de hijos vacía


class GenericTree:  # Clase para representar el árbol genérico
    """Generic tree implementation"""

    def __init__(self, root=None):  # Constructor que puede recibir un nodo raíz o dejarlo como None
        self.root = root            # Asigna el nodo raíz al atributo del árbol

    def find_leaves(self):  # Método que busca todas las hojas del árbol
        """Find all leaf nodes in the tree"""
        leaves = []  # Lista para guardar los valores de las hojas encontradas

        def dfs(node):  # Función auxiliar recursiva para recorrer el árbol (Depth First Search)
            if not node:  # Si el nodo es None, no se hace nada
                return
            if not node.children:  # Si el nodo no tiene hijos, es una hoja
                leaves.append(node.value)  # Agrega el valor de la hoja a la lista
            for child in node.children:  # Recorre todos los hijos del nodo actual
                dfs(child)  # Llama recursivamente a dfs para cada hijo

        dfs(self.root)  # Inicia el recorrido desde la raíz del árbol
        return leaves  # Retorna la lista de hojas encontradas


# ✅ Test cases

# Test 1: Empty tree
# Tree: None
empty_tree = GenericTree(None)
print(empty_tree.find_leaves() == [])  # 📭 No leaves

# Test 2: Single node (root is leaf)
# Tree: X
single = GenericTree(GenericTreeNode('X'))
print(single.find_leaves() == ['X'])  # 🌱 Root is leaf

# Test 3: Linear tree
# Tree: A → B → C
#       A
#       |
#       B
#       |
#       C
linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.find_leaves() == ['C'])  # 🍃 End of chain

# Test 4: Multiple leaves
# Tree:     A
#         / | \
#        B  C  D
#       /|\    |
#      E F G   H
tree_root = GenericTreeNode('A')
b, c, d = GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D')
e, f, g, h = GenericTreeNode('E'), GenericTreeNode('F'), GenericTreeNode('G'), GenericTreeNode('H')
tree_root.children = [b, c, d]
b.children = [e, f, g]
d.children = [h]
tree = GenericTree(tree_root)
print(sorted(tree.find_leaves()) == ['C', 'E', 'F', 'G', 'H'])  # 🍂 All leaves

# Test 5: Wide tree (all children are leaves)
# Tree:     A
#      / | | | \
#     B  C D E  F
wide_root = GenericTreeNode('A')
wide_root.children = [GenericTreeNode('B'), GenericTreeNode('C'), GenericTreeNode('D'),
                      GenericTreeNode('E'), GenericTreeNode('F')]
wide_tree = GenericTree(wide_root)
print(sorted(wide_tree.find_leaves()) == ['B', 'C', 'D', 'E', 'F'])  # 🌿 Wide tree
