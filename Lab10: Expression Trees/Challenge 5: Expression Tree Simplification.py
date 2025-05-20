class Node:
    """Node for expression tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def simplify_expression_tree(root):
    """Simplify expression tree by evaluating constant subtrees"""
    if root is None:
        return None

    # Si es hoja, retorna directamente
    if root.left is None and root.right is None:
        return root

    # Recorrer hijos en postorden
    root.left = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    # Verifica si ambos hijos son numéricos
    if (root.left and root.right and
        root.left.value.isdigit() and root.right.value.isdigit()):
        a = int(root.left.value)
        b = int(root.right.value)
        op = root.value

        # Realiza operación según el operador
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a // b  # División entera como en los ejemplos
        else:
            return root  # operador no reconocido, se devuelve sin cambios

        # Retornar nuevo nodo simplificado con el resultado
        return Node(str(result))

    # Si no se puede simplificar, se retorna el nodo original
    return root


# ✅ Test cases
# Test 1: All constants
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)  # 🔢 Full evaluation

# Test 2: Mixed variables and constants
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')  # 🔤 Variable preserved

# Test 3: Partial simplification
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '+' and result3.left.value == '6' and result3.right.value == '5')  # 📊 Subtree simplification

# Test 4: All variables
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')  # 🔤 No simplification

# Test 5: Complex nested simplification
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and 
      result5.right.value == '*' and result5.right.left.value == 'z')  # 🧮 Mixed simplification
