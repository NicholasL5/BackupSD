class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_belakang(self, data):
        newNode = Node(data)
        if not self.head:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
            return
        self.tail.next = newNode
        newNode.next = self.head
        self.tail = newNode


    def tambah(self, num):
        newNode = Node(num)

        if not self.head:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.tail.next = newNode
        self.head = newNode

        # temp = self.head
        # while temp.next is not self.head:
        #     temp = temp.next
        # newNode.next = temp.next
        # temp.next = newNode
        # self.head = newNode

    def tambah_index(self, index, data):
        prevNode = None
        temp = self.head
        counter = 0
        if index == 0:
            self.tambah(data)
        else:
            for i in range(index):
                if temp is self.tail:
                    if counter == index-1:
                        self.tambah_belakang(data)
                        return
                    else:
                        print("kelebihan index")
                        return
                prevNode = temp
                temp = temp.next
                counter += 1
            newNode = Node(data)
            prevNode.next = newNode
            newNode.next = temp

    def hapus(self, key):
        temp = self.head
        # Jika SLL kosong
        if not self.head:
            print("SLL kosong")
            return

        if temp.data == key:
            if temp.next == self.head:
                temp = None
                self.head = None
                return

            self.tail.next = self.head.next
            self.head = self.head.next
            # temp = None
            return

        while temp.next != self.head:
            if temp.next.data == key:
                if temp.next is self.tail:
                    self.tail = temp
                temp.next = temp.next.next

                # temp = None
                return
            temp = temp.next

    def hapus_key(self, value):
        temp = self.head
        if temp.next is self.head and self.head.data == value:
            self.tail.next = self.head.next
            self.head = self.head.next
            return

        while temp.next:
            if temp == self.tail:
                if temp.data == value:
                    prevNode.next = self.head
                    self.tail = prevNode
                    return
                else:
                    return

            if temp.data == value:
                if temp is self.head:
                    self.tail.next = self.head.next
                    self.head = self.head.next
                else:
                    prevNode.next = temp.next
            prevNode = temp
            temp = temp.next

    def print(self):
        temp = self.head
        if not self.head:
            print("kosong")
            return
        while temp is not self.tail:
            print(temp.data, end="-->")
            temp = temp.next
        print(temp.data)

cll = CLL()
# cll.tambah(3)
# cll.tambah(7)
# cll.tambah(0)
# cll.tambah(9)
# cll.tambah_belakang(9)
# cll.tambah_belakang(0)
# cll.tambah_index(2,4)
# cll.hapus_key(0)
# cll.hapus(9)
# cll.hapus(9)
cll.tambah(5)
cll.tambah(5)
cll.tambah_belakang(6)
cll.tambah_index(3,4)

cll.print()


