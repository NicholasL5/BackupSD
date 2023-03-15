# from cobastack import Stack, Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

        # print("%d masuk" % data)

    def pop(self):
        if self.is_empty():
            return print("kosong")
        temp = self.top
        self.top = self.top.next
        popped = temp.data
        return popped

    def peek(self):
        if self.is_empty():
            return print("kosong")
        return self.top.data

    def show(self):
        temp = self.top
        while temp.next:
            print(temp.data)
            temp = temp.next
        print(temp.data)


nama_pria = input("input nama lengkap pria: ")
nama_wanita = input("input nama lengkap wanita: ")

counter_cinta = 30

stack_pria = Stack()
stack_wanita = Stack()

for char in nama_pria.upper():
    if char == " ":
        pass
    else:
        # ord char % 64 untuk mendapatkan nomor urut alfabet
        stack_pria.push((ord(char) % 64) % 10)

for char in nama_wanita.upper():
    if char == " ":
        pass
    else:
        stack_wanita.push(((ord(char) % 64) + 5) % 10)

while not stack_pria.is_empty() and not stack_wanita.is_empty():
    # if stack_pria.pop() == stack_wanita.pop():
    #     counter_cinta += 10
    # else:
    #     counter_cinta -= 1
    if stack_pria.peek() == stack_wanita.peek():
        counter_cinta += 10
    else:
        counter_cinta -= 1
    stack_pria.pop()
    stack_wanita.pop()

if counter_cinta < 0:
    print("0%")
elif counter_cinta > 100:
    print("100%")
else:
    print(counter_cinta, "%")
