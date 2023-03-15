class Node:
    def __init__(self, data, index):
        self.data = data
        self.next = None
        self.index = index

class Queue:
    def __init__(self):
        self.counter = 0
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, new_data):
        if not self.check_que(new_data):
            new_node = Node(new_data, self.counter)
            self.counter += 1
            if self.isEmpty():
                self.front = self.rear = new_node
                return True
            self.rear.next = new_node
            self.rear = new_node
            return True

    def check_que(self, data):
        """return true kalau ada duplikat"""
        if not self.isEmpty():
            itr = self.front
            while itr:
                if itr.data == data:
                    return True
                itr = itr.next

    def dequeue_index(self, index):
        if self.isEmpty():
            return
        itr = self.front
        if itr.index == index:
            self.front = itr.next
            return
        while itr.next is not None:
            if itr.next.index == index:
                if itr.next == self.rear:
                    self.rear = itr
                    itr.next = None
                    return
                itr.next = itr.next.next
                return
            itr = itr.next

    def subque(self, tup):
        subque = Queue()
        for i in tup:
            itr = self.front
            while itr is not None:
                if itr.index == int(i):
                    subque.enqueue(itr.data)
                    self.dequeue_index(itr.index)
                    break
                itr = itr.next
        return subque

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


    def peek(self):
        return self.front.data

    def printQ(self):
        if self.isEmpty():
            return print("kosong")
        itr = self.front
        while itr:
            if itr is self.rear:
                break
            print(itr.data, end=" -> ")
            itr = itr.next
        print(itr.data)





