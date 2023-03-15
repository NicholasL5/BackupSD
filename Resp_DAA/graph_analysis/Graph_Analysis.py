import sys

class Node:
    def __init__(self, weight, source):
        self.weight = weight
        self.source = source

    # def get_weight(self):
    #     return self.weight
    #
    # def get_source(self):
    #     return self.source
    #
    # def change_node(self, weight, source):
    #     self.weight = weight
    #     self.source = source


class Graph:
    def __init__(self, size):
        # implementasi matrix
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, start, dest, weight=1):
        self.graph[start][dest] = weight
        self.graph[dest][start] = weight

    def DFS(self, start):
        stack = []
        visited = [False for _ in range(self.size)]
        list_visited = []
        counter = 1
        stack.append(start)

        visited[start] = True
        print('DFS:',end=" ")
        while stack:
            print()
            print(f"iterasi ke - {counter}")
            print(f"stack sebelum: {stack}")
            vertice = stack.pop()
            list_visited.append(vertice)
            print(f"stack sesudah pop: {stack}")
            copy_edges = self.graph[vertice].copy()

            # sorting list semua edge yang ada pada satu vertice
            # sorting edge dibalik supaya pada saat dicek edge yang bernilai paling besar akan dimasukkan ke stack duluan
            # sehingga pada saat stack di pop, hasil pop akan selalu edge yang paling pendek
            edges = sorted([index for index in copy_edges if index > 0],reverse=True)
            while edges:
                # mengambil node, node sama dengan index dari nilai edge
                index = copy_edges.index(edges[0])
                if visited[index] is False:
                    stack.append(index)
                    visited[index] = True

                copy_edges[index] = 0
                edges.pop(0)
            for i in list_visited:
                print(self.get_name(i), end=" -> ")
            counter += 1

    def get_name(self, index):
        if index == 0:
            return "Gate"
        elif index == 1:
            return "Court Yard"
        elif index == 2:
            return "Barracks"
        elif index == 3:
            return "Training Ground"
        elif index == 4:
            return "Hall"
        elif index == 5:
            return "Kitchen"
        elif index == 6:
            return "Armory"
        elif index == 7:
            return "Bath"

    def BFS(self, start):
        queue = []
        visited = [False for _ in range(self.size)]
        list_visited = []
        counter = 1
        queue.append(start)
        visited[start] = True
        list_visited.append(start)
        print('BFS:', end=" ")
        while queue:
            print()
            print(f"iterasi ke - {counter}")
            print(f"que sebelum: {queue}")
            vertice = queue.pop(0)
            print(f"que sesudah deque: {queue}")
            copy_edges = self.graph[vertice].copy()
            edges = sorted([index for index in copy_edges if index > 0])

            while edges:
                index = copy_edges.index(edges[0])
                if visited[index] is False:
                    queue.append(index)
                    visited[index] = True
                    list_visited.append(index)

                copy_edges[index] = 0
                edges.pop(0)
            print(f"que sesudah add: {queue}")
            for i in list_visited:
                print(self.get_name(i),end=" -> ")
            counter += 1

    def remove_edge(self, start, dest):
        self.graph[start][dest] = 0
        self.graph[dest][start] = 0

    def dijkstra(self, start, dest):
        infinity = sys.maxsize
        visited = set()
        que_node = []
        weight = []
        for i in range(self.size):
            weight.append(infinity)

        path = {}
        weight[start] = 0
        # path adalah dictionary dengan key = node dan value = list yang isinya jarak terpendek dari titik awal ke
        # node key, dan node yang harus dilewati
        path[start] = [weight[start], start]
        prev_start = start

        while len(visited) != self.size:
            print()
            print(f"mulai dari node {start} atau {self.get_name(start)}")
            visited.add(start)
            # append queue untuk melihat node mana saja yang dikunjungi (belum tentu paling pendek)
            if start not in que_node:
                que_node.append(start)
            # counter untuk tracking index atau node tujuan
            counter = 0
            for j in self.graph[start]:

                if j > 0:
                    print(f"edge ke node {counter}")
                    # hitung jarak (weight node + nilai edge)
                    dist = weight[start] + j

                    # kalau jarak hitungan lebih kecil dari weight node ganti
                    # update path ke node tersebut. path[key] = [jarak terpendek baru, node yang harus dilewati]
                    if dist < weight[counter]:
                        weight[counter] = dist
                        path[counter] = [dist, start]
                    print("weight edge", path)
                counter += 1

            # sort semua edge di node start, pilih edge yang paling pendek
            edges = sorted([index for index in self.graph[start] if index > 0])
            flag = False
            for i in edges:
                # pilih edge terpendek kalau node tujuan belum di visit
                if self.graph[start].index(i) not in visited:
                    prev_start = start
                    start = self.graph[start].index(i)
                    flag = True
                    break
            # kalau tidak ada edge yang memenuhi, kembali ke node sebelum sekarang
            if not flag:
                start = prev_start
                if start == que_node[0]:
                    prev_start = que_node[0]
                else:
                    prev_start = que_node[que_node.index(prev_start) - 1]

        # semua node sudah di visit, hasil akhir path sudah terbentuk
        # hasil akhir jarak terpendek bisa didapat dari melihat isi dictionary path, path[destination]
        # backtrack seperti di link di gc
        print()
        stack = []
        val = path[dest]
        stack.append(dest)
        while val[0] != 0:
            stack.append(val[1])
            val = path[val[1]]
        print("jawaban:")
        print(path[dest][0])
        # copy untuk print nama node
        copy_stack = stack.copy()
        while stack:
            print(stack.pop(), end="->")
        print()
        while copy_stack:
            print(self.get_name(copy_stack.pop()), end=" -> ")
        print()
        print("path akhir:")
        return path

    def print_graph(self):
        for i in self.graph:
            print(i)

#   0 ,     1    ,   2     ,        3        ,  4  ,    5   ,   6   , 7
# Gate, Courtyard, Barracks, Training Grounds, Hall, Kitchen, Armory, Bath.

graph = Graph(8)
# gate-courtyard
graph.add_edge(0, 1, 12)
# gate-kitchen
graph.add_edge(0, 5, 9)
# courtyard-armory
graph.add_edge(1, 6, 1)
# courtyard-hall
graph.add_edge(1, 4, 4)
# hall-armory
graph.add_edge(4, 6, 5)
# hall-kitchen
graph.add_edge(4, 5, 2)
# hall-bath
graph.add_edge(4, 7, 3)
# bath-barrack
graph.add_edge(7, 2, 1)
# hall-barrack
graph.add_edge(4, 2, 3)
# hall-TG
graph.add_edge(4, 3, 10)
# armory-TG
graph.add_edge(6, 3, 2)
# barrack-TG
graph.add_edge(2, 3, 5)
# barrack-armory
graph.add_edge(2, 6, 11)

graph.print_graph()
# graph.BFS(0)
# print()
# graph.DFS(0)
# print()
# d

print("soal 3")
print(graph.dijkstra(2, 1))

print("soal 4")
print(graph.dijkstra(0, 7))

# print("soal 5")
# graph.remove_edge(2,7)
# graph.remove_edge(2,4)
# print(graph.dijkstra(7,2))


# graph.add_edge(2,7)
# graph.add_edge(2,4)
# print("soal 6")
# graph.remove_edge(4,1)
# graph.remove_edge(4,2)
# graph.remove_edge(4,3)
# graph.remove_edge(4,6)
# graph.remove_edge(4,7)
# print(graph.dijkstra(2,5))

print("soal 7a")
graph.dijkstra(2,6)
print("ganti")
print(graph.dijkstra(6,0))

# print("soal 7b")
# print(graph.dijkstra(0,2))
