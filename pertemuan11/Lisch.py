class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Eisch:
    def __init__(self, capacity:int = 100):
        self.hash_table = [Node() for _ in range(capacity)]
        self.capacity = capacity

    def hash_function(self, data):
        if type(data) is int:
            return data % self.capacity
        else:
            temp = 0
            for i in data:
                temp += ord(i)
            return temp % self.capacity

    def insert(self, data):
        index = self.hash_function(data)
        if self.hash_table[index].data is None:
            self.hash_table[index].data = data
        else:
            itr = self.hash_table[index]
            for i in range(self.capacity-1, -1, -1):
                if self.hash_table[i].data is None:
                    self.hash_table[i].data = data
                    self.hash_table[itr.data].next = i
                    itr.next = i
                    break

    def print(self):
        for i in self.hash_table:
            print(f"{i.data} {i.next}")