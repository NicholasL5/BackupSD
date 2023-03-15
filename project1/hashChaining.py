class Node:
    def __init__(self, key=None, data=None):
        self.nextNode = None
        self.prevNode = None
        self.data = data
        self.key = key
    
    def append(self, key, data):
        if key == self.key:
            self.data = data
        elif self.nextNode is None:
            self.nextNode = Node(key, data) 
            self.nextNode.prevNode = self
        else:
            self.nextNode.append(key, data)

class HashMap:  #with chaining
    def __init__(self, table_size):
        self.map = [None for i in range(table_size)]
    
    def hash(self, data):
        res = 0
        i = 1
        for letter in data:
            res += ord(letter)
            # i += 1

        return res
    
    def insert(self, key, data):
        hashKey = self.hash(key)
        print(hashKey)
        hashKey = hashKey % len(self.map)

        if self.map[hashKey] is None:
            self.map[hashKey] = Node(key, data)
        else:
            self.map[hashKey].append(key, data)            

    def search(self, key):
        hashKey = self.hash(key) % len(self.map)
        curNode = self.map[hashKey]
        while curNode is not None:
            if curNode.key == key:
                return curNode.data
            curNode = curNode.nextNode
        return False

    def delete(self, key):
        hashKey = self.hash(key) % len(self.map)
        curNode = self.map[hashKey]
        while curNode is not None:
            if curNode.key == key:
                if curNode.prevNode == None:
                    self.map[hashKey] = curNode.nextNode
                elif curNode.nextNode == None:
                    curNode.prevNode.nextNode = None
                else:
                    curNode.prevNode.nextNode = curNode.nextNode
                    curNode.nextNode.prevNode = curNode.prevNode

            curNode = curNode.nextNode




    def display(self):
        counter = 0
        for node in self.map:
            print("MapIndex", counter, end=": ")
            curNode = node
            while curNode is not None:
                print("{", curNode.key, ":", curNode.data, end=" }, ")
                curNode = curNode.nextNode
            print(" ")
            counter+=1

hashing = HashMap(10)

hashing.insert("Hans", 90)
hashing.insert("Winson", 100)
hashing.insert("Exel", 95)
hashing.insert("Henry", 98)
hashing.insert("Palit", 99)
hashing.display()
print(hashing.search("Winson"))
hashing.insert("Winson", 93)
hashing.display()
hashing.delete("Winson")
hashing.display()


        

        
        
    