
def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   (precedence(stack[-1]) > precedence(ch) or
                    (precedence(stack[-1]) == precedence(ch)
                     and ch != '^'))):
                postfix += stack.pop()

            stack.append(ch)

    if '(' in stack:
        raise ValueError("Mismatched parentheses")

    while stack:
        postfix += stack.pop()

    return postfix


exp = input("Enter infix expression: ")
print("Postfix Expression:", infix_to_postfix(exp))
