class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class circDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head.prev
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        newNode.next = self.head
        self.head.prev = newNode
        self.tail = newNode

    def add_front(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head.prev
            return

        newNode.next = self.head
        newNode.prev = self.tail
        self.tail.next = newNode
        self.head.prev = newNode
        self.head = newNode

    def add_index(self, index, data):
        temp = self.head
        prevNode = None
        flag = False
        counter = 0
        if index == 0:
            self.add_front(data)
        else:
            for i in range(index):
                if temp is self.tail:
                    """
                    membuat fungsi add index bisa tambah belakang. Misal panjang ll = 3, index ke 3 bisa
                    ditambah dan dijadikan tail
                    """

                    if counter == index-1:
                        self.add_end(data)
                        return
                    else:
                        print("kelebihan index")
                        return
                prevNode = temp
                temp = temp.next
                counter += 1

            newNode = Node(data)
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = temp
            temp.prev = newNode

    def print(self):
        if self.head is None:
            print("kosong")
            return
        temp = self.head
        while temp.next is not self.head:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data)

    def print_reverse(self):
        # mencetak linked list dari belakang /terbalik
        temp = self.head.prev
        while temp.prev:
            print(temp.data, end="-->")
            temp = temp.prev
            if temp == self.head:
                print(temp.data)
                break

    def deleteIndex(self, index):
        if self.head is None:
            return

        if index == 0:
            if self.head.next is self.head:
                self.head = None
                self.tail = None
                self.current = None
            else:
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
            return

        temp = self.head
        for i in range(index):
            if temp.next is self.head:
                return
            else:
                temp = temp.next

        if temp is self.tail:
            temp.prev.next = self.head
            temp.next.prev = temp.prev
            self.tail = temp.prev
            return
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev