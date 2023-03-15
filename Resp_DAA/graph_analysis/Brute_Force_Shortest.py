class Graph:
    def __init__(self, size):
        # implementasi matrix
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, start, dest, weight=1):
        self.graph[start][dest] = weight
        self.graph[dest][start] = weight

    def DFS(self,start, end):
        visited = []
        path = []
        total = 0
        weight = []
        print()
        print('DFS:', end='')
        self.DFS_util(start, end, path, weight, total, visited)

    def DFS_util(self, start, end, path, weight, total, visited):
        visited.append(start)
        path.append(start)
        if start == end:
            weight.append(total)

        # loop tiap edge
        for i in self.graph[start]:
            if self.graph[start].index(i) not in visited and i > 0:
                self.DFS_util(self.graph[start].index(i), end, path, weight, total, visited)

    def print_graph(self):
        for i in self.graph:
            print(i)

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(1, 3)



