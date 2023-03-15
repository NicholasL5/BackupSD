from pertemuan3.cobastack import Stack
from pertemuan5.cobaQ import Queue

def check_movement(value:list):
    if value[0].lower() == "maju":
        print("mundur", value[1])
    elif value[0].lower() == "kiri":
        print("kanan", value[1])
    elif value[0].lower() == "kanan":
        print("kiri", value[1])
    elif value[0].lower() == "mundur":
        print("maju", value[1])

list_input = []
stack_input = Stack()
ans = True
while ans:
    perintah, jum = input("masukkan perintah dan banyaknya perintah contoh(maju,2):").split(sep=",")
    list_input.append([perintah, int(jum)])
    inpt = input("input lagi? y/n")
    if inpt.lower() == 'n':
        ans = False

for i in list_input:
    stack_input.push(i)

stack_input.show()

while not stack_input.is_empty():
    check_movement(stack_input.pop())
