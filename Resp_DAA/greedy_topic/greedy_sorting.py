import random

# pekerjaan = []
# n = int(input("banyak pekerjaan:"))
# for i in range(n):
#     pekerjaan.append(list(map(int, input("input jam start, end:").split(sep=","))))

def random_list():
    n = random.randrange(3,13)
    li = []
    for i in range(int(n)):
        val_a = random.randrange(1, 13)
        while val_a == 12:
            val_a = random.randrange(1,13)
        val_b = random.randrange(val_a+1, 13)
        li.append([val_a, val_b])

    return li


def check_overlap(li1, li2):
    return True if (li1[0]) <= (li2[1]) and (li2[0]) < (li1[1]) else False

# data untuk gagal overlap
data = [[1,3], [3,5], [5,7], [7,9], [4,6], [2,3], [2,4], [1,4], [6,8], [6,9]]


# data untuk gagal S-E. solusi tukar 1,3 dan 4,6
# data = [[4,6],[1,3], [3,5], [5,7], [7,12]]

# data untuk gagal S. solusi optimal [[1, 2], [2, 3], [4, 6], [6, 8], [8, 9]]. solusi hilangkan [3,7]
# data = [[3,7],[5,8],[1,2],[8,9],[4,6],[1,5], [6,8],[2,3]]

# data = random_list()
# sort S-E
# data = sorted(data, key=lambda x:(x[1]-x[0]))
# untuk pertimbangan sort berdasarkan angka depan kalau S-E sama. Kalau pakai ini jawaban pasti benar
# data = sorted(data, key=lambda x:((x[1]-x[0]), x[0]) )

# data = [[1,10], [2,3],[3,4],[4,5]]

# sort S
# data = sorted(data, key=lambda x:(x[0]))

# sort E (gabisa gagal kayaknya)
# data = sorted(data, key=lambda x:(x[1]))

# sort overlap
count_overlap = []
for i in data:
    counter = 0
    for j in data:
        status = False
        if i != j:
            if j[0] < i[0]:
                status = check_overlap(j, i)
            else:
                status = check_overlap(i, j)
        if status:
            counter += 1
    count_overlap.append(counter)
#
print(data)
print(count_overlap)
data = [x for (y,x) in sorted(zip(count_overlap,data), key=lambda x: x[0])]


pekerjaan = [data[0]]


for i in data[1:]:
    counter = 0
    for j in pekerjaan:
        status = True
        if j[0] < i[0]:
            status = check_overlap(j, i)
        else:
            status = check_overlap(i, j)
        if not status:
            counter += 1
    if counter == len(pekerjaan):
        pekerjaan.append(i)

print("selesai",end="")
print(pekerjaan)








