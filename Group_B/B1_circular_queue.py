class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = x
        print("Inserted", x)

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        x = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print("Deleted", x)

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


size = int(input("Enter size of queue: "))
q = CircularQueue(size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        q.enqueue(x)
    elif ch == 2:
        q.dequeue()
    elif ch == 3:
        q.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")
