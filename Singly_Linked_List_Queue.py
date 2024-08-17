
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        x = int(input("Enter element to be inserted into the Queue : "))
        new = Node(x)
        if self.front is None:
            self.front = new
            self.rear = new
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        elif self.front.next is None:
            print("Popped Element is :", self.front.data)
            print("-----------------------------------")
            self.front = None
        else:
            temp = self.front
            print("Popped Element is :", self.front.data)
            print("------------------------------------")
            self.front = temp.next
            temp = None

    def display(self):
        if self.front is None:
            print("Queue is empty\n---------------------")
        else:
            print("Elements of the Queue are :")
            temp = self.front
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print("\nFront of the Queue is :", self.front.data)
            print("Rear of the Queue is :", self.rear.data)


q = Queue()

while (1):
    print("Enter the option from below")
    print("1 - Enqueue Operation")
    print("2 - Dequeue Operation")
    print("3 - Display Operation")
    print("4 - Exit")

    option = int(input())
    if option == 1:
        print("Enqueue Operation\n------------")
        q.enqueue()
    elif option == 2:
        print("Dequeue Operation\n------------")
        q.dequeue()
    elif option == 3:
        print("Display Operation\n------------")
        q.display()
    elif option == 4:
        print("Exiting...")
        break
