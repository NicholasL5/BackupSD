import numpy as np
class Mahasiswa:
    def __init__(self, nama, nrp, ipk:float, jumlahSks):
        self.nama = nama
        self.nrp = nrp
        self.ipk = ipk
        self.jumSks = jumlahSks
        self.peluang = 0
        self.group = None

    def printMahasiswa(self):
        print("nama :", self.nama)
        print("ipk :", self.ipk)
        print("sks :", self.jumSks)
        print("group:", self.group)
        print("peluang:", self.peluang)
        print()

    def hitungPeluang(self, jumlahGroup):
        self.peluang = 100 - ((self.group - 1)*100) / jumlahGroup

class Kelas:
    def __init__(self, array):
        self.array = array

    def hitung(self):
        new_array = np.array([[item, item.ipk, item.jumSks] for item in self.array])

        new_array = new_array[np.lexsort((new_array[:, 2], -new_array[:, 1]))]

        counter = 0
        sks = 0
        for item in new_array:
            if counter == 0 and sks == 0:
                counter += 1
                sks = item[2]
                item[0].group = counter
            else:
                if item[2] != sks:
                    counter += 1
                    item[0].group = counter
                else:
                    item[0].group = counter

        for item in new_array:
            item[0].hitungPeluang(counter)
            item[0].printMahasiswa()




