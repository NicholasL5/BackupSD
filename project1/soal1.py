import numpy as np
from itertools import groupby
from soal1_class import Mahasiswa, Kelas

masih_input = True
array = np.array([])
while masih_input:
    nama, nrp, ipk, sks = input("masukkan nama, nrp, ipk, sks: ").split(sep=",")
    # nama = input("masukkan nama:")
    # nrp = input("masukkan nrp:")
    # ipk = input("masukkan ipk:")
    # sks = input("masukkan jumlah sks:")
    mahasiswa = Mahasiswa(nama, nrp, float(ipk), int(sks))
    array = np.append(array, np.array([mahasiswa]))
    lanjut = input("lanjut input? y/n")
    if lanjut.lower() == 'n':
        masih_input = False

print()
kelas_sd = Kelas(array)
kelas_sd.hitung()


# # sampel data
# # memakai data manual

# mahasiswa1 = Mahasiswa("budi", "c10", 3.75, 24)
# mahasiswa2 = Mahasiswa("andi", "c11", 3.75, 20)
# mahasiswa3 = Mahasiswa("sapi", "c12", 3.5, 20)
# mahasiswa4 = Mahasiswa("topi", "c13", 3.60, 20)
# mahasiswa5 = Mahasiswa("yopi", "c14", 2.00, 18)
# mahasiswa6 = Mahasiswa("roti", "c15", 3.60, 22)
# mahasiswa7 = Mahasiswa("yeti", "c16", 3.00, 20)
# mahasiswa8 = Mahasiswa("sopi", "c17", 3.75, 20)
#
# array = [mahasiswa1, mahasiswa2, mahasiswa3, mahasiswa4, mahasiswa5, mahasiswa6, mahasiswa7, mahasiswa8]
#
# newArray = np.array([[item, item.ipk, item.jumSks] for item in array])
#
# newArray = newArray[np.lexsort((newArray[:,2], -newArray[:,1]))]
#
# counter = 0
# sks = 0
# for item in newArray:
#     if counter == 0 and sks == 0:
#         counter+=1
#         sks = item[2]
#         item[0].group = counter
#     else:
#         if item[2] != sks:
#             counter+=1
#             item[0].group = counter
#         else:
#             item[0].group = counter
#
# for item in newArray:
#     item[0].hitungPeluang(counter)
#     item[0].printMahasiswa()




