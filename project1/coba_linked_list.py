class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add(self, num):
        if self.head is None:
            newNode = Node(num)
            self.head = newNode
        else:
            newNode = Node(num)
            newNode.next = self.head
            self.head = newNode

    def append(self, num):
        newNode = Node(num)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def delete(self, value):
        temp = self.head

        if self.head is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == value:
                if temp is None:
                    return

                prev.next = temp.next
                temp = None
                break

            prev = temp
            temp = temp.next


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")

            temp = temp.next


ll = SLL()
ll.add(3)
ll.add(6)

ll.add(9)
ll.append(12)
ll.append(6)
ll.delete(120)
ll.printList()
