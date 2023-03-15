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
                    self.hash_table[i].next = itr.next
                    itr.next = i
                    break

    def print(self):
        for i in self.hash_table:
            print(f"{i.data} {i.next}")

    def search(self, data):
        tmp = self.hash_function(data)
        return self.search_util(data, tmp)

    def search_util(self, data, index:int):
        if self.hash_table[index].data == data:
            return True
        else:
            if self.search_util(data,self.hash_table[index].next):
                return True
        return False

hash_ei = Eisch(10)
# 53, 13, 43, 18
hash_ei.insert(43)
hash_ei.insert(53)
hash_ei.insert(13)
hash_ei.insert(18)
hash_ei.print()

print(hash_ei.search(18))