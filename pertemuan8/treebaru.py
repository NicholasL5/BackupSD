class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Graph:
    def __init__(self, vertex):
        self.size = vertex
        self.matrix = [[0 for _ in range(vertex)] for _ in range(vertex)]

    def insert(self, start, dest, val=1):
        self.matrix[start-1][dest-1] = val
        self.matrix[dest-1][start-1] = val

    def DFS(self, start):
        visited = [False for _ in range(self.size)]
        print()
        self.DFS_util(start, visited)

    def DFS_util(self, s, visited):
        visited[s] = True
        print(s)
        for i in range(len(self.matrix[s])):
            if self.matrix[s][i] != 0 and visited[i] is False:
                self.DFS_util(i, visited)


    def BFS(self, start):
        visited = [False for _ in range(self.size)]
        q = [start]
        while False in visited:
            popped = q.pop(0)
            visited[popped] = True
            print(popped)
            for i in range(len(self.matrix[popped])):
                if self.matrix[popped][i] != 0 and visited[i] == False:
                    q.append(i)

    def print(self):
        for i in self.matrix:
            print(i)

    def print_all_path(self, s, d):
        visited = [False for _ in range(self.size)]
        path = []
        self.print_all_path_util(s, d, visited, path)

    def print_all_path_util(self, s, d, visited, path):
        visited[s] = True
        path.append(s)

        if s == d:
            print(path)
        else:
            for i in range(len(self.matrix[s])):
                if self.matrix[s][i] != 0 and visited[i] is not True:
                    self.print_all_path_util(i, d, visited, path)
        path.pop()
        visited[s] = False

class Tree:
    def __init__(self):
        self.root = None

    def print_all_level(self):
        h = self.get_max_height()
        for i in range(h):
            print()
            self.print_current(self.root, i)

    def print_current(self,node,level):
        if node is None:
            return
        if level == 0:
            print(node.data, end=" ")
        else:
            self.print_current(node.left, level-1)
            self.print_current(node.right, level-1)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_util(self.root, data)

    def insert_util(self, node, data):
        if not node:
            return Node(data)
        elif data < node.data:
            node.left = self.insert_util(node.left, data)
        else:
            node.right = self.insert_util(node.right, data)
        return node

    def get_max_height(self):
        return self.get_max_height_util(self.root)

    def get_max_height_util(self, node:Node):
        if not node:
            return 0
        lheight = self.get_max_height_util(node.left)
        rheight = self.get_max_height_util(node.right)
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

tree = Tree()
tree.insert(8)
tree.insert(3)
tree.insert(12)
tree.insert(2)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(15)
tree.insert(13)
tree.print_all_level()
print()
# print(tree.get_max_height())

graph = Graph(4)
graph.insert(1,2)
graph.insert(1,4)
graph.insert(2,4)
graph.insert(2,3)
graph.insert(3,4)
# graph.BFS(0)
graph.DFS(0)
print()
graph.print_all_path(0,3)

