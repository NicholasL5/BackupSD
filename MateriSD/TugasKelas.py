class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class circDLL:

    def __init__(self):
        self.head = None

    def buatHead(self, data):
        newNode = Node(data)
        self.head = newNode
        newNode.prev = self.head
        newNode.next = self.head
        self.tail = self.head.prev


    def tambahDepan(self, data):
        if self.head is None:
            self.buatHead(data)

        else:
            newNode = Node(data)
            newNode.next = self.head

            temp = self.head
            # set next ujung kanan ll dengan head
            while temp.next:
                if temp.next == self.head:
                    break
                temp = temp.next

            # set next ujung terakhir dengan newNode (calon head)
            temp.next = newNode
            # set new node prev dengan ujung terakhir ll
            newNode.prev = temp
            # set prev head dengan new node
            self.head.prev = newNode
            # set next new node dengan head
            newNode.next = self.head
            # ganti head
            self.head = newNode
            temp = None

    def tambahBelakang(self, data):
        if self.head is None:
            self.buatHead(data)
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next:
                if temp.next == self.head:
                    break
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
            new_node.next = self.head
            self.head.prev = new_node

    def tambahTengah(self, data):
        if self.head is None:
            self.buatHead(data)
        else:
            new_node = Node(data)
            temp = self.head

            # hitung panjang linkedlist
            length = 0
            while temp.next:
                if temp.next == self.head:
                    break
                length += 1
                temp = temp.next
            length += 1

            temp = self.head

            if length % 2 == 0:
                index = length/2
            else:
                index = (length+1) / 2

            for i in range(int(index)):
                temp = temp.next

            new_node.prev = temp.prev
            new_node.next = temp
            temp.prev.next = new_node
            temp.prev = new_node

    def hapusDepan(self):
        # langsung menghapus head dan memindah head ke next node
        temp = self.head

        if self.head is not None:
            self.head = temp.next
            self.head.prev = temp.prev
            temp.prev.next = self.head
            temp = None
            return


    def hapusBelakang(self):
        # mengakses node paling terakhir, karena circular jadi dapat diakses dengan cara head.prev
        # langsung menghapus node paling akhir
        if self.head is not None:
            temp = self.head.prev
            temp.prev.next = self.head
            self.head.prev = temp.prev
            temp = None

    def hapusTengah(self):
        # langsung menghapus index yang ada di tengah
        if self.head is not None:
            temp = self.head

            length = 0
            while temp.next:
                if temp.next == self.head:
                    break
                length += 1
                temp = temp.next
            length += 1

            temp = self.head

            if length % 2 == 0:
                index = length / 2
            else:
                index = (length + 1) / 2

            for i in range(int(index)-1):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp = None



    def printDepan(self):
        # hanya mencetak masing2 node sebanyak 1 kali, jika mencetak circular linklist
        # maka loop tidak pernah berhenti
        temp = self.head
        while temp.next:
            print(temp.data, end="-->")
            temp = temp.next
            if temp.next == self.head:
                print(temp.data, end="-->")
                break

    def printBelakang(self):
        # mencetak linked list dari belakang /terbalik
        temp = self.head.prev
        while temp.prev:
            print(temp.data, end="-->")
            temp = temp.prev
            if temp == self.head:
                print(temp.data, end="-->")
                break


if __name__ == "__main__":
    ll = circDLL()
    ll.tambahDepan("apel")
    ll.tambahDepan("mangga")
    ll.tambahDepan("semangka")
    ll.tambahDepan("durian")

    ll.tambahBelakang("jeruk")
    ll.tambahBelakang("pir")

    ll.tambahTengah("markisa")
    ll.tambahTengah("jambu")

    ll.hapusTengah()
    ll.hapusTengah()

    ll.printDepan()
    print()
    ll.printBelakang()
