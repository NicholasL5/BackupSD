class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircQueue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.front

    def dequeue(self):
        if self.isEmpty():
            print("kosong")
            return
        temp = self.front
        self.rear = temp.next
        self.front = temp.next
        return temp.data

    def peek(self):
        return self.front

    def printQ(self):
        itr = self.front
        while itr:
            if itr.next is self.front:
                break
            print(itr.data, end=" -> ")
            itr = itr.next
        print(itr.data)


que = CircQueue()
que.enqueue(5)
que.enqueue(4)
que.enqueue(3)
que.enqueue(2)
que.enqueue(1)
que.printQ()
