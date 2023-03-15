import sys
import time
list_angka = [3,6,4,8,2,7,5]

start_time = time.time()

for i in range(len(list_angka)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(list_angka)):
        if list_angka[min_idx] > list_angka[j]:
            min_idx = j


    list_angka[i], list_angka[min_idx] = list_angka[min_idx], list_angka[i]
    print(list_angka)


print("waktu")
print((time.time()-start_time)*1000)
