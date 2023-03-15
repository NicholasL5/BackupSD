class Tumbuhan:
    def __init__(self):
        self.status = 0

    def getNama(self):
        if self.status == 1:
            return "Tunas"
        if self.status == 2:
            return "Prajurit"
        if self.status == 3:
            return "Jendral"
        if self.status == 4:
            return "Raja"


from itertools import groupby

def Tumbuh(hari, array):
    # basis
    if hari > 0:
        Tumbuh(hari-1, array)
        print("hari ke ", hari)
        for i in array:
            if i.status < 4:
                i.status += 1
            elif i.status == 4:
                array.append(Tumbuhan())

        sorted_array = sorted(array, key=lambda tumbuhan: tumbuhan.status, reverse=True)
        grouped = [list(result) for key, result in groupby(sorted_array, key=lambda tumbuhan: tumbuhan.status)]

        for item in grouped:
            print(len(item), item[0].getNama())


tunas = Tumbuhan()
arr = [tunas]
Tumbuh(10,arr)


