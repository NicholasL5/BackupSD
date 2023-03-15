import heapq
# index parent = (index child-1) // 2
# sort dari list
# mulai dari paling belakang 7 cek dengan 3, 3 cek 1, 1 cek 0. 6 cek 2, 2 cek 0 dst
#      0  1   2  3   4  5  6   7
li1 = [8, 7, 20, 19, 4, 1, 0, 99]


for i in range(len(li1)):
    li1[i] = li1[i]*-1



# heapify default = min heap
heapq.heapify(li1)
for i in range(len(li1)):
    li1[i] = li1[i]*-1
print(li1)

