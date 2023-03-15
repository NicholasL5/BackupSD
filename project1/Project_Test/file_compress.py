import heapq
import os

class Node:
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        if other is None:
            return False
        elif not isinstance(other, Node):
            return False
        else:
            return True if self.count == other.count else False


class FileCompress:
    def __init__(self):
        self.char_dict = {}
        self.heap = []
        self.code_dict = {}
        self.reverse_map = {}

    def buat_tree(self):
        node1 = heapq.heappop(self.heap)
        node2 = heapq.heappop(self.heap)
        parent_node = Node(None, node1.count + node2.count)
        parent_node.left = node1
        parent_node.right = node2
        heapq.heappush(self.heap, parent_node)

    def buat_heap(self, val):
        for i in val:
            heapq.heappush(self.heap, Node(i, int(val[i])))
        return self.heap

    def map_char(self, string):
        count = {}
        for char in string:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        return count

    def buat_code_util(self, node: Node, code):
        if node is None:
            return
        if node.char is not None:
            self.code_dict[node.char] = code
            self.reverse_map[code] = node.char

        self.buat_code_util(node.left, (code + "0"))
        self.buat_code_util(node.right, (code + "1"))

    def ganti_text(self, text):
        text_code = ""

        for char in text:
            text_code += self.code_dict[char]

        pad = 8 - len(text_code) % 8
        for i in range(pad):
            text_code += "0"
        padded_info = "{0:08b}".format(pad)
        text_code = padded_info + text_code
        return text_code

    def to_binary(self, text_code):
        b = bytearray()
        for i in range(0, len(text_code), 8):
            byte = text_code[i:i + 8]
            b.append(int(byte, 2))
        return b

    def buat_code(self):
        root = heapq.heappop(self.heap)
        code = ""
        self.buat_code_util(root, code)

    def compress(self, file):
        file_dir, file_extension = os.path.splitext(file)
        print(file_dir)
        # search / terakhir
        index = file.rfind("/")
        parent_dir = file[0:(index + 1)]
        print(parent_dir)
        # buat folder compressed
        compressed_dir = parent_dir + "compressed/" + file_dir + "-compressed/"
        if not os.path.exists(compressed_dir):
            os.makedirs(compressed_dir)
        # output = compressed + nama file + extension .bin
        output_path = compressed_dir + file_dir + ".bin"
        # buat simpan data tabel code
        data_path = compressed_dir + "data.txt"

        with open(file, "r") as f:
            data = f.read()
            mapped = self.map_char(data)
            print(mapped)
            self.buat_heap(mapped)
            while len(self.heap) != 1:
                self.buat_tree()
            self.buat_code()
            text_code = self.ganti_text(data)
            output = self.to_binary(text_code)
            tabel_code = str(self.code_dict)

        with open(data_path, "w") as out:
            out.write(tabel_code)

        with open(output_path, "wb") as out:
            out.write(bytes(output))

# ------------------------------------------------------------
    def remove_padding(self,str_bits):
        padded_info = str_bits[:8]
        extra_padding = int(padded_info,2)

        str_bits = str_bits[8:]
        encoded_text = str_bits[:-1*extra_padding]

        return encoded_text

    def decode(self,text):
        code = ''
        decoded = ''
        print('reverse map',self.reverse_map)
        for bit in text:
            code += bit
            if (code in self.reverse_map):
                character = self.reverse_map[code]
                decoded += character
                code = ''
        return decoded

    def decompress(self, file):
        print(1)
        filnename, extension = os.path.splitext(file)
        output_path = filnename + "-decompressed.txt"

        print(1.2)
        with open(file,'rb') as f, open(output_path,'w') as output:
            string_of_bits = ''

            byte = f.read(1)
            while(len(byte)>0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8,'0')
                string_of_bits += bits
                byte = f.read(1)
        
            print(2)
            encoded = self.remove_padding(string_of_bits)
            print(encoded)
            print(3)
            decoded = self.decode(encoded)
            print(decoded)
            print(4)
            output.write(decoded)
        
        print('decompressed')
        return output_path

