stack = []
MAX = 5

def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        x = int(input("Enter element: "))
        stack.append(x)
        print("Element inserted")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Deleted element:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Top element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack elements:", stack[::-1])


while True:
    print("\n1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY")
    print("5. EXIT")

    ch = int(input("Enter choice: "))

    if ch == 1:
        push()
    elif ch == 2:
        pop()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid Choice")
