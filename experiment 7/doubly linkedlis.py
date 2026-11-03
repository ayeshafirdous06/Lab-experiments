
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = None


def insert_begin():
    global head

    x = int(input("Enter element: "))
    new_node = Node(x)

    new_node.next = head

    if head is not None:
        head.prev = new_node

    head = new_node
    print("Node inserted")


def insert_end():
    global head

    x = int(input("Enter element: "))
    new_node = Node(x)

    if head is None:
        head = new_node
    else:
        temp = head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    print("Node inserted")


def insert_pos():
    global head

    x = int(input("Enter element: "))
    pos = int(input("Enter position: "))

    if pos < 1:
        print("Invalid Position")
        return

    new_node = Node(x)

    if pos == 1:
        new_node.next = head

        if head:
            head.prev = new_node

        head = new_node
        print("Node inserted")
        return

    temp = head

    for i in range(pos - 2):
        if temp is None:
            print("Invalid Position")
            return
        temp = temp.next

    if temp is None:
        print("Invalid Position")
        return

    new_node.next = temp.next
    new_node.prev = temp

    if temp.next:
        temp.next.prev = new_node

    temp.next = new_node

    print("Node inserted")


def delete_begin():
    global head

    if head is None:
        print("List is Empty")
        return

    print("Deleted element:", head.data)
    head = head.next

    if head:
        head.prev = None


def delete_end():
    global head

    if head is None:
        print("List is Empty")
        return

    temp = head

    if temp.next is None:
        print("Deleted element:", temp.data)
        head = None
        return

    while temp.next:
        temp = temp.next

    print("Deleted element:", temp.data)
    temp.prev.next = None


def delete_pos():
    global head

    pos = int(input("Enter position: "))

    if pos < 1 or head is None:
        print("Invalid Position or Empty List")
        return

    temp = head

    if pos == 1:
        delete_begin()
        return

    for i in range(pos - 1):
        if temp is None:
            print("Invalid Position")
            return
        temp = temp.next

    if temp is None:
        print("Invalid Position")
        return

    print("Deleted element:", temp.data)

    temp.prev.next = temp.next

    if temp.next:
        temp.next.prev = temp.prev


def search():
    x = int(input("Enter element to search: "))
    temp = head
    pos = 1

    while temp:
        if temp.data == x:
            print("Element found at position:", pos)
            return

        temp = temp.next
        pos += 1

    print("Element not found")


def display():
    if head is None:
        print("List is Empty")
        return

    temp = head

    print("Forward:", end=" ")

    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next

    print("None")


def reverse_display():
    if head is None:
        print("List is Empty")
        return

    temp = head

    while temp.next:
        temp = temp.next

    print("Backward:", end=" ")

    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.prev

    print("None")


while True:
    print("\n--- DOUBLY LINKED LIST ---")
    print("1. INSERT BEGINNING")
    print("2. INSERT END")
    print("3. INSERT POSITION")
    print("4. DELETE BEGINNING")
    print("5. DELETE END")
    print("6. DELETE POSITION")
    print("7. SEARCH")
    print("8. DISPLAY FORWARD")
    print("9. DISPLAY BACKWARD")
    print("10. EXIT")

    ch = int(input("Enter choice: "))

    if ch == 1:
        insert_begin()

    elif ch == 2:
        insert_end()

    elif ch == 3:
        insert_pos()

    elif ch == 4:
        delete_begin()

    elif ch == 5:
        delete_end()

    elif ch == 6:
        delete_pos()

    elif ch == 7:
        search()

    elif ch == 8:
        display()

    elif ch == 9:
        reverse_display()

    elif ch == 10:
        break

    else:
        print("Invalid Choice")
