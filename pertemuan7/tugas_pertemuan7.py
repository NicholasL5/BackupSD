class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, start, dest, weight=1):
        self.graph[start][dest] = weight
        self.graph[dest][start] = weight

    def print_graph(self):
        for i in self.graph:
            print(i)

    def DFS(self,start, target):
        visited = set()
        print('DFS:', end='')

        if self.DFS_util(start, target, visited):
            print()
            return print("Yes")
        print()
        return print("No")

    def DFS_util(self,start, target, visited):
        visited.add(start)

        print(int(start)+1,end='->')
        for i in range(self.size):
            if i not in visited and self.graph[start][i] > 0:
                if i == target:
                    return True

                # return terus kalau ketemu target
                if self.DFS_util(i, target, visited):
                    return True

    def BFS(self, start, target):
        queue = []
        visited = [False for _ in range(self.size)]

        queue.append(start)
        visited[start] = True
        print('BFS:', int(start)+1, end="->")
        while queue:
            vertice = queue.pop(0)

            for i in range(self.size):
                if visited[i] is False and self.graph[vertice][i] > 0:
                    queue.append(i)
                    visited[i] = True
                    print(i+1, end='->')
                    if i == target:
                        print()
                        return print("Yes")
        print()
        return print("No")

jum_kota = int(input("input jumlah kota:"))

jum_jalur = int(input("input jumlah jalur:"))

town = Graph(jum_kota)

for i in range(1, jum_jalur+1):
    a,b = input(f"input jalur ke-{i}:").split(sep=" ")
    town.add_edge(int(a)-1, int(b)-1)

town.print_graph()
cari = True
while cari:
    # asumsi input dan output mulai dari 1 bukan dari 0. A = 1, B = 2
    a,b = input("cari jalur (kota dimulai dari 1): ").split(sep=" ")
    town.BFS(int(a)-1, int(b)-1)
    town.DFS(int(a)-1, int(b)-1)


