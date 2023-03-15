import sys


class Graph:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def insert(self, s, d, val):
        self.matrix[s][d] = val

    def search_edge(self, s, d):
        """:return nilai edge dari 2 vertex"""
        return self.matrix[s][d]

    def print_all_path(self, s, d):
        """
        sama seperti DFS, rekursi vertex pertama yang terhubung, kalau vertex tersebut adalah tujuan atau tidak
        ada vertex yang bisa dituju lagi, mundur, lanjut ke vertex yang terhubung selanjutnya
        """

        visited = [False for _ in range(self.size)]
        path = []
        all_path = []
        all_path = self.print_all_path_utils(s, d, visited, path, all_path)
        return all_path

    def print_all_path_utils(self, s, d, visited, path, all_path):
        flag = False
        visited[s] = True
        path.append(s)
        if s == d:
            flag = True
            print(path)
            all_path.append(path.copy())
        else:
            for i in range(len(self.matrix[s])):
                if visited[i] is False and self.matrix[s][i] != 0:
                    self.print_all_path_utils(i, d, visited, path, all_path)
        # kalau ketemu d (tujuan) atau tidak ada vertex yang terhubung lagi, kembali ke vertex sebelumnya
        # dan lanjutkan DFS
        path.pop()
        visited[s] = False
        if flag or True not in visited:
            return all_path


def change_name(arr):
    copy = []
    for i in arr:
        if i == 0:
            copy.append("A")
        elif i == 1:
            copy.append("B")
        elif i == 2:
            copy.append("C")
        elif i == 3:
            copy.append("D")
        elif i == 4:
            copy.append("E")
        elif i == 5:
            copy.append("F")
        elif i == 6:
            copy.append("G")
    return copy


def copy_with_name(arr):
    """untuk ganti representasi angka jadi huruf"""
    res = []
    for i in arr:
        res.append(change_name(i))
    return res


def count_time(path_dict):
    """hitung semua cost dan time semua path"""
    count = 0
    for i in path:
        val = [0, 0]
        for j in range(len(i) - 1):
            val[0] += graph.search_edge(i[j], i[j + 1])[0]
            val[1] += graph.search_edge(i[j], i[j + 1])[1]
        path_dict[count] = val
        count += 1
    return path_dict


graph = Graph(7)
graph.insert(0, 1, (15, 10))
graph.insert(0, 2, (5, 10))
graph.insert(0, 3, (10, 10))
graph.insert(0, 6, (50, 10))

graph.insert(1, 4, (5, 10))

graph.insert(2, 1, (5, 10))
graph.insert(2, 3, (3, 10))

graph.insert(3, 5, (15, 10))

graph.insert(4, 2, (2, 10))
graph.insert(4, 5, (1, 10))
graph.insert(4, 6, (10, 10))

graph.insert(5, 4, (1, 10))
graph.insert(5, 6, (5, 10))


print("A. semua kemungkinan path (memakai DFS):")
path = graph.print_all_path(0, 6)
# print(path)
print("\ndalam huruf:")
res = copy_with_name(path)
for i in res:
    print(i)


path_dict = {}
path_dict = count_time(path_dict)
# print(path_dict)


min_val = sys.maxsize
index = 0
# untuk mencari minimum cost dari semua jumlah cost yang ada (yang dibawah 50)
for i in path_dict.keys():
    if path_dict[i][0] < 50 and path_dict[i][1] < min_val:
        min_val = path_dict[i][1]

print("\nB. Cost terkecil dan Waktu tempuh dibawah 50:")
for i in path_dict.keys():
    if path_dict[i][1] == min_val:
        print(res[i], end=" -> ")
        print(path_dict[i])


