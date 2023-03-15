arr = [["a", 4, 60],
     ["b", 2, 40],
     ["c", 6, 75],
     ["d", 5, 25],
     ["e", 3, 70],
     ["f", 1, 30],
     ["g", 3, 50],
     ["h", 1, 40],
     ["i", 6, 65],
     ["j", 4, 55]] 
# O(1)

arr.sort(key=lambda x:x[2],reverse=True)
# O(nlogn), default sort biasa = nlogn. Function lambda di key tidak signifikan karena hanya cek index2 nya, jadi tetap
# nlogn.

n = max(arr,key=lambda x:x[1])[1]
# max = O(n). function lambda juga tidak signifikan karena hanya melihat index 1 
jawaban = [None for _ in range(n)] 
# O(n) loop inisialisasi jawaban
for i in arr:
    # O(n) loop
    if None not in jawaban:
        # O(1) if
        break

    for j in range(i[1]-1, -1, -1):
        # O(n) loop karena worst case i[1] = i dengan deadline terbesar
        if jawaban[j] == None:
            # O(1)
            jawaban[j] = i[0]
            # O(1)
            break

# time complexity keseluruhan = O(n^2) u/ nested loop + O(n) + O(n) + O(nlogn)
print(jawaban)


