import sys

class Graph:
    def __init__(self, size):
        # implementasi matrix
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, start, dest, weight=1):
        self.graph[start][dest] = weight
        self.graph[dest][start] = weight

    def DFS(self,start):
        visited = set()
        print()
        print('DFS:', end='')
        self.DFS_util(start, visited)

    def DFS_util(self,start, visited):
        visited.add(start)
        print(start,end='-->')
        for i in range(self.size):
            if i not in visited and self.graph[start][i] > 0:
                self.DFS_util(i, visited)

    def to_adjacentList(self):
        """mengubah representasi matrix menjadi adjacent list pakai dictionary python"""
        graph_list = {key:[] for key in range(self.size)}
        for i in range(self.size):
            for j in range(self.size):
                if self.graph[i][j] > 0:
                    graph_list[i].append(j)
        return graph_list

    def BFS(self, start):
        queue = []
        visited = [False for _ in range(self.size)]

        queue.append(start)
        visited[start] = True
        print('BFS:', start, end="-->")
        while queue:
            vertice = queue.pop(0)
            for i in range(self.size):
                if visited[i] is False and self.graph[vertice][i] > 0:
                    queue.append(i)
                    visited[i] = True
                    print(i, end='->')

    def print_graph(self):
        for i in self.graph:
            print(i)

    def dijkstra(self,start):
        infinity = sys.maxsize
        visited = []
        weight = []
        for i in range(self.size):
            weight.append(infinity)


        path = {}
        weight[start] = 0
        # isi path adalah nilai path dan prev node
        path[start] = [weight[start], start]

        while len(visited) != self.size:
            print()
            print(f"mulai dari node {start}")
            visited.append(start)
            # counter untuk tracking index
            counter = 0
            for j in self.graph[start]:

                if j > 0 and counter not in visited:
                    print(f"edge ke node {counter}")
                    # calculate distance
                    dist = weight[start] + j
                    if dist < weight[counter]:
                        weight[counter] = dist
                        path[counter] = [dist, start]
                    print("weight edge", path)
                counter += 1

            edges = sorted([index for index in self.graph[start] if index > 0])
            for i in edges:
                if self.graph[start].index(i) not in visited:
                    start = self.graph[start].index(i)
                    break


        return path

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Graph:
#     def __init__(self, size):
#         # implementasi adjacent list
#         self.size = size
#         self.graph = [None for _ in range(size)]
#
#     def add_edge(self, start, dest):
#         new_node = Node(dest)
#         new_node.next = self.graph[start]
#         self.graph[start] = new_node
#
#         # kalau directed code dibawah ini dihapus
#         new_node = Node(start)
#         new_node.next = self.graph[dest]
#         self.graph[dest] = new_node
#
#
#
#     def print_graph(self):
#         for i in range(len(self.graph)):
#             print('Vertice: ',)
#             itr = self.graph[i]
#             while itr is not None:
#                 print(itr.data, end='->')
#                 itr = itr.next
#             print()


g = Graph(5)
g.add_edge(0,1, 2)
g.add_edge(0,2, 1)
g.add_edge(1,2, 5)
g.add_edge(2,3, 4)
g.add_edge(3,4, 2)
g.add_edge(0,4, 3)
g.print_graph()
path = g.dijkstra(0)
print(path)




