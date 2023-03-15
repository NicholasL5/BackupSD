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
            return 1
        else:
            lheight = self.get_max_height(node.left)
            rheight = self.get_max_height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1






