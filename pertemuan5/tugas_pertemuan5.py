import math
from itertools import permutations
from cobaQ import Queue

# class Queue:
#     def __init__(self):
#         self.front = self.rear = None
#
#     def isEmpty(self):
#         return self.front is None
#
#     def enqueue(self, new_data):
#         new_node = Node(new_data)
#         if self.isEmpty():
#             self.front = self.rear = new_node
#             return
#         self.rear.next = new_node
#         self.rear = new_node
#
#     def dequeue(self):
#         if self.isEmpty():
#             print("kosong")
#             return
#         temp = self.front
#         self.front = temp.next
#         return temp.data
#
#     def peek(self):
#         return self.front
#
#     def printQ(self):
#         itr = self.front
#         while itr:
#             if itr is self.rear:
#                 break
#             print(itr.data, end=" -> ")
#             itr = itr.next
#         print(itr.data)

def calc_distance(start, end):
    distance = math.sqrt(((end[0]-start[0])**2) + ((end[1]-start[1])**2))
    return distance


masih_input = True
list_jalur = []
while masih_input:
    koor_x, koor_y = input("masukkan input").split(sep=",")
    list_jalur.append((int(koor_x),int(koor_y)))
    ans = input("lanjut? y/n")
    if ans == "n":
        masih_input = False
print(list_jalur)

# generate semua kombinasi jalur yang mungkin
kombinasi_jalur = permutations(list_jalur)

default = (0,0)
list_Q = Queue()
list_Q.enqueue(default)

# menghitung jarak terpendek dari semua kemungkinan kombinasi jalur
jalur_pendek = 9999999999
for i in tuple(kombinasi_jalur):
    dist = 0
    default = (0,0)
    # print(i)
    for j in tuple(i):
        dist += calc_distance(default, j)
        # print(dist)
        default = j
    if dist < jalur_pendek:
        jalur_pendek = dist
        jalur_jawaban = i

print("jawaban:", jalur_pendek)
for i in jalur_jawaban:
    list_Q.enqueue(i)

list_Q.printQ()







# 0,1 || 0,-3 || 0,5 || 0,-7
