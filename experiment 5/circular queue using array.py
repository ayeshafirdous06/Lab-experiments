
MAX = 5
queue = [None] * MAX

front = -1
rear = -1


def enqueue():
    global front, rear

    if (rear + 1) % MAX == front:
        print("Circular Queue Overflow")
    else:
        x = int(input("Enter element: "))

        if front == -1:
            front = 0

        rear = (rear + 1) % MAX
        queue[rear] = x

        print("Element inserted")


def dequeue():
    global front, rear

    if front == -1:
        print("Circular Queue Underflow")
    else:
        print("Deleted element:", queue[front])
        queue[front] = None

        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % MAX


def get_front():
    if front == -1:
        print("Queue is Empty")
    else:
        print("Front element:", queue[front])


def get_rear():
    if rear == -1:
        print("Queue is Empty")
    else:
        print("Rear element:", queue[rear])


def display():
    if front == -1:
        print("Queue is Empty")
    else:
        print("Circular Queue:", end=" ")

        i = front

        while True:
            print(queue[i], end=" ")

            if i == rear:
                break

            i = (i + 1) % MAX

        print()


def delete():
    global front, rear

    if front == -1:
        print("Queue is Empty")
    else:
        queue[:] = [None] * MAX
        front = rear = -1
        print("All elements deleted")


while True:
    print("\n--- CIRCULAR QUEUE ---")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. FRONT")
    print("4. REAR")
    print("5. DISPLAY")
    print("6. DELETE ALL")
    print("7. EXIT")

    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()

    elif ch == 2:
        dequeue()

    elif ch == 3:
        get_front()

    elif ch == 4:
        get_rear()

    elif ch == 5:
        display()

    elif ch == 6:
        delete()

    elif ch == 7:
        break

    else:
        print("Invalid Choice")
