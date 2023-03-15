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
        if temp is None:
            print("kosong")
        else:
            while temp.next is not None:
                print(temp.data)
                temp = temp.next
            print(temp.data)

    def clear(self):
        self.top = None

import string
import random


def generate_stack(size: int):
    # string.ascii_lowercase adalah semua huruf dan digits adalah angka
    stack_input = Stack()
    chars = string.ascii_lowercase + string.digits
    for i in range(size):
        stack_input.push(random.choice(chars))
    return stack_input


if __name__ == "__main__":
    is_input = True
    stack_num = Stack()
    stack_alphabet = Stack()
    temp = Stack()
    while is_input:
        jum_data = int(input("masukkan jumlah data:"))
        stack_start = generate_stack(jum_data)
        print("stack start:")
        stack_start.show()
        print()
        while not stack_start.is_empty():
            temp.clear()
            character = stack_start.pop()
            if character.isdigit():
                if stack_num.is_empty():
                    stack_num.push(character)
                else:
                    if int(stack_num.peek()) > int(character):
                        stack_num.push(character)
                    else:
                        while not stack_num.is_empty() and int(stack_num.peek()) < int(character):
                            temp.push(stack_num.pop())
                        stack_num.push(character)
                        while not temp.is_empty():
                            stack_num.push(temp.pop())
            else:
                if stack_alphabet.is_empty():
                    stack_alphabet.push(character)

                else:
                    if ord(stack_alphabet.peek()) > ord(character):
                        stack_alphabet.push(character)
                    else:
                        while not stack_alphabet.is_empty() and ord(stack_alphabet.peek()) < ord(character):
                            temp.push(stack_alphabet.pop())
                        stack_alphabet.push(character)
                        while not temp.is_empty():
                            stack_alphabet.push(temp.pop())


        print("stack angka:")
        stack_num.show()
        print()
        print("stack alphabet:")
        stack_alphabet.show()
        ans = input("lanjut? y/n")
        if ans == "n":
            stack_num.clear()
            stack_alphabet.clear()
            temp.clear()
            is_input = False

