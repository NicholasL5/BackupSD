class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, num):
        #jika masih kosong
        if self.head is None:
            newNode = Node(num)
            self.head = newNode
        else:
            newNode = Node(num)
            newNode.next = self.head
            self.head = newNode

    def delete(self, key):
        temp = self.head

        if self.head is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' --> ')
            temp = temp.next

    def delete_duplicate(self):
        temp = self.head
        hapus = False
        if temp.next == self.head:
            return

        while temp is not None:
            hapus = False
            if temp.next is None:
                return
            temp2 = temp
            while temp2 is not None:
                hapus = False
                if temp2.next is None:
                    break
                if temp2.next.data == temp.data:
                    if temp2.next.next is None:
                        temp2.next = None
                    else:
                        temp2.next = temp2.next.next
                    hapus = True
                if not hapus:
                    temp2 = temp2.next

            temp = temp.next

ll = LinkedList()
ll.add(3)
ll.add(3)
ll.add(3)
# ll.add(9)
# ll.add(0)
# ll.add(5)
# ll.add(4)
# ll.add(1)
# ll.add(1)
# ll.add(2)
# ll.add(3)
ll.print()
ll.delete_duplicate()
print()
ll.print()
print()
print("soal 2:")
# soal2
list1 = [2,5,7]
list2 = [1,3,4]

list1 = sorted(list1, reverse=True)
list2 = sorted(list2, reverse=True)
ll2 = LinkedList()
# for i in list2:
#     list1.append(i)
index = None
counter1 = 0
counter2 = 0
tanda1 = False
tanda2 = False
for i in range(len(list1) + len(list2)):
    if not tanda1 and tanda2:
        if list1[counter1] >= list2[counter2]:
            ll2.add(list1[counter1])
            counter1 += 1
        else:
            ll2.add(list2[counter2])
            counter2 += 1
    else:
        if tanda1:
            ll2.add(list2[counter2])
            counter2 += 1
        elif tanda2:
            ll2.add(list1[counter1])
            counter1 += 1
    if counter1 > len(list1):
        tanda1 = True
    else:
        tanda2 = True
ll2.print()

# soal3





