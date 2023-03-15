class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
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

    def dequeue(self):
        if self.isEmpty():
            print("kosong")
            return
        temp = self.front
        self.front = temp.next
        return temp.data

    def to_list(self):
        data = []
        if not self.isEmpty():
            itr = self.front
            while itr:
                data.append(itr.data)
                itr = itr.next

        return data

    def add_all(self, queue):
        itr = queue.front
        # cek kalo sama
        while itr:
            self.enqueue(itr.data)
            itr = itr.next


    def peek(self):
        return self.front.data

    def printQ(self):
        itr = self.front
        while itr:
            if itr is self.rear:
                break
            print(itr.data, end=" -> ")
            itr = itr.next
        print(itr.data)


