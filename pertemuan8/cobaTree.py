class Node:
    def __init__(self, data):
        self.left = self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def get_max_height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.get_max_height(node.left)
            rheight = self.get_max_height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def print_inorder(root, target):
    if root:
        if print_inorder(root.left, target):
            return True
        print(root.data, end=" ")
        if root.data == target:
            print("ketemu")
            return True
        if print_inorder(root.right, target):
            return True


def print_preorder(root, target):
    if root:
        print(root.data, end=" ")
        if root.data == target:
            print("ketemu")
            return True
        if print_preorder(root.left, target):
            return True
        if print_preorder(root.right, target):
            return True

def print_postorder(root, target):
    if root:
        if print_preorder(root.left, target):
            return True
        if print_preorder(root.right, target):
            return True
        print(root.data, end=" ")
        if root.data == target:
            print("ketemu")
            return True


def printLevelOrder(root, target):
    flag = False
    print("BFS/Level Order Traversal:")
    h = height_lvl(root)
    for i in range(0, h):
        print(f"level - {i}")
        if printCurrLvl(root, i, target):
            print(f"ketemu di level {i}", end=" ")
            flag = True
        print()
    if not flag:
        print(f"tidak ada data {target}")


def height_lvl(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height_lvl(node.left)
        rheight = height_lvl(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def printCurrLvl(root, lvl, target):
    flag = False
    if root is None:
        return
    if lvl == 0:
        print(root.data, end=" ")
        if root.data == target:
            return True
    elif lvl > 0:
        if printCurrLvl(root.left, lvl - 1, target):
            flag = True
        if printCurrLvl(root.right, lvl - 1, target):
            flag = True
        if flag:
            return True


my_tree = Node(8)
my_tree.insert(3)
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(12)
my_tree.insert(9)
my_tree.insert(6)
my_tree.insert(15)
my_tree.insert(13)
my_tree.get_max_height(my_tree)
# asumsi jika ketemu sisa node tetap di print
# BFS
printLevelOrder(my_tree, 4)
target = 12
print("DFS:")
if not print_inorder(my_tree, target):
    print(f"tidak ada {target} di tree")
if not print_preorder(my_tree, target):
    print(f"tidak ada {target} di tree")
if not print_postorder(my_tree, target):
    print(f"tidak ada {target} di tree")


