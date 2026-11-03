
queue = []
MAX = 5

def enqueue():
    if len(queue) == MAX:
        print("Queue Overflow")
    else:
        x = int(input("Enter element: "))
        queue.append(x)
        print("Element inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))

def display():
    if len(queue) == 0:
        print("Queue is Empty")
    else:
        print("Queue elements:", queue)


while True:
    print("\n1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. DISPLAY")
    print("4. EXIT")

    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid Choice")
