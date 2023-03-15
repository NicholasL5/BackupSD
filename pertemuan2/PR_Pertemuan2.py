from CDLL import Node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


jum_kota = int(input("input jumlah kota:"))

jum_jalur = int(input("input jumlah jalur:"))

list_rute = []
list = []
# dimulai dengan array of node, urut dari 1-jumlah kota
for i in range(1, jum_kota+1):
    newNode = Node(i)
    list.append(newNode)
print(list)
counter = 1

while counter <= jum_jalur:
    flag = False
    input1, input2 = input(f"input jalur ke {counter}: ").split(sep=" ")
    # input -1 karena digunakan pada index
    input1 = int(input1) - 1
    input2 = int(input2) - 1

    # mengecek apakah ada input jalur yang dibalik. Karena asumsinya adalah misal jalur 1 - 3 akan sama dengan 3 - 1
    for item in list_rute:
        if input1 in item and input2 in item:
            print("invalid input")
            flag = True
            break
    if not flag:
        if int(input1) > jum_kota or int(input2) > jum_kota:
            print("invalid input")
        else:
            # mengecek jika prev dan next ada maka invalid input
            if list[input1].prev is not None and list[input1].next is not None:
                print("invalid input")

            # menambah node jika next dan prev kosong
            elif list[input1].next is None and list[input2].prev is None:
                list[input1].next = list[input2]
                list[input2].prev = list[input1]
                list_rute.append((input1, input2))
                counter += 1
            else:
                print("invalid input")

    print(list_rute)


is_asking = True
counter = 0

while is_asking:
    ketemu = False
    input1, input2 = input("cari jalur: ").split(sep=" ")
    input1 = int(input1)
    input2 = int(input2)
    temp = list[input1 - 1]
    # loop selama temp masih ada next dicek apakah data = input
    while temp is not None:
        if temp.data == input2:
            print("Yes")
            ketemu = True
            break
        temp = temp.next

    if ketemu is False:
        temp = list[input1 - 1]
        # sama seperti loop atas hanya saja mundur
        while temp is not None:
            if temp.data == input2:
                print("Yes")
                ketemu = True
                break
            temp = temp.prev
    if ketemu is False:
        print("No")
