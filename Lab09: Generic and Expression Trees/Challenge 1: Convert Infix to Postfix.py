def infix_to_postfix(tokens):
    """Convierte una expresión infija a notación postfija"""
    # Esta función toma una lista de tokens que representan una expresión infija
    # y devuelve una lista de tokens en notación postfija
    
    result = []
    # Inicializa una lista vacía para almacenar la expresión postfija final
    
    stack = []
    # Inicializa una pila vacía para almacenar temporalmente los operadores
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    # Define un diccionario para almacenar la precedencia de los operadores
    # Un número mayor significa mayor precedencia
    # '+' y '-' tienen precedencia 1
    # '*' y '/' tienen precedencia 2
    # '^' tiene precedencia 3
    
    for token in tokens:
        # Itera a través de cada token en la expresión de entrada
        
        if token not in ['+', '-', '*', '/', '(', ')', '^']:
            result.append(token)
            # Si el token es un operando (número o variable), añádelo directamente al resultado
            
        elif token == '(':
            stack.append(token)
            # Si el token es un paréntesis de apertura, añádelo a la pila
            
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            # Si el token es un paréntesis de cierre, saca los operadores de la pila
            # y añádelos al resultado hasta encontrar un paréntesis de apertura correspondiente
            
            if stack and stack[-1] == '(':
                stack.pop()
            # Elimina el paréntesis de apertura de la pila (descártalo)
            
        else:
            # Si el token es un operador
            while (stack and stack[-1] != '(' and 
                  (stack[-1] in precedence) and 
                  (precedence.get(stack[-1], 0) >= precedence.get(token, 0))):
                result.append(stack.pop())
            # Saca los operadores de la pila y añádelos al resultado si tienen
            # mayor o igual precedencia que el operador actual
            
            stack.append(token)
            # Añade el operador actual a la pila
    
    while stack:
        result.append(stack.pop())
    # Después de procesar todos los tokens, saca los operadores restantes de la pila
    # y añádelos al resultado
    
    return result
    # Devuelve la expresión postfija final


# Test case 1: Simple addition
# Input: 2 + 3
# Output: 2 3 +
print(infix_to_postfix(['2', '+', '3']) == ['2', '3', '+'])  # Simple operation
# Expected: True

# Test case 2: Operator precedence
# Input: 2 + 3 * 4
# Output: 2 3 4 * +
print(infix_to_postfix(['2', '+', '3', '*', '4']) == ['2', '3', '4', '*', '+'])  # Precedence test
# Expected: True

# Test case 3: Parentheses override precedence
# Input: (2 + 3) * 4
# Output: 2 3 + 4 *
print(infix_to_postfix(['(', '2', '+', '3', ')', '*', '4']) == ['2', '3', '+', '4', '*'])  # Parentheses test
# Expected: True

# Test case 4: Complex expression
# Input: (1 + 2) * (3 - 4)
# Output: 1 2 + 3 4 - *
print(infix_to_postfix(['(', '1', '+', '2', ')', '*', '(', '3', '-', '4', ')']) == ['1', '2', '+', '3', '4', '-', '*'])  # Complex expression
# Expected: True

# Test case 5: Multiple operators
# Input: a + b * c / d
# Output: a b c * d / +
print(infix_to_postfix(['a', '+', 'b', '*', 'c', '/', 'd']) == ['a', 'b', 'c', '*', 'd', '/', '+'])  # Variables test
# Expected: True


