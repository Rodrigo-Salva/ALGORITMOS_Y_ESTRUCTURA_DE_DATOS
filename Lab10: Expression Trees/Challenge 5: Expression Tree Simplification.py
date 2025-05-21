# Clase para definir un nodo del árbol de expresiones
class Node:
    def __init__(self, value):
        self.value = value    # Valor del nodo (puede ser número, variable u operador)
        self.left = None      # Hijo izquierdo
        self.right = None     # Hijo derecho

# Función que verifica si un valor es un número
def is_number(s):
    try:
        float(s)             # Intenta convertir el valor a número flotante
        return True          # Si lo logra, es un número
    except ValueError:
        return False         # Si falla, no es un número

# Función que evalúa una operación matemática con dos números
def calculate(op, a, b):
    a = float(a)             # Convierte el primer valor a número
    b = float(b)             # Convierte el segundo valor a número

    # Aplica la operación correspondiente
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        if b == 0:
            return None      # Evita división entre cero
        res = a / b
    else:
        return None          # Si no es una operación válida, retorna None

    # Si el resultado es entero, devuelve como entero. Si no, como decimal
    return str(int(res)) if res.is_integer() else str(res)

# Función principal que simplifica el árbol de expresiones
def simplify_expression_tree(root):
    if root is None:
        return None          # Si el nodo es nulo, no hay nada que hacer

    # Primero se simplifican recursivamente los hijos izquierdo y derecho (postorden)
    root.left = simplify_expression_tree(root.left)
    root.right = simplify_expression_tree(root.right)

    # Si ambos hijos existen y son números, se puede simplificar el nodo actual
    if root.left and root.right:
        if is_number(root.left.value) and is_number(root.right.value):
            result = calculate(root.value, root.left.value, root.right.value)
            if result is not None:
                return Node(result)  # Crea un nuevo nodo con el resultado simplificado

    return root  # Si no se puede simplificar, retorna el nodo como está

# ---------------------- CASOS DE PRUEBA ----------------------

# Test 1: Árbol de expresión 2 + 3 => Se espera que simplifique a 5
node1 = Node('+')
node1.left = Node('2')
node1.right = Node('3')
result1 = simplify_expression_tree(node1)
print(result1.value == '5' and result1.left is None and result1.right is None)

# Test 2: Árbol de expresión x + 3 => No se puede simplificar porque "x" es una variable
node2 = Node('+')
node2.left = Node('x')
node2.right = Node('3')
result2 = simplify_expression_tree(node2)
print(result2.value == '+' and result2.left.value == 'x' and result2.right.value == '3')

# Test 3: Árbol de expresión (2 * 3) + (8 - 3) => Primero se simplifica a 6 + 5 => luego a 11
node3 = Node('+')
node3.left = Node('*')
node3.right = Node('-')
node3.left.left = Node('2')
node3.left.right = Node('3')
node3.right.left = Node('8')
node3.right.right = Node('3')
result3 = simplify_expression_tree(node3)
print(result3.value == '11' and result3.left is None and result3.right is None)

# Test 4: Árbol de expresión x + y => No se puede simplificar porque ambos son variables
node4 = Node('+')
node4.left = Node('x')
node4.right = Node('y')
result4 = simplify_expression_tree(node4)
print(result4.value == '+' and result4.left.value == 'x' and result4.right.value == 'y')

# Test 5: Árbol de expresión (10 / 2) + (z * 4) => Se simplifica 10 / 2 a 5, pero z * 4 no cambia
node5 = Node('+')
node5.left = Node('/')
node5.right = Node('*')
node5.left.left = Node('10')
node5.left.right = Node('2')
node5.right.left = Node('z')
node5.right.right = Node('4')
result5 = simplify_expression_tree(node5)
print(result5.value == '+' and result5.left.value == '5' and
      result5.right.value == '*' and result5.right.left.value == 'z' and result5.right.right.value == '4')
