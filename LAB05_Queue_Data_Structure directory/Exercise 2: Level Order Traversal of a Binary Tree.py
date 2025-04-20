from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

#        Test
def test_level_order_traversal():
    # Árbol 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)
    print(level_order_traversal(root1) == [1, 2, 3, 4, 5, 6])  # True

    # Árbol 2: solo un nodo
    root2 = TreeNode(10)
    print(level_order_traversal(root2) == [10])  # True

    # Árbol 3: vacío
    root3 = None
    print(level_order_traversal(root3) == [])  # True

    # Árbol 4: solo hijos izquierdos
    root4 = TreeNode(7)
    root4.left = TreeNode(8)
    root4.left.left = TreeNode(9)
    print(level_order_traversal(root4) == [7, 8, 9])  # True

    # Árbol 5: árbol donde se espera un orden diferente
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    print(level_order_traversal(root5) == [1, 3, 2])  # False (orden incorrecto)

if __name__ == "__main__":
    test_level_order_traversal()
