def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output = []
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  
        else:  
            while (stack and stack[-1] != '(' and 
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if token.isnumeric():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
    return stack[0]

def evaluate_infix(expression):
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)

# Example usage
expr = "( 3 + 4 ) * 2"
print("Result:", evaluate_infix(expr)) 
