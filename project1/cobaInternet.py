class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def buatHead(self, data):
        newNode = Node(data)
        self.head = newNode
        newNode.prev = self.head
        newNode.next = self.head
        self.tail = self.head.prev

    def addLast(self, data):
        if self.head is None:
            self.buatHead(data)
        else:
            newNode = Node(data)
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.head.prev = newNode
            self.tail = newNode

    def removeIndex(self, index):

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
            self.current = self.tail
            return
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev



    def printTab(self):
        if self.head is None:
            return
        else:
            pointer = self.head
            while (pointer != self.tail):
                print(pointer.data[0], end=" ")
                pointer = pointer.next
            print(pointer.data[0], end=" ")
            self.current = pointer
            print()

    def printHTML(self):
        print(self.current.data[1])


internet = [
    ("www.google.com", '''<!DOCTYPE html>
        <html>
            <head>
                <title>Google</title>
            </head>
            <body>
                <h1>This is a Heading</h1>
                <p>This is a paragraph.</p>
            </body>
        </html>'''),
    ("www.youtube.com", '''<!DOCTYPE html>
        <html>
            <head>
                <title>YouTube</title>
            </head>
            <body>
                <h1>This is a Heading</h1>
                <p>This is a paragraph.</p>
            </body>
        </html>''')
]

tab = DoubleLinkedList()

running = True
while (running):
    tab.printTab()
    print("1. Search")
    print("2. Close Page")
    if tab.head is None:
        print("No tabs open")
    else:
        tab.printHTML()
    x = int(input())
    if x == 1:
        link = input('Link:')
        for i in range(len(internet)):
            if link == internet[i][0]:
                tab.addLast((internet[i][0], internet[i][1]))
    elif x == 2:
        index = int(input())
        tab.removeIndex(index)