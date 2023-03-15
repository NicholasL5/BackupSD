# linkless
class Hash:
    def __init__(self, capacity:int=100):
        self.value_table = [None]*capacity
        self.capacity = capacity

    def hash_function(self, data):
        if type(data) is int:
            return data % self.capacity
        else:
            temp = 0
            for i in data:
                temp += ord(i)
            return temp % self.capacity

    def insert(self, data: any):
        index = self.hash_function(data)
        if self.value_table[index] is None:
            self.value_table[index] = [data]
        else:
            self.value_table[index].append(data)

    def print(self):
        for i in self.value_table:
            print(i)

    def search(self, find):
        index = self.hash_function(find)
        if self.value_table[index] is None:
            return False
        for i in self.value_table[index]:
            if i == find:
                return True
        return False


hashlinkless = Hash(10)
hashlinkless.insert(53)
hashlinkless.insert("JuStIN")
hashlinkless.insert(13)
hashlinkless.insert(43)
hashlinkless.insert(99)
hashlinkless.print()
print(hashlinkless.search(13))

