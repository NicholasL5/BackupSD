import numpy as np


def appendEISCH(table, data):
    hashKey = customhash(data) % len(table)
    # print(hashKey)
    if table[hashKey][0] is None:  # lek ra onok data
        table[hashKey][0] = data
    else:  # lek ws onok data e
        isFull = True
        link = hashKey
        while table[link][1] is not None:      #get the last link
            link = table[link][1]
        for i in range(len(table)-1, -1, -1):
            if table[i][0] is None:
                #set data
                table[i][0] = data
                isFull = False
                #set link
                table[link][1] = i     
                break
            # else:
            #     link = i
        if isFull:
            print("Hash Table Full")

def appendEISCH(table, data):
    hashKey = customhash(data) % len(table)
    # print(hashKey)
    if table[hashKey][0] is None:  # lek ra onok data
        table[hashKey][0] = data
    else:  # lek ws onok data e
        isFull = True
        for i in range(len(table)-1, -1, -1):
            if table[i][0] is None:
                #setting data
                table[i][0] = data
                isFull = False
                #setting link 
                table[i][1] = table[hashKey][1] 
                table[hashKey][1] = i                    
                break
            # else:
            #     link = i
        if isFull:
            print("Hash Table Full")



def customhash(data):
    res = 0
    i = 1
    for letter in data:
        res += ord(letter)+i
        i += 1
    return res

#init hashtable
tableSize = 7
hashTable = [[None, None] for i in range(7)]
appendEISCH(hashTable, "punten")
appendEISCH(hashTable, "punten")
appendEISCH(hashTable, "punten")
appendEISCH(hashTable, "punten")
# appendEISCH(hashTable, "puntens")
# appendEISCH(hashTable, "puntens")
# appendEISCH(hashTable, "jir")
# appendEISCH(hashTable, "puntsens")
print(np.array(hashTable))
