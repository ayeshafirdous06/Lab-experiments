
def evaluate_postfix(expression):
    stack = []

    for ch in expression:
        if ch.isdigit():
            stack.append(int(ch))

        elif ch in "+-*/^":
            if len(stack) < 2:
                raise ValueError("Invalid expression")

            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
            elif ch == '^':
                stack.append(a ** b)

        elif ch.isspace():
            continue

        else:
            raise ValueError("Invalid character")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack[0]


exp = input("Enter postfix expression: ")

try:
    print("Result:", evaluate_postfix(exp))
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
