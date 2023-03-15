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
            print(temp.data, end="")
            temp = temp.next
        print(temp.data)




