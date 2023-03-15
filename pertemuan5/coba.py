import math


class Node():
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.next = None
        pass


class Queue():
    def __init__(self):
        self.front = self.rear = Node(0, 0)
        self.listHouse = []

    def isEmpty(self):
        return self.front is None or self.rear is None

    # saat enqueue, program harus cek dari node awal
    # hingga akhir. Lalu dibandingkan jarak antar node
    # dengan data yang baru masuk. Jika data yang baru
    # masuk jaraknya lebih kecil/sama dengan maka node
    # baru akan disisipkan diantara 2 node
    def enqueue(self, _x, _y):
        newNode = Node(_x, _y)
        self.listHouse.append(newNode)
        itr = self.front
        while itr != self.rear:
            x1 = self.distance(itr, newNode)
            x2 = self.distance(itr, itr.next)
            if x1 <= x2:
                newNode.next = itr.next
                itr.next = newNode
                return
            itr = itr.next
        self.rear.next = newNode
        self.rear = newNode

    def distance(self, p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def totalJarak(self):
        _count = 0
        itr = self.front
        while itr != self.rear:
            _count += self.distance(itr, itr.next)
            itr = itr.next
        print('total jarak yang ditempuh', _count)

    def dequeue(self):
        if self.isEmpty():
            print('Kosong')

        temp = self.front
        if self.front == self.rear:
            self.front = self.rear = None
            return
        self.front = self.front.next
        print('(', temp.x, ',', temp.y, ')', "keluar")
        return temp

    def peek(self):
        print('(', self.front.x, ',', self.front.y, ')')
        return self.front

    def printQueue(self):
        itr = self.front
        while itr != self.rear:
            print('(', itr.x, ',', itr.y, ')', end=' -> ')
            itr = itr.next
        print('(', itr.x, ',', itr.y, ')')

    # program akan enqueue ulang jika titik awalnya diganti
    def setStart(self, _x, _y):
        newNode = Node(_x, _y)
        self.front = self.rear = newNode
        temp = self.listHouse
        self.listHouse = []
        for i in temp:
            self.enqueue(i.x, i.y)


q = Queue()
q.enqueue(1, 0)
q.enqueue(-2, 0)
q.enqueue(4, 0)
# q.enqueue(-7, 0)
q.printQueue()
q.totalJarak()
# q.setStart(-5, 0)
# q.printQueue()
# q.totalJarak()


